import json
from django.db.models.base import ModelBase
from kowloon import models as database_models
from django.contrib.gis.db.models import fields
from django.contrib.gis.db.models.manager import GeoManager

GEOM_FIELDS = [
    fields.GeometryField,
    fields.PointField,
    fields.LineStringField,
    fields.PolygonField,
    fields.MultiPointField,
    fields.MultiLineStringField,
    fields.MultiPolygonField,
    fields.GeometryCollectionField,
]

def _get_name(self):
    return self._meta.db_table

def _get_model_name(self):
    return self._meta.object_name

def _get_properties(self):
    properties = []
    for field in self._meta.fields:
        if type(field) not in GEOM_FIELDS:
            properties.append((field.name, unicode(getattr(self, field.name))))
    return json.dumps(properties)

def monkey_patch_models():
    models = {} 
    for model in [getattr(database_models, x) for x in dir(database_models)]:
        if type(model) == ModelBase and type(model.objects) == GeoManager:
            model.__str__ = _get_name
            model.get_model_name = _get_model_name
            model.get_properties = _get_properties
            models[model.__name__] = model
    return models
