from rest_framework import serializers
from .models import Sport, League, Team, Player, Coach

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    sport = serializers.StringRelatedField()

    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    leagues = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()

    class Meta:
        model = Coach
        fields = '__all__'
