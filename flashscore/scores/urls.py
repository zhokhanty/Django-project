from django.urls import path
from . import views
from .views import analytics_view

urlpatterns = [
    # Sports
    path('sports/', views.load_all_sports, name='sport_list'),
    path('sports/<int:sport_id>/', views.sport_detail, name='sport_detail'),
    path('sports/create/', views.sport_create, name='sport_create'),
    path('sports/<int:sport_id>/update/', views.sport_update, name='sport_update'),
    path('sports/<int:sport_id>/delete/', views.sport_delete, name='sport_delete'),

    # Leagues
    path('leagues/', views.league_list, name='league_list'),
    path('leagues/<int:league_id>/', views.league_detail, name='league_detail'),
    path('leagues/create/', views.league_create, name='league_create'),
    path('leagues/<int:league_id>/update/', views.league_update, name='league_update'),
    path('leagues/<int:league_id>/delete/', views.league_delete, name='league_delete'),

    # Teams
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:team_id>/update/', views.team_update, name='team_update'),
    path('teams/<int:team_id>/delete/', views.team_delete, name='team_delete'),

    # Players
    path('players/', views.player_list, name='player_list'),
    path('players/<int:player_id>/', views.player_detail, name='player_detail'),
    path('players/create/', views.player_create, name='player_create'),
    path('players/<int:player_id>/update/', views.player_update, name='player_update'),
    path('players/<int:player_id>/delete/', views.player_delete, name='player_delete'),
    path('analytics/', analytics_view, name='analytics'),
    # Coaches
    path('coaches/', views.coach_list, name='coach_list'),
    path('coaches/<int:coach_id>/', views.coach_detail, name='coach_detail'),
    path('coaches/create/', views.coach_create, name='coach_create'),
    path('coaches/<int:coach_id>/update/', views.coach_update, name='coach_update'),
    path('coaches/<int:coach_id>/delete/', views.coach_delete, name='coach_delete'),

    path('search/', views.global_search, name='global_search'),

    path('leagues/', views.list_leagues, name='list_leagues'),
    path('leagues/<str:country>/', views.leagues_by_country, name='leagues_by_country'),
    path('teams/<str:league_name>/', views.teams_in_league, name='teams_in_league'),
    path('league/<int:league_id>/table/', views.league_table_view, name='league_table'),
]
