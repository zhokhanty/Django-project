from django.contrib import admin
from .models import Sport, League, Team, Player, Coach
from .models import Match

admin.site.register(Match)
admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)