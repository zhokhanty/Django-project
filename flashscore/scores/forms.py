from django import forms
from .models import Sport, League, Team, Player, Coach


class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name', 'icon']


class LeagueForm(forms.ModelForm):
    sport = forms.ModelChoiceField(
        queryset=Sport.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Sport"
    )

    class Meta:
        model = League
        fields = ['name', 'icon', 'sport']


class TeamForm(forms.ModelForm):
    leagues = forms.ModelMultipleChoiceField(
        queryset=League.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Leagues"
    )

    class Meta:
        model = Team
        fields = ['name', 'icon', 'leagues', 'points_l', 'points_c']


class PlayerForm(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Team"
    )

    class Meta:
        model = Player
        fields = [
            'firstname', 'lastname', 'num_of_player',
            'position', 'date_of_birth', 'team'
        ]


class CoachForm(forms.ModelForm):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Team"
    )

    class Meta:
        model = Coach
        fields = ['firstname', 'lastname', 'date_of_birth', 'team', 'exp']