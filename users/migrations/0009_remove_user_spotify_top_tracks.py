# Generated by Django 5.1.1 on 2024-11-06 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_user_spotify_top_tracks"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="spotify_top_tracks",),
    ]
