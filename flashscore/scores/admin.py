from django.contrib import admin
from .models import Sport, League, Team, Player, Coach

admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)