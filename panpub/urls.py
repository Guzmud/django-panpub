#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url

from django_filters.views import FilterView

from panpub import filters, views

urlpatterns = [
    url(
        regex="^crafter/(?P<pk>\d+)/$",
        view=views.CrafterDetail.as_view(),
        name='crafter_detail',
    ),
    url(
        regex="^crafter/search/$",
        view=FilterView.as_view(filterset_class=filters.CrafterFilter),
        name='crafter_search',
    ),
    url(
        regex="^crafter/$",
        view=views.CrafterList.as_view(),
        name='crafter_list',
    ),

    url(
        regex="^corpus/~create/$",
        view=views.CorpusCreate.as_view(),
        name='corpus_create',
    ),
    url(
        regex="^corpus/(?P<pk>\d+)/~delete/$",
        view=views.CorpusDelete.as_view(),
        name='corpus_delete',
    ),
    url(
        regex="^corpus/(?P<pk>\d+)/$",
        view=views.CorpusDetail.as_view(),
        name='corpus_detail',
    ),
    url(
        regex="^corpus/(?P<pk>\d+)/~update/$",
        view=views.CorpusUpdate.as_view(),
        name='corpus_update',
    ),
    url(
        regex="^corpus/search/$",
        view=FilterView.as_view(filterset_class=filters.CorpusFilter),
        name='corpus_search',
    ),
    url(
        regex="^corpus/$",
        view=views.CorpusList.as_view(),
        name='corpus_list',
    ),

    url(
        regex="^content/(?P<pk>\d+)/$",
        view=views.ContentDetail.as_view(),
        name='content_detail',
    ),
    url(
        regex="^content/search/$",
        view=FilterView.as_view(filterset_class=filters.ContentFilter),
        name='content_search',
    ),
    url(
        regex="^content/$",
        view=views.ContentList.as_view(),
        name='content_list',
    ),

    url(
        regex="^text/~create/$",
        view=views.TextCreate.as_view(),
        name='text_create',
    ),
    url(
        regex="^text/(?P<pk>\d+)/~delete/$",
        view=views.TextDelete.as_view(),
        name='text_delete',
    ),
    url(
        regex="^text/(?P<pk>\d+)/$",
        view=views.TextDetail.as_view(),
        name='text_detail',
    ),
    url(
        regex="^text/(?P<pk>\d+)/~update/$",
        view=views.TextUpdate.as_view(),
        name='text_update',
    ),
    url(
        regex="^text/(?P<text_id>\d+)/export/(?P<export_format>\w+)/$",
        view=views.text_export,
        name='text_export',
    ),
    url(
        regex="^text/search/$",
        view=FilterView.as_view(filterset_class=filters.TextFilter),
        name='text_search',
    ),
    url(
        regex="^text/$",
        view=views.TextList.as_view(),
        name='text_list',
    ),

    url(
        regex="op/export/$",
        view=views.panpub_export,
        name='panpub_export',
    ),
]
