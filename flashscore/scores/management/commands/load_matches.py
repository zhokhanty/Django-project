import requests
from django.core.management.base import BaseCommand
from scores.models import Sport, League, Team, Match
from datetime import datetime

# Данные о лигах
LEAGUES = {
    "EnglandPL": 4328,
    "Bundesliga": 4331,
    "Seria A": 4332,
    "LaLiga": 4335,
    "Liga 1": 4334,
}

API_URL = "https://www.thesportsdb.com/api/v1/json/3/eventsseason.php"

class Command(BaseCommand):
    help = "Загружает информацию о матчах для футбольных лиг и обновляет данные"

    def handle(self, *args, **kwargs):
        football, _ = Sport.objects.get_or_create(name="Football")

        for league_name, league_id in LEAGUES.items():
            league, _ = League.objects.get_or_create(name=league_name, sport=football)

            # Получаем данные о матчах для каждой лиги
            response = requests.get(API_URL, params={"id": league_id, "s": "2024-2025"})
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Ошибка загрузки данных для {league_name}."))
                continue

            data = response.json()

            if data and "events" in data:
                matches = []

                for match_data in data["events"]:
                    try:
                        event_name = match_data["strEvent"]
                        home_team_name = match_data["strHomeTeam"]
                        away_team_name = match_data["strAwayTeam"]
                        home_team_badge = match_data.get("strHomeTeamBadge", "")
                        away_team_badge = match_data.get("strAwayTeamBadge", "")
                        home_score = int(match_data["intHomeScore"]) if match_data["intHomeScore"] else None
                        away_score = int(match_data["intAwayScore"]) if match_data["intAwayScore"] else None
                        round_number = int(match_data["intRound"])
                        timestamp = datetime.strptime(match_data["strTimestamp"], "%Y-%m-%d %H:%M:%S")
                        status = match_data["strStatus"]
                        video_url = match_data.get("strVideo", "")

                        # Создаем или обновляем команды
                        home_team, _ = Team.objects.get_or_create(name=home_team_name, defaults={"icon": home_team_badge})
                        away_team, _ = Team.objects.get_or_create(name=away_team_name, defaults={"icon": away_team_badge})

                        # Обновляем значки, если они есть
                        if home_team_badge and not home_team.icon:
                            home_team.icon = home_team_badge
                            home_team.save()

                        if away_team_badge and not away_team.icon:
                            away_team.icon = away_team_badge
                            away_team.save()

                        # Создаем или обновляем матч
                        match, created = Match.objects.get_or_create(
                            league=league,
                            home_team=home_team,
                            away_team=away_team,
                            round_number=round_number,
                            timestamp=timestamp,
                            defaults={
                                "home_score": home_score,
                                "away_score": away_score,
                                "status": status,
                                "video_url": video_url,
                            },
                        )

                        # Обновляем данные матча, если они изменились
                        if not created:
                            match.home_score = home_score
                            match.away_score = away_score
                            match.status = status
                            match.video_url = video_url
                            match.save()

                        action = "created" if created else "updated"
                        matches.append(match)

                        self.stdout.write(self.style.SUCCESS(f"Match {event_name} {action} в лиге {league_name}."))

                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Ошибка обработки данных матча: {match_data}. Ошибка: {e}"))

                # Сортируем матчи по времени
                sorted_matches = sorted(matches, key=lambda x: x.timestamp)

                # Логируем отсортированные матчи
                self.stdout.write(self.style.SUCCESS(f"Матчи в лиге {league_name}:"))
                for match in sorted_matches:
                    self.stdout.write(self.style.SUCCESS(f"Дата: {match.timestamp}, {match.home_team.name} vs {match.away_team.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Нет данных для лиги {league_name}."))

        self.stdout.write(self.style.SUCCESS("Все матчи успешно обработаны!"))
