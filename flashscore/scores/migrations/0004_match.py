# Generated by Django 5.1.3 on 2024-12-10 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_remove_team_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_score', models.IntegerField(blank=True, null=True)),
                ('away_score', models.IntegerField(blank=True, null=True)),
                ('round_number', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='scores.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='scores.team')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.league')),
            ],
        ),
    ]