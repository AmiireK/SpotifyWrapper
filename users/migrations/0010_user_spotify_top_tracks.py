# Generated by Django 5.1.1 on 2024-11-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_remove_user_spotify_top_tracks"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="spotify_top_tracks",
            field=models.JSONField(blank=True, null=True),
        ),
    ]