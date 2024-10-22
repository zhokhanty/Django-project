from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import TeamDetailView, PlayerDetailView, CoachDetailView, LeagueTableView


urlpatterns = [
    path('', views.home, name='home'),
    path('sport/<int:id>/', views.sport_detail, name='sport_detail'),
    path('league/<int:league_id>/', views.league_detail, name='league_detail'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
    path('coach/<int:pk>/', CoachDetailView.as_view(), name='coach_detail'),
    path('search/', views.global_search, name='global_search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)