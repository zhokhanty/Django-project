import requests
from django.conf import settings

def fetch_sports_data():
    url = f"{settings.THE_SPORTS_DB_API_URL}all_sports.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("sports", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sports data: {e}")
        return []

def fetch_leagues_by_sport(sport_name):
    url = f"{settings.THE_SPORTS_DB_API_URL}all_leagues.php"
    try:
        response = requests.get(url)
        response.raise_for_status()
        leagues = response.json().get("leagues", [])
        filtered_leagues = [league for league in leagues if league.get('strSport') == sport_name]
        return filtered_leagues
    except requests.exceptions.RequestException as e:
        print(f"Error fetching leagues data: {e}")
        return []

def fetch_teams_by_league(league_name):
    url = f"{settings.THE_SPORTS_DB_API_URL}lookup_all_teams.php?id={league_name}"
    print(f"Fetching teams for league: {league_name}, URL: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        teams = response.json().get("teams", [])
        print(f"Teams fetched: {teams}")
        return response.json().get("teams", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching teams data: {e}")
        return []