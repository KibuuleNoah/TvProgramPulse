# Generated by Django 5.0.6 on 2024-06-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="tel",
            field=models.IntegerField(
                null=True, unique=True, verbose_name="phone number"
            ),
        ),
    ]
