from .models import Sport, League, Team, Player, Coach
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .forms import SportForm, LeagueForm, TeamForm, PlayerForm, CoachForm
import requests
from django.shortcuts import render
from django.http import JsonResponse

def check_role(user, role):
    profile = getattr(user, 'profile', None)
    return profile and profile.role == role

def load_all_sports(request):
    try:
        # Fetch data from the API
        url = f"{API_BASE_URL}all_sports.php"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the API response
            sports_data = response.json().get('sports', [])
            
            # Save sports into the database (avoid duplicates)
            for sport in sports_data:
                Sport.objects.get_or_create(name=sport['strSport'])
            
            # Fetch all sports from the database
            sports = Sport.objects.all()

            # Render sports to the template
            return render(request, 'sports/home.html', {'sports': sports})
        else:
            # Handle API errors
            return JsonResponse({'error': 'Failed to fetch sports from API'}, status=response.status_code)
    except Exception as e:
        # Catch unexpected exceptions
        return JsonResponse({'error': str(e)}, status=500)

def sport_detail(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    return render(request, 'sports/sport_detail.html', {'sport': sport})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def sport_create(request):
    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sport_list')
    else:
        form = SportForm()
    return render(request, 'sports/sport_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def sport_update(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    if request.method == 'POST':
        form = SportForm(request.POST, request.FILES, instance=sport)
        if form.is_valid():
            form.save()
            return redirect('sport_list')
    else:
        form = SportForm(instance=sport)
    return render(request, 'sports/sport_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def sport_delete(request, sport_id):
    sport = get_object_or_404(Sport, id=sport_id)
    if request.method == 'POST':
        sport.delete()
        return redirect('sport_list')
    return render(request, 'sports/sport_confirm_delete.html', {'sport': sport})


# League Views
def league_list(request):
    leagues = League.objects.all()
    return render(request, 'leagues/league_list.html', {'leagues': leagues})

def league_detail(request, league_id):
    league = get_object_or_404(League, id=league_id)
    return render(request, 'leagues/league_detail.html', {'league': league})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def league_create(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('league_list')
    else:
        form = LeagueForm()
    return render(request, 'leagues/league_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def league_update(request, league_id):
    league = get_object_or_404(League, id=league_id)
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES, instance=league)
        if form.is_valid():
            form.save()
            return redirect('league_list')
    else:
        form = LeagueForm(instance=league)
    return render(request, 'leagues/league_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def league_delete(request, league_id):
    league = get_object_or_404(League, id=league_id)
    if request.method == 'POST':
        league.delete()
        return redirect('league_list')
    return render(request, 'leagues/league_confirm_delete.html', {'league': league})


# Team Views
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'teams/team_detail.html', {'team': team})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'teams/team_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def team_update(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'teams/team_form.html', {'form': form})

@csrf_exempt
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'teams/team_confirm_delete.html', {'team': team})


# Player Views
def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'players/player_detail.html', {'player': player})

@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'players/player_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def player_update(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/player_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'players/player_confirm_delete.html', {'player': player})


# Coach Views
def coach_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coaches/coach_list.html', {'coaches': coaches})

def coach_detail(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    return render(request, 'coaches/coach_detail.html', {'coach': coach})

@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def coach_create(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm()
    return render(request, 'coaches/coach_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def coach_update(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coach_list')
    else:
        form = CoachForm(instance=coach)
    return render(request, 'coaches/coach_form.html', {'form': form})

# Delete Coach (Restricted to Admins)
@login_required
@user_passes_test(lambda u: check_role(u, 'admin'))
def coach_delete(request, coach_id):
    coach = get_object_or_404(Coach, id=coach_id)
    if request.method == 'POST':
        coach.delete()
        return redirect('coach_list')
    return render(request, 'coaches/coach_confirm_delete.html', {'coach': coach})


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

API_BASE_URL = "https://www.thesportsdb.com/api/v1/json/3/"



def list_leagues(request):
    url = f"{API_BASE_URL}all_leagues.php"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('leagues', [])
        return render(request, 'sports/list_leagues.html', {'leagues': data})
    return JsonResponse({'error': 'Unable to fetch leagues'}, status=500)

def leagues_by_country(request, country, sport=None):
    url = f"{API_BASE_URL}search_all_leagues.php?c={country}"
    if sport:
        url += f"&s={sport}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('countrys', [])
        return render(request, 'sports/leagues_by_country.html', {'leagues': data, 'country': country})
    return JsonResponse({'error': 'Unable to fetch leagues'}, status=500)

def teams_in_league(request, league_name, country=None):
    url = f"{API_BASE_URL}search_all_teams.php?l={league_name}"
    if country:
        url += f"&c={country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('teams', [])
        return render(request, 'sports/teams_in_league.html', {'teams': data, 'league': league_name})
    return JsonResponse({'error': 'Unable to fetch teams'}, status=500)