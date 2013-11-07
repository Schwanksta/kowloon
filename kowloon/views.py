from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from kowloon.modelutils import monkey_patch_models

KOWLOON_MODELS = monkey_patch_models()

def index(request):
    return render_to_response("kowloon/index.html", {
            'database_tables': sorted(KOWLOON_MODELS.values())
        })

def viewer(request, table):
    model = KOWLOON_MODELS.get(table)

    # You can pass in filters using GET like in the django admin. 
    # so /?name=Compton on the neighborhoods table would give you just Compton.
    filters = request.GET.dict()
    qs = model.objects.all().filter(**filters).geojson()

    geojson = render_to_string("kowloon/geojson.json", {'object_list': qs})

    return render_to_response("kowloon/viewer.html", {
            'geojson': geojson,
            'extent': qs.extent()
        })

