from rest_framework.routers import DefaultRouter
from app import (
    viewsets
)

api_urlpatterns = []

competicao_router = DefaultRouter()

competicao_router.register(
    r'^api/competicao',
    viewsets.CompeticaoViewSet,
    basename="competicao"
)

api_urlpatterns += competicao_router.urls
time_router = DefaultRouter()

time_router.register(
    r'^api/time',
    viewsets.TimeViewSet,
    basename="time"
)

api_urlpatterns += time_router.urls
match_router = DefaultRouter()

match_router.register(
    r'^api/match',
    viewsets.MatchViewSet,
    basename="match"
)

api_urlpatterns += match_router.urls
