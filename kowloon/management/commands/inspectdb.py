###
# This is an overridden inspectdb, because Django enforces max_length on 
# CharFields and PostgreSQL does not. Because of this, if you load shapefile
# data into PG it might not contain a max_length. When Django introspects
# the database when you initially run the kowloon command, the lack of 
# max_length will throw errors.
#
# To get around this, we just set blank max_lengths to 500 and call it a day.
###

from django.contrib.gis.management.commands.inspectdb import Command as InspectDBCommand

class Command(InspectDBCommand):

    def handle_inspection(self, options):
        table_name = options.get('table_name', None)
        # If we supply a table name, we will send a filter function to the 
        # base inspectdb command that filters to just that table.
        if table_name:
            options['table_name_filter'] = lambda x:  x == table_name
        return super(InspectDBCommand, self).handle_inspection(options)

    def get_field_type(self, connection, table_name, row):
        """
        Runs all of the normal get_field_type hoo-ha for GeoDjango, but adds a
        max_length to CharFields that don't have one.
        """
        field_type, field_params, field_notes = super(Command, self).get_field_type(connection, table_name, row)
        if field_type == 'CharField' and not field_params.get('max_length', None):
            field_params['max_length'] = 500
        return field_type, field_params, field_notes
