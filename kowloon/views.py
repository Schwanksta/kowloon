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

