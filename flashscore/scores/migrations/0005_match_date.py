# Generated by Django 5.1.3 on 2024-12-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
