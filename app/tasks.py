import datetime

from celery import shared_task
from django_celery_results.models import TaskResult

from .models import Match, Competicao, Time
from .serializers import MatchSerializer
from .uol_jogos import UolAPI

"""
This module defines various Celery tasks used for Spleeter Web.
"""


@shared_task()
def clean_tasks_results():
    qs = TaskResult.objects.all()
    print('---- Clean all Results')
    qs.delete()
    print('---- Clean all Results - Done')


@shared_task()
def update_matches():
    api = UolAPI()
    count_existing = 0
    matches = api.get_matches()
    print('qtd matches by UOL: ', len(matches))
    for match in matches:
        if not Match.objects.filter(id_match=match['id']).exists():
            match_data = match
            competicao = Competicao.objects.get_or_create(nome=match['competicao'])
            time1 = Time.objects.get_or_create(nome_comum=match['time1']['nome-comum'],
                                               nome_completo=match['time1']['nome-completo'],
                                               sigla=match['time1']['sigla'],
                                               tipo=match['time1']['tipo'],
                                               brasao=match['time1']['brasao'])
            time2 = Time.objects.get_or_create(nome_comum=match['time2']['nome-comum'],
                                               nome_completo=match['time2']['nome-completo'],
                                               sigla=match['time2']['sigla'],
                                               tipo=match['time2']['tipo'],
                                               brasao=match['time2']['brasao'])
            match_data['competicao'] = competicao[0].pk
            match_data['time1'] = time1[0].pk
            match_data['time2'] = time2[0].pk
            match_data['data'] = datetime.datetime.strptime(match['data'], "%Y-%m-%d")
            match_data['eliminou_jogo_volta'] = match['eliminou-jogo-volta']
            match_data['classificou_gols_fora'] = match['classificou-gols-fora']
            match_data['id_match'] = match['id']
            item = MatchSerializer(data=match_data)
            if item.is_valid():
                item.save()
            else:
                print(item.errors)
        else:
            match_data = match
            item_db = Match.objects.filter(id_match=match['id']).first()
            match_data['competicao'] = item_db.competicao.pk
            match_data['time1'] = item_db.time1.pk
            match_data['time2'] = item_db.time2.pk
            match_data['data'] = datetime.datetime.strptime(match['data'], "%Y-%m-%d")
            item = MatchSerializer(instance=item_db, data=match_data, partial=True)
            if item.is_valid():
                item.save()
                count_existing = count_existing + 1
    print('Updates performed: ', count_existing)
