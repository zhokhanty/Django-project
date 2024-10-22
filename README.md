# Django-project
This project related to sports

## Members:
    * Bagythzhan Zhalgas 22B030317
    * Mussilimov Galymzhan 22B031186
    * Kyanysh Farabi 22B030489

## Description:

Our project dedicates to sports and we create our own project similar to flashscore. This project has two applications:

## 1. Scores:

This application includes management system of sport website and represent some models in below:

      Sports:
      
      This fundamental model includes popular sports. Each sport entry 
      comprises essential details such as the leagues.
      
      League:
      
      This component includes some difference leagues 
      in which we divide by countries and something like this.
      
      Team:
      
      In this component we added a some teams and distributed into leagues.
      
      Player:
      
      This component includes detailed information about players like 
      position where he playing, number of player, what team does he play for and etc.
      
      Coach:
      
      This component includes detailed information and each coach has its team.
      
## 2. Users:

This application aimed at the authorization of users. User can register of website to have a profile and some interesting things and also has log in and log out system.

## CRUD methods:

Our project has all CRUD method for each models:

    # Sport CRUD
    path('sport/create/', views.create_sport, name='create_sport'),
    path('sport/<int:id>/', views.sport_detail, name='sport_detail'),
    path('sport/<int:id>/update/', views.update_sport, name='update_sport'),
    path('sport/<int:id>/delete/', views.delete_sport, name='delete_sport'),

    # League CRUD
    path('league/create/', views.create_league, name='create_league'),
    path('league/<int:id>/', views.league_detail, name='league_detail'),
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

Our project also has search system:

    def global_search(request):
    query = request.GET.get('q')
    sports = Sport.objects.filter(name__icontains=query) if query else []
    teams = Team.objects.filter(name__icontains=query) if query else []
    players = Player.objects.filter(firstname__icontains=query) | Player.objects.filter(lastname__icontains=query) if query else []
    coaches = Coach.objects.filter(firstname__icontains=query) | Coach.objects.filter(lastname__icontains=query) if query else []

    context = {
        'query': query,
        'sports': sports,
        'teams': teams,
        'players': players,
        'coaches': coaches
    }
    return render(request, 'scores/search_results.html', context)
