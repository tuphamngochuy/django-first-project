# Generated by Django 5.2 on 2025-04-04 17:27

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE SCHEMA IF NOT EXISTS authentication;
            """
        ),
    ]
