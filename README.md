Kowloon
=======

Setup and installation
----------------------

This is just a little experiment in creating a PostGIS viewer using Django + Leaflet. I mean, why not?

You install the project as you would any Django project, though you don't need
to add a database, you WILL need to configure your username and password in
the settings (settings_dev.py and settings_prod.py, depending on what you're doing)

```bash
# Create a virtualenv
$ virtualenv kowloon
# Go in and download the repo to 'project'
$ cd kowloon && git clone git@github.com:Schwanksta/kowloon.git project
# Activate our virtualenv
$ . bin/activate
$ cd project
# Install the required python libraries
$ pip install -r requirements.txt
```

Then, once you've configured the settings, you fire up a server

```bash
$ python kowloon.py -d database_name
```

Point your browser to http://127.0.0.1:8000 and inspect your database layers.

You can also inspect your models in a Django shell using:

```bash
$ python kowloon.py shell -d database_name
```

What can it do?
---------------

Right now functionality is limited to basic operations -- Adding a PostGIS layer
to a map, inspecting the properties/database columns for a feature, and calculating a new
column based on a spatial join to another layer.

