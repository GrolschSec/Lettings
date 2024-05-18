# Generated by Django 3.0 on 2024-05-18 15:13

from django.db import migrations
from typing import Any
from django.apps.registry import Apps
from oc_lettings_site.utils.data_migration_utils import copy_model_data


def copy_data(apps: Apps, schema_editor: Any):
    """
    Copies data from one old app to the current app

    Args:
        apps: The app registry.
        schema_editor: The schema editor.

    Returns:
        None
    """
    copy_model_data(
        apps,
        schema_editor,
        "oc_lettings_site",
        "Profile",
        "profiles",
        "Profile",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(copy_data),
    ]
