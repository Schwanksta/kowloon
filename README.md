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

Then, once you've configured the settings:

```bash
$ python kowloon.py -d database_name
```

You can also inspect your models in a Django shell using:

```bash
$ python kowloon.py shell -d database_name
```
