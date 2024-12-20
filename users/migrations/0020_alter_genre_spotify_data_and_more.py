# Generated by Django 5.1.1 on 2024-11-22 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0019_alter_spotifydata_wrapper_type_genre"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="spotify_data",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="genres",
                to="users.spotifydata",
            ),
        ),
        migrations.AlterField(
            model_name="spotifydata",
            name="wrapper_type",
            field=models.CharField(
                choices=[
                    ("RECENTLY_PLAYED", "Recently Played"),
                    ("TOP_TRACKS_SHORT", "Top Tracks Short Term"),
                    ("TOP_TRACKS_MEDIUM", "Top Tracks Medium Term"),
                    ("TOP_TRACKS_LONG", "Top Tracks Long Term"),
                    ("TOP_ARTISTS", "Top Artists"),
                    ("TOP_ALBUM", "Top Album"),
                    ("TOP_GENRES", "Top Genres"),
                    ("TOP_PLAYLISTS", "Top Playlists"),
                ],
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("playlist_id", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("image_url", models.URLField(blank=True, null=True)),
                ("total_duration_minutes", models.FloatField()),
                ("track_count", models.PositiveIntegerField()),
                (
                    "spotify_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlists",
                        to="users.spotifydata",
                    ),
                ),
            ],
        ),
    ]
