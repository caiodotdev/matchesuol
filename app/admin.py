#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


class MatchInline(admin.TabularInline):
    model = Match


class CompeticaoAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [MatchInline]
    list_display = ("id", "nome")


admin.site.register(Competicao, CompeticaoAdmin)


class TimeAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    list_display = ("id", "id_time", "nome_completo", "nome_comum", "brasao", "sigla", "tipo")


admin.site.register(Time, TimeAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = (
        "id", "id_match", "competicao", "id_competicao", "time1", "time2", "data", "horario", "local", "estadio",
        "rodada",
        "posicao", "placar1", "placar2", "penalti1", "penalti2", "eliminou_jogo_volta", "classificou_gols_fora",
        "datahora",
        "desempate_time1", "desempate_time2")


admin.site.register(Match, MatchAdmin)
