import json
from django.db.models.base import ModelBase
from kowloon import models as database_models
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.contrib.gis.db.models.manager import GeoManager
from django.contrib.gis.db.models import fields

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
    properties = {}
    for field in self._meta.fields:
        if type(field) not in GEOM_FIELDS:
            properties[field.name] = getattr(self, field.name)
    return json.dumps(properties)

KOWLOON_MODELS = {}
def monkey_patch_models():
    for model in [getattr(database_models, x) for x in dir(database_models)]:
        if type(model) == ModelBase and type(model.objects) == GeoManager:
            model.__str__ = _get_name
            model.get_model_name = _get_model_name
            model.get_properties = _get_properties
            KOWLOON_MODELS[str(model)] = model
monkey_patch_models()

def index(request):
    return render_to_response("kowloon/index.html", {
            'database_tables': sorted(KOWLOON_MODELS.values())
        })


def viewer(request, table):
    model = getattr(database_models, table)

    # You can pass in filters using GET like in the django admin. 
    # so /?name=Compton on the neighborhoods table would give you just Compton.
    filters = request.GET.dict()
    qs = model.objects.all().filter(**filters).geojson()

    geojson = render_to_string("kowloon/geojson.json", {'object_list': qs})

    return render_to_response("kowloon/viewer.html", {
            'geojson': geojson,
            'extent': qs.extent()
        })

