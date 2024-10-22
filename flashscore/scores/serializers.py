from rest_framework import serializers
from .models import Sport, League, Team, Player, Coach

# Сериализатор для модели Sport
class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name', 'icon']

# Сериализатор для модели League
class LeagueSerializer(serializers.ModelSerializer):
    sport = serializers.PrimaryKeyRelatedField(queryset=Sport.objects.all())

    class Meta:
        model = League
        fields = ['id', 'name', 'icon', 'sport']

# Сериализатор для модели Team
class TeamSerializer(serializers.ModelSerializer):
    leagues = serializers.PrimaryKeyRelatedField(queryset=League.objects.all(), many=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'icon', 'leagues', 'points_l', 'points_c']

# Сериализатор для модели Player
class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Player
        fields = ['id', 'firstname', 'lastname', 'num_of_player', 'position', 'date_of_birth', 'team']

# Сериализатор для модели Coach
class CoachSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Coach
        fields = ['id', 'firstname', 'lastname', 'date_of_birth', 'team', 'exp']
