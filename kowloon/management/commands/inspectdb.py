###
# This is an overridden inspectdb, because Django enforces max_length on 
# CharFields, and PostgreSQL does not. Because of this, if you load shapefile
# data into PG it might not contain a max_length. When Django introspects
# the database when you initially run the kowloon command, the lack of 
# max_length will throw errors.
#
# To get around this, we just set blank max_lengths to 500 and call it a day.
###

from django.contrib.gis.management.commands.inspectdb import Command as InspectDBCommand

class Command(InspectDBCommand):

    def get_field_type(self, connection, table_name, row):
        field_type, field_params, field_notes = super(Command, self).get_field_type(connection, table_name, row)
        if field_type == 'CharField' and not field_params.get('max_length', None):
            field_params['max_length'] = 500
        return field_type, field_params, field_notes
