from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Sport, League, Team, Player, Coach

# Sport Views
class SportListView(ListView):
    model = Sport
    template_name = 'sport/sport_list.html'

class SportDetailView(DetailView):
    model = Sport
    template_name = 'sport/sport_detail.html'

class SportCreateView(LoginRequiredMixin, CreateView):
    model = Sport
    template_name = 'sport/sport_form.html'
    fields = ['name', 'icon']

class SportUpdateView(LoginRequiredMixin, UpdateView):
    model = Sport
    template_name = 'sport/sport_form.html'
    fields = ['name', 'icon']

class SportDeleteView(LoginRequiredMixin, DeleteView):
    model = Sport
    template_name = 'sport_confirm_delete.html'
    success_url = reverse_lazy('sport_list')

# League Views
class LeagueListView(ListView):
    model = League
    template_name = 'league_list.html'

class LeagueDetailView(DetailView):
    model = League
    template_name = 'league_detail.html'

class LeagueCreateView(CreateView):
    model = League
    template_name = 'league_form.html'
    fields = ['name', 'icon', 'sport']

class LeagueUpdateView(UpdateView):
    model = League
    template_name = 'league_form.html'
    fields = ['name', 'icon', 'sport']

class LeagueDeleteView(DeleteView):
    model = League
    template_name = 'league_confirm_delete.html'
    success_url = reverse_lazy('league_list')

# Team Views
class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'

class TeamCreateView(CreateView):
    model = Team
    template_name = 'team_form.html'
    fields = ['name', 'icon', 'league']

class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'team_form.html'
    fields = ['name', 'icon', 'league']

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'team_confirm_delete.html'
    success_url = reverse_lazy('team_list')

# Player Views
class PlayerListView(ListView):
    model = Player
    template_name = 'player_list.html'

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'player_detail.html'

class PlayerCreateView(CreateView):
    model = Player
    template_name = 'player_form.html'
    fields = ['firstname', 'lastname', 'num_of_player', 'position', 'date_of_birth', 'team']

class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'player_form.html'
    fields = ['firstname', 'lastname', 'num_of_player', 'position', 'date_of_birth', 'team']

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player_confirm_delete.html'
    success_url = reverse_lazy('player_list')

# Coach Views
class CoachListView(ListView):
    model = Coach
    template_name = 'coach_list.html'

class CoachDetailView(DetailView):
    model = Coach
    template_name = 'coach_detail.html'

class CoachCreateView(CreateView):
    model = Coach
    template_name = 'coach_form.html'
    fields = ['firstname', 'lastname', 'date_of_birth', 'team', 'exp']

class CoachUpdateView(UpdateView):
    model = Coach
    template_name = 'coach_form.html'
    fields = ['firstname', 'lastname', 'date_of_birth', 'team', 'exp']

class CoachDeleteView(DeleteView):
    model = Coach
    template_name = 'coach_confirm_delete.html'
    success_url = reverse_lazy('coach_list')