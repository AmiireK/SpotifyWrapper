# Generated by Django 5.1.1 on 2024-11-22 03:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0018_alter_spotifydata_created_at"),
    ]

    operations = [
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
                ],
                max_length=20,
            ),
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=100)),
                ("count", models.IntegerField()),
                ("percentage", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "spotify_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.spotifydata",
                    ),
                ),
            ],
        ),
    ]
