# Generated by Django 3.0 on 2024-05-20 14:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_auto_20240518_1513"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profile",
            options={"verbose_name_plural": "Profiles"},
        ),
    ]
