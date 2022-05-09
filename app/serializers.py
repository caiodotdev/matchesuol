from rest_framework import serializers

from app.models import Competicao


class CompeticaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competicao
        fields = ("id", "nome")


from app.models import Time


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ("id", "id_time", "nome_completo", "nome_comum", "brasao", "sigla", "tipo")


from app.models import Match


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
        "id", "id_match", "competicao", "id_competicao", "time1", "time2", "data", "horario", "local", "estadio",
        "rodada", "posicao", "placar1", "placar2", "penalti1", "penalti2", "eliminou_jogo_volta",
        "classificou_gols_fora", "datahora", "desempate_time1", "desempate_time2")
