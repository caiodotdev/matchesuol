from django.urls import path, include

from app import conf

from app.urls_api import api_urlpatterns

urlpatterns = []

urlpatterns += [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]

from app.views import match

urlpatterns += [
    # match
    path(
        '',
        match.ListFull.as_view(),
        name=conf.MATCH_LIST_URL_NAME
    ),
    path(
        'match/create/',
        match.Create.as_view(),
        name=conf.MATCH_CREATE_URL_NAME
    ),
    path(
        'match/<int:pk>/',
        match.Detail.as_view(),
        name=conf.MATCH_DETAIL_URL_NAME
    ),
    path(
        'match/<int:pk>/update/',
        match.Update.as_view(),
        name=conf.MATCH_UPDATE_URL_NAME
    ),
    path(
        'match/<int:pk>/delete/',
        match.Delete.as_view(),
        name=conf.MATCH_DELETE_URL_NAME
    )
]
urlpatterns += api_urlpatterns
