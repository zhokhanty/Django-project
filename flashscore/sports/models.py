from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='sport_icons/', null=True, blank=True)

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='league_icons/', null=True, blank=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='teams_icons/', null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Player(models.model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    num_of_player = models.IntegerField()
    position = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Coach(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    exp = models.IntegerField()