from datetime import timezone

from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/sport_icons/', null=True, blank=True)

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/league_icons/', null=True, blank=True)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE, related_name='leagues')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/teams_icons/', null=True, blank=True)
    leagues = models.ManyToManyField('League', related_name='teams')
    points_l = models.IntegerField(default=0)
    points_c = models.IntegerField(default=0)

    @property
    def upcoming_matches(self):
        return self.match_set.filter(date__gte=timezone.now())

    @property
    def past_matches(self):
        return self.match_set.filter(date__lt=timezone.now())

class Player(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    num_of_player = models.IntegerField()
    position = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.team.name}"


class Coach(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    team = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='coach')
    exp = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.team.name}"

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_matches', on_delete=models.CASCADE)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)
    round_number = models.IntegerField()
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=50)
    date = models.DateTimeField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    round_number = models.IntegerField(null=True, blank=True)
    home_team_badge = models.URLField(max_length=500, blank=True, null=True)  # Значок домашней команды
    away_team_badge = models.URLField(max_length=500, blank=True, null=True)
    def is_past(self):
        return self.date < timezone.now()

    def is_upcoming(self):
        return self.date > timezone.now()