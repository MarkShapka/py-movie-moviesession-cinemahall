# Generated by Django 4.0.2 on 2023-08-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_cinemahall_movie_moviesession'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemahall',
            name='rows',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cinemahall',
            name='seats_in_row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]