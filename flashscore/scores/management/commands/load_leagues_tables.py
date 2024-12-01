import requests
from django.core.management.base import BaseCommand
from scores.models import Sport, League, Team
import json

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
    help = "Загружает таблицы футбольных лиг из API"

    def handle(self, *args, **kwargs):
        football, _ = Sport.objects.get_or_create(name="Football")

        for league_name, league_id in LEAGUES.items():
            # Получение или создание лиги
            league, _ = League.objects.get_or_create(name=league_name, sport=football)

            # Запрос к API
            response = requests.get(API_URL, params={"l": league_id, "s": "2024-2025"})
            data = response.json()

            if data and "table" in data:
                for team_data in data["table"]:
                    try:
                        # Извлечение данных из API
                        team_name = team_data["strTeam"]
                        team_badge = team_data.get("strBadge")  # Значение может быть пустым
                        points = int(team_data["intPoints"])
                        position = int(team_data["intRank"])

                        # Получение или создание команды
                        team, _ = Team.objects.get_or_create(name=team_name)
                        if team_badge:  # Если эмблема доступна, добавляем её
                            team.icon = team_badge
                        team.points_l = points
                        team.save()

                        # Добавление команды в лигу
                        team.leagues.add(league)

                        # Логирование успешной обработки команды
                        self.stdout.write(self.style.SUCCESS(f"Команда {team_name} добавлена в {league_name}."))
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f"Пропущен ключ {e} в данных команды: {team_data}"))
            else:
                self.stdout.write(self.style.WARNING(f"Нет данных для лиги {league_name}."))

        self.stdout.write(self.style.SUCCESS("Все лиги успешно обработаны!"))
