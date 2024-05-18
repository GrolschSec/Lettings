from django.apps.registry import Apps
from typing import Any
from django.db.models import ForeignKey


def copy_model_data(
    apps: Apps,
    schema_editor: Any,
    old_app_name: str,
    old_model_name: str,
    new_app_name: str,
    new_model_name: str,
) -> None:
    """
    Copy data from one model to another, it can be useful when moving a model to anothher app

    Args:
        apps: The Django Apps registry.
        schema_editor: The Django schema editor.
        old_app_name: The name of the old app containing the source model.
        old_model_name: The name of the old model to copy data from.
        new_app_name: The name of the new app containing the destination model.
        new_model_name: The name of the new model to copy data to.

    Returns:
        None

    """
    OldModel = apps.get_model(old_app_name, old_model_name)
    NewModel = apps.get_model(new_app_name, new_model_name)

    for old_obj in OldModel.objects.all():
        new_obj = NewModel()

        for field in old_obj._meta.fields:

            if isinstance(field, ForeignKey):
                RelatedModel = apps.get_model(field.related_model._meta.app_label, field.related_model.__name__)
                related_obj = RelatedModel.objects.get(pk=getattr(old_obj, field.name).pk)
                setattr(new_obj, field.name, related_obj)
    
            elif hasattr(new_obj, field.name):
                setattr(new_obj, field.name, getattr(old_obj, field.name))

        new_obj.save()