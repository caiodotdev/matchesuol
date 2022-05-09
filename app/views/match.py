#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView, DeleteView, UpdateView
)
from django.views.generic.list import ListView

try:
    from django.core.urlresolvers import reverse_lazy
except ImportError:
    from django.urls import reverse_lazy, reverse

from app.models import Match, Competicao, Time
from app.forms import MatchForm
from app.mixins import MatchMixin
from app.conf import MATCH_DETAIL_URL_NAME, MATCH_LIST_URL_NAME

import django_filters


class MatchFormSetManagement(object):
    formsets = []

    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            self.object = form.save()

            for Formset in self.formsets:
                formset = context["{}set".format(str(Formset.model.__name__).lower())]
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()
        return super(MatchFormSetManagement, self).form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(MatchFormSetManagement, self).get_context_data(**kwargs)
        for Formset in self.formsets:
            if self.request.POST:
                data["{}set".format(str(Formset.model.__name__).lower())] = Formset(self.request.POST,
                                                                                    self.request.FILES,
                                                                                    instance=self.object)
            else:
                data["{}set".format(str(Formset.model.__name__).lower())] = Formset(instance=self.object)
        return data


class MatchFilter(django_filters.FilterSet):
    data_inicial = django_filters.DateFilter(
        field_name='data',
        lookup_expr='gte',
        label='Data Inicial',
    )
    data_final = django_filters.DateFilter(
        field_name='data',
        lookup_expr='lte',
        label='Data Final',
    )
    competicao = django_filters.ModelChoiceFilter(
        field_name='competicao__nome',
        lookup_expr='icontains',
        label='Competição',
        queryset=Competicao.objects.all(),
    )
    time1 = django_filters.ModelChoiceFilter(
        field_name='time1__nome_comum',
        lookup_expr='icontains',
        label='Time 1',
        queryset=Time.objects.all(),
    )
    time2 = django_filters.ModelChoiceFilter(
        field_name='time2__nome_comum',
        lookup_expr='icontains',
        label='Time 2',
        queryset=Time.objects.all(),
    )

    class Meta:
        model = Match
        fields = []


class ListFull(LoginRequiredMixin, MatchMixin, ListView):
    """
    List all Matchs
    """
    login_url = '/admin/login/'
    template_name = 'match/list_full.html'
    model = Match
    context_object_name = 'matchs'
    ordering = 'data'
    paginate_by = 10
    search = ''

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = MatchFilter(self.request.GET, queryset)
        queryset = self.search_general(filter.qs)
        queryset = self.ordering_data(queryset)
        # update_matches()
        return queryset

    def search_general(self, qs):
        if 'search' in self.request.GET:
            self.search = self.request.GET['search']
            if self.search:
                search = self.search
                qs = qs.filter(
                    Q(Q(competicao__nome__icontains=search) | Q(time1__nome_comum__icontains=search) | Q(
                        time2__nome_comum__icontains=search)))
        return qs

    def get_ordering(self):
        if 'ordering' in self.request.GET:
            self.ordering = self.request.GET['ordering']
            if self.ordering:
                return self.ordering
            else:
                self.ordering = 'data'
        return self.ordering

    def ordering_data(self, qs):
        qs = qs.order_by(self.get_ordering())
        return qs

    def get_context_data(self, **kwargs):
        context = super(ListFull, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = MatchFilter(self.request.GET, queryset)
        page_size = self.get_paginate_by(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context.update(**{
                'ordering': self.ordering,
                'search': self.search,
                'filter': filter,
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            })
        else:
            context.update(**{
                'search': self.search,
                'ordering': self.ordering,
                'filter': filter,
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            })
        return context


class Create(LoginRequiredMixin, MatchMixin, PermissionRequiredMixin, MatchFormSetManagement, CreateView):
    """
    Create a Match
    """
    login_url = '/admin/login/'
    model = Match
    permission_required = (
        'app.add_match'
    )
    form_class = MatchForm
    template_name = 'match/create.html'
    context_object_name = 'match'

    def get_context_data(self, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy(MATCH_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_initial(self):
        data = super(Create, self).get_initial()
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Match criado com sucesso')
        return super(Create, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Create, self).form_invalid(form)


class Detail(LoginRequiredMixin, MatchMixin, DetailView):
    """
    Detail of a Match
    """
    login_url = '/admin/login/'
    model = Match
    template_name = 'match/detail.html'
    context_object_name = 'match'

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)
        return context


class Update(LoginRequiredMixin, MatchMixin, PermissionRequiredMixin, MatchFormSetManagement, UpdateView):
    """
    Update a Match
    """
    login_url = '/admin/login/'
    model = Match
    template_name = 'match/update.html'
    context_object_name = 'match'
    form_class = MatchForm
    permission_required = (
        'app.change_match'
    )

    def get_initial(self):
        data = super(Update, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy(MATCH_DETAIL_URL_NAME, kwargs=self.kwargs_for_reverse_url())

    def get_context_data(self, **kwargs):
        data = super(Update, self).get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Match atualizado com sucesso')
        return super(Update, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(Update, self).form_invalid(form)


class Delete(LoginRequiredMixin, MatchMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a Match
    """
    login_url = '/admin/login/'
    model = Match
    permission_required = (
        'app.delete_match'
    )
    template_name = 'match/delete.html'
    context_object_name = 'match'

    def get_context_data(self, **kwargs):
        context = super(Delete, self).get_context_data(**kwargs)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(Delete, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Match removido com sucesso')
        return super(Delete, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy(MATCH_LIST_URL_NAME)
