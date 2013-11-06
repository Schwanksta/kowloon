import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings") 
from optparse import OptionParser
from django.conf import settings
from django.core.management import call_command

parser = OptionParser()
parser.add_option("-d", "--database", action="store", type="string", dest="database")
(options,args) = parser.parse_args()
# We pass the database name in on the command line.
settings.DATABASES['default']['NAME'] = options.database

output = open("kowloon/models.py", "w") # Every time we run, we overwrite
call_command("inspectdb",stdout=output) # the models file with Django's introspection
output.close()                          # this way we can run GeoDjango queries over 
                                        # arbitrary tables.
# Run the web server.
call_command("runserver")
