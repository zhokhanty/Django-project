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

    def __str__(self):
        return self.name

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