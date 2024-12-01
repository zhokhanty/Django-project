import json
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .services import fetch_sports_data, fetch_leagues_by_sport, fetch_teams_by_league
from .models import Sport, League, Team, Player, Coach
from .forms import SportForm
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt

def home(request):
    sports = fetch_sports_data()
    context = {
        'sports': sports,
    }
    return render(request, 'scores/home.html', context)

# Sport CRUD
@csrf_exempt
def create_sport(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sport = Sport.objects.create(
            name=data.get("name"),
            icon=data.get("icon")
        )
        return JsonResponse({
            'id': sport.id,
            'name': sport.name,
            'icon': sport.icon.url if sport.icon else None
        }, status=201)
    
def sport_detail(request, strSport):
    sport = fetch_sports_data()
    leagues = fetch_leagues_by_sport(strSport)
    if not leagues:
        raise Http404("Leagues not found for the specified sport.")
    
    return render(request, 'scores/sport_detail.html', {'sport': sport, 'leagues': leagues})

@csrf_exempt
def update_sport(request, id):
    if request.method == 'PUT':
        sport = get_object_or_404(Sport, id=id)
        data = json.loads(request.body)
        
        # Updating fields
        sport.name = data.get("name", sport.name)
        sport.icon = data.get("icon", sport.icon)
        
        sport.save()
        
        return JsonResponse({
            'id': sport.id,
            'name': sport.name,
            'icon': sport.icon.url if sport.icon else None
        })

@csrf_exempt
def delete_sport(request, id):
    if request.method == 'DELETE':
        sport = get_object_or_404(Sport, id=id)
        sport.delete()
        return JsonResponse({'message': 'Sport deleted successfully'}, status=204)
    
# League CRUD
@csrf_exempt
def create_league(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        sport_id = data.get("id")
        if sport_id is None:
            return JsonResponse({'error': 'sport_id is required'}, status=400)

        try:
            sport = get_object_or_404(Sport, id=sport_id)
        except Http404:
            return JsonResponse({'error': 'Sport not found'}, status=404)

        league = League.objects.create(
            name=data.get("name"),
            icon=data.get("icon"),
            sport=sport
        )
        return JsonResponse({
            'id': league.id,
            'name': league.name,
            'icon': league.icon.url if league.icon else None,
            'sport_id': league.sport.id
        }, status=201)
    
def league_detail(request, strLeague):
    teams = fetch_teams_by_league(strLeague)
    league = get_object_or_404(League, name=strLeague)

    league_table_entries = Team.objects.filter(league=league).order_by('-points_c')
    
    context = {
        'teams': teams,
        'league_table_entries': league_table_entries,
    }
    return render(request, 'scores/league_detail.html', context)

@csrf_exempt
def update_league(request, id):
    if request.method == 'PUT':
        league = get_object_or_404(League, id=id)
        data = json.loads(request.body)
        
        league.name = data.get("name", league.name)
        league.icon = data.get("icon", league.icon)
        league.sport = get_object_or_404(Sport, id=data.get("sport_id", league.sport.id))
        
        league.save()
        
        return JsonResponse({
            'id': league.id,
            'name': league.name,
            'icon': league.icon.url if league.icon else None,
            'sport': league.sport.id
        })

@csrf_exempt
def delete_league(request, id):
    if request.method == 'DELETE':
        league = get_object_or_404(League, id=id)
        league.delete()
        return JsonResponse({'message': 'League deleted successfully'}, status=204)
    
# Team CRUD 
@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        leagues = League.objects.filter(id__in=data.get("leagues", []))
        team = Team.objects.create(
            name=data.get("name"),
            icon=data.get("icon"),
            points_l=data.get("points_l", 0),
            points_c=data.get("points_c", 0)
        )
        team.leagues.set(leagues)
        return JsonResponse({
            'id': team.id,
            'name': team.name,
            'icon': team.icon.url if team.icon else None,
            'leagues': [league.id for league in team.leagues.all()],
            'points_l': team.points_l,
            'points_c': team.points_c
        }, status=201)

def team_detail(request, id):
    team = get_object_or_404(Team, id=id)
    players = team.players.all()
    return render(request, 'scores/team_detail.html', {'team': team, 'players': players})

@csrf_exempt
def update_team(request, id):
    if request.method == 'PUT':
        team = get_object_or_404(Team, id=id)
        data = json.loads(request.body)
        
        team.name = data.get("name", team.name)
        team.icon = data.get("icon", team.icon)
        team.points_l = data.get("points_l", team.points_l)
        team.points_c = data.get("points_c", team.points_c)
        
        leagues = League.objects.filter(id__in=data.get("leagues", []))
        team.leagues.set(leagues)
        
        team.save()
        
        return JsonResponse({
            'id': team.id,
            'name': team.name,
            'icon': team.icon.url if team.icon else None,
            'leagues': [league.id for league in team.leagues.all()],
            'points_l': team.points_l,
            'points_c': team.points_c
        })

@csrf_exempt
def delete_team(request, id):
    if request.method == 'DELETE':
        team = get_object_or_404(Team, id=id)
        team.delete()
        return JsonResponse({'message': 'Team deleted successfully'}, status=204)

# Player CRUD
@csrf_exempt
def create_player(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        team_id = data.get("id")
        if team_id is None:
            return JsonResponse({'error': 'team_id is required'}, status=400)

        try:
            team = get_object_or_404(Team, id=team_id)
        except Http404:
            return JsonResponse({'error': 'Team not found'}, status=404)
        
        player = Player.objects.create(
            firstname=data.get("firstname"),
            lastname=data.get("lastname"),
            num_of_player=data.get("num_of_player"),
            position=data.get("position"),
            date_of_birth=data.get("date_of_birth"),
            team=team
        )
        return JsonResponse({
            'id': player.id,
            'name': f"{player.firstname} {player.lastname}",
            'num_of_player': player.num_of_player,
            'position': player.position,
            'date_of_birth': player.date_of_birth,
            'team': player.team.id
        }, status=201)

def player_detail(request, id):
    player = get_object_or_404(Player, id=id)
    return render(request, 'scores/player_detail.html', {"player": player})

@csrf_exempt
def update_player(request, id):
    if request.method == 'PUT':
        player = get_object_or_404(Player, id=id)
        data = json.loads(request.body)
        
        player.firstname = data.get("firstname", player.firstname)
        player.lastname = data.get("lastname", player.lastname)
        player.num_of_player = data.get("num_of_player", player.num_of_player)
        player.position = data.get("position", player.position)
        player.date_of_birth = data.get("date_of_birth", player.date_of_birth)
        player.team = get_object_or_404(Team, id=data.get("team_id", player.team.id))
        
        player.save()
        
        return JsonResponse({
            'id': player.id,
            'name': f"{player.firstname} {player.lastname}",
            'num_of_player': player.num_of_player,
            'position': player.position,
            'date_of_birth': player.date_of_birth,
            'team': player.team.id
        })

@csrf_exempt
def delete_player(request, id):
    if request.method == 'DELETE':
        player = get_object_or_404(Player, id=id)
        player.delete()
        return JsonResponse({'message': 'Player deleted successfully'}, status=204)

# Coach CRUD
@csrf_exempt
def create_coach(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        team_id = data.get("id")
        if team_id is None:
            return JsonResponse({'error': 'team_id is required'}, status=400)

        try:
            team = get_object_or_404(Team, id=team_id)
        except Http404:
            return JsonResponse({'error': 'Team not found'}, status=404)
        
        coach = Coach.objects.create(
            firstname=data.get("firstname"),
            lastname=data.get("lastname"),
            date_of_birth=data.get("date_of_birth"),
            exp=data.get("exp"),
            team=team
        )
        return JsonResponse({
            'id': coach.id,
            'name': f"{coach.firstname} {coach.lastname}",
            'date_of_birth': coach.date_of_birth,
            'exp': coach.exp,
            'team': coach.team.id
        }, status=201)

def coach_detail(request, id):
    coach = get_object_or_404(Coach, id=id)
    return render(request, 'scores/coach_detail.html', {'coach': coach})

@csrf_exempt
def update_coach(request, id):
    if request.method == 'PUT':
        coach = get_object_or_404(Coach, id=id)
        data = json.loads(request.body)
        
        coach.firstname = data.get("firstname", coach.firstname)
        coach.lastname = data.get("lastname", coach.lastname)
        coach.date_of_birth = data.get("date_of_birth", coach.date_of_birth)
        coach.exp = data.get("exp", coach.exp)
        coach.team = get_object_or_404(Team, id=data.get("team_id", coach.team.id))
        
        coach.save()
        
        return JsonResponse({
            'id': coach.id,
            'name': f"{coach.firstname} {coach.lastname}",
            'date_of_birth': coach.date_of_birth,
            'exp': coach.exp,
            'team': coach.team.id
        })

@csrf_exempt
def delete_coach(request, id):
    if request.method == 'DELETE':
        coach = get_object_or_404(Coach, id=id)
        coach.delete()
        return JsonResponse({'message': 'Coach deleted successfully'}, status=204)

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


def league_table_view(request, league_id):
    """
    Отображение таблицы выбранной лиги.
    """
    league = get_object_or_404(League, id=league_id)
    teams = league.teams.order_by('-points_l', 'name')  # Сортировка по очкам и алфавиту

    context = {
        'league': league,
        'teams': teams,
    }
    return render(request, 'scores/league_table.html', context)