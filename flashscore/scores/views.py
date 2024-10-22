from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Sport, League, Team, Player, Coach
from .forms import SportForm
from django.views.generic import DetailView
from django.db.models import F
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Sport, League, Team, Player, Coach
from .serializers import SportSerializer, LeagueSerializer, TeamSerializer, PlayerSerializer, CoachSerializer




def home(request):
    sports = Sport.objects.all()
    context = {
        'sports': sports,
    }
    return render(request, 'scores/home.html', context)

def sport_detail(request, id):
    sport = get_object_or_404(Sport, id=id)
    leagues = sport.leagues.all()
    return render(request, 'scores/sport_detail.html', {'sport': sport, 'leagues': leagues})

def league_detail(request, league_id):
    league = League.objects.get(id=league_id)


    if league_id == 4:
        league_table_entries = Team.objects.filter(leagues=league).order_by('-points_c')
    else:
        league_table_entries = Team.objects.filter(leagues=league).order_by('-points_l')

    context = {
        'league': league,
        'league_table_entries': league_table_entries,
    }
    return render(request, 'scores/league_detail.html', context)

class TeamDetailView(DetailView):
    model = Team
    template_name = 'scores/team_detail.html'
    context_object_name = 'team'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'scores/player_detail.html'
    context_object_name = 'player'

class CoachDetailView(DetailView):
    model = Coach
    template_name = 'scores/coach_detail.html'
    context_object_name = 'coach'

class LeagueTableView(DetailView):
    model = League
    template_name = 'scores/league_table.html'
    context_object_name = 'league'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['matches'] = self.object.matches.all().order_by('-date')[:10]
        return context

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

# POST запрос для создания нового спорта
@api_view(['POST'])
def create_sport(request):
    if request.method == 'POST':
        serializer = SportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST запрос для создания новой лиги
@api_view(['POST'])
def create_league(request):
    if request.method == 'POST':
        serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST запрос для создания новой команды
@api_view(['POST'])
def create_team(request):
    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST запрос для создания нового игрока
@api_view(['POST'])
def create_player(request):
    if request.method == 'POST':
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST запрос для создания нового тренера
@api_view(['POST'])
def create_coach(request):
    if request.method == 'POST':
        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
