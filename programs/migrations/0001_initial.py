# Generated by Django 5.0.6 on 2024-06-01 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Television",
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
                ("name", models.CharField(max_length=20, unique=True)),
                ("rating", models.FloatField(default=0.0)),
                ("region", models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Program",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("rating", models.FloatField(default=0.0)),
                ("time", models.TimeField()),
                ("days", models.TextField()),
                ("tags", models.TextField(null=True)),
                ("language", models.CharField(max_length=20, null=True)),
                (
                    "television",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="programs.television",
                    ),
                ),
            ],
        ),
    ]
