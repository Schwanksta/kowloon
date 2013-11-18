from django.shortcuts import render_to_response
from kowloon.modelutils import monkey_patch_models

KOWLOON_MODELS = monkey_patch_models()

def index(request):
    return render_to_response("kowloon/index.html", {
            'database_tables': sorted(KOWLOON_MODELS.values())
        })

def get_layer(request, table):
    model = KOWLOON_MODELS.get(table)

    # You can pass in filters using GET like in the django admin. 
    # so /?name=Compton on the neighborhoods table would give you just Compton.
    filters = request.GET.dict()
    qs = model.objects.all().filter(**filters).geojson()

    qs_extent = qs.extent()
    extent = [
        [qs_extent[1], qs_extent[0]],
        [qs_extent[3], qs_extent[2]],
    ]
     
    return render_to_response("kowloon/geojson.json", {'object_list': qs, 'extent': extent}, content_type="text/json")


def spatial_calc(request, poly_table, point_table, operation="count", field="*"):
    poly_model = KOWLOON_MODELS.get(poly_table)
    point_model = KOWLOON_MODELS.get(point_table)

    poly_table_name = poly_model._meta.db_table
    point_table_name = point_model._meta.db_table

    #this obviously won't always work.
    poly_field = poly_model.objects.all()[0].get_geom_fields()[0].name
    point_field = point_model.objects.all()[0].get_geom_fields()[0].name

    query = """
    SELECT %(operation)s(%(field)s) FROM %(point_table)s WHERE ST_Contains(%(poly_table)s.%(poly_field)s, %(point_table)s.%(point_field)s)
    """ % {
        'operation': operation,
        'field': field,
        'point_table': point_table_name,
        'poly_table': poly_table_name,
        'poly_field': poly_field,
        'point_field': point_field,
    }

    if field != '*':
        new_field = '%s_%s' % (field, operation)
    else:
        new_field = '%s_%s' % (point_table_name, operation)

    qs = poly_model.objects.extra(
        select = {
            new_field: query
        }
    ).geojson()

    qs_extent = qs.extent()
    extent = [
        [qs_extent[1], qs_extent[0]],
        [qs_extent[3], qs_extent[2]],
    ]
     
    return render_to_response("kowloon/geojson.json", {'object_list': qs, 'extent': extent}, content_type="text/json")

