# Generated by Django 5.1.1 on 2024-11-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0015_spotifydata_artist_album_track"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spotifydata",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
