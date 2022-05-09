from rest_framework import viewsets

from django_filters import rest_framework as filters

from . import (
    serializers,
    models
)

import django_filters



class CompeticaoFilter(django_filters.FilterSet):
    class Meta:
        model = models.Competicao
        fields = ["id", "nome"]


class CompeticaoViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.CompeticaoSerializer
    queryset = models.Competicao.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CompeticaoFilter



class TimeFilter(django_filters.FilterSet):
    class Meta:
        model = models.Time
        fields = ["id", "id_time", "nome_completo", "nome_comum", "brasao", "sigla", "tipo"]


class TimeViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.TimeSerializer
    queryset = models.Time.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeFilter



class MatchFilter(django_filters.FilterSet):
    class Meta:
        model = models.Match
        fields = ["id", "id_match", "competicao__nome", "id_competicao", "time1__id", "time2__id", "data", "horario", "local", "estadio", "rodada", "posicao", "placar1", "placar2", "penalti1", "penalti2", "eliminou_jogo_volta", "classificou_gols_fora", "datahora", "desempate_time1", "desempate_time2"]


class MatchViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.MatchSerializer
    queryset = models.Match.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MatchFilter

