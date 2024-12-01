from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD

    path('league/<int:league_id>/table/', views.league_table_view, name='league_table'),
=======
>>>>>>> 69fb49fd9b086aab8df72868e46cb86f3f929080
    # Sport CRUD
    path('sport/create/', views.create_sport, name='create_sport'),
    path('sport/<str:strSport>/', views.sport_detail, name='sport_detail'),
    path('sport/<int:id>/update/', views.update_sport, name='update_sport'),
    path('sport/<int:id>/delete/', views.delete_sport, name='delete_sport'),

    # League CRUD
    path('league/create/', views.create_league, name='create_league'),
    path('league/<str:strLeague>/', views.league_detail, name='league_detail'),
    path('league/<int:id>/update/', views.update_league, name="update_league"),
    path('league/<int:id>/delete/', views.delete_league, name="delete_league"),

    # Team CRUD
    path('team/create/', views.create_team, name='create_team'),
    path('team/<int:id>/', views.team_detail, name='team_detail'),
    path('team/<int:id>/update/', views.update_team, name='update_team'),
    path('team/<int:id>/delete/', views.delete_team, name='delete_team'),

    # Player CRUD
    path('player/create/', views.create_player, name='create_player'),
    path('player/<int:id>/', views.player_detail, name='player_detail'),
    path('player/<int:id>/update/', views.update_player, name='update_player'),
    path('player/<int:id>/delete/', views.delete_player, name='delete_player'),

    # Coach CRUD
    path('coach/create/', views.create_coach, name='create_coach'),
    path('coach/<int:id>/', views.coach_detail, name='coach_detail'),
    path('coach/<int:id>/update/', views.update_coach, name='update_coach'),
    path('coach/<int:id>/delete/', views.delete_coach, name='delete_coach'),

    path('search/', views.global_search, name='global_search'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)