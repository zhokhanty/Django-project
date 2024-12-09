import requests
from django.core.management.base import BaseCommand
from scores.models import Sport, League, Team
import json
from django.core.files.base import ContentFile

# Данные о лигах
LEAGUES = {
    "EnglandPL": 4328,
    "Bundesliga": 4331,
    "Seria A": 4332,
    "LaLiga": 4335,
    "Liga 1": 4334,
}

API_URL = "https://www.thesportsdb.com/api/v1/json/3/lookuptable.php"

class Command(BaseCommand):
    help = "Загружает таблицы футбольных лиг из API и обновляет существующие команды"

    def handle(self, *args, **kwargs):
        football, _ = Sport.objects.get_or_create(name="Football")

        for league_name, league_id in LEAGUES.items():
            league, _ = League.objects.get_or_create(name=league_name, sport=football)

            response = requests.get(API_URL, params={"l": league_id, "s": "2024-2025"})
            data = response.json()

            if data and "table" in data:
                for team_data in data["table"]:
                    try:
                        team_name = team_data["strTeam"]
                        team_badge_url = team_data.get("strTeamBadge")
                        points = int(team_data["intPoints"])

                        team, created = Team.objects.get_or_create(name=team_name)

                        if created or not team.icon:
                            if team_badge_url:
                                badge_response = requests.get(team_badge_url)
                                if badge_response.status_code == 200:
                                    file_name = f"{team_name.replace(' ', '_')}_badge.jpg"
                                    team.icon.save(file_name, ContentFile(badge_response.content), save=False)

                        team.points_l = points
                        team.save()

                        if league not in team.leagues.all():
                            team.leagues.add(league)

                        action = "created" if created else "updated"
                        self.stdout.write(self.style.SUCCESS(f"Team {team_name} {action} в {league_name}."))
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f"Пропущен ключ {e} в данных команды: {team_data}"))
            else:
                self.stdout.write(self.style.WARNING(f"Нет данных для лиги {league_name}."))

        self.stdout.write(self.style.SUCCESS("Все лиги успешно обработаны!"))