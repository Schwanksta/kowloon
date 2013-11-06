# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class CommentsHomicidecomment(models.Model):
    comment_ptr = models.ForeignKey('DjangoComments', primary_key=True)
    is_blocked = models.BooleanField()
    class Meta:
        db_table = 'comments_homicidecomment'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoCommentFlags(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    comment = models.ForeignKey('DjangoComments')
    flag = models.CharField(max_length=30)
    flag_date = models.DateTimeField()
    class Meta:
        db_table = 'django_comment_flags'

class DjangoComments(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey('DjangoContentType')
    object_pk = models.TextField()
    site = models.ForeignKey('DjangoSite')
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=75)
    user_url = models.CharField(max_length=200)
    comment = models.TextField()
    submit_date = models.DateTimeField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_public = models.BooleanField()
    is_removed = models.BooleanField()
    class Meta:
        db_table = 'django_comments'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256)
    f_table_schema = models.CharField(max_length=256)
    f_table_name = models.CharField(max_length=256)
    f_geometry_column = models.CharField(max_length=256)
    coord_dimension = models.IntegerField()
    srid = models.IntegerField()
    type = models.CharField(max_length=30)
    class Meta:
        db_table = 'geometry_columns'

class HomicideBlogpost(models.Model):
    id = models.IntegerField(primary_key=True)
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    lead_image = models.CharField(max_length=100, blank=True)
    robotext_hed = models.CharField(max_length=255, blank=True)
    robotext_body = models.TextField(blank=True)
    date_time = models.DateTimeField()
    last_update = models.DateTimeField()
    homicide = models.ForeignKey('HomicideHomicide', unique=True, null=True, blank=True)
    byline = models.CharField(max_length=255)
    class Meta:
        db_table = 'homicide_blogpost'

class HomicideBlogpostRelatedHomicides(models.Model):
    id = models.IntegerField(primary_key=True)
    blogpost = models.ForeignKey(HomicideBlogpost)
    homicide = models.ForeignKey('HomicideHomicide')
    class Meta:
        db_table = 'homicide_blogpost_related_homicides'

class HomicideHomicide(models.Model):
    id = models.IntegerField(primary_key=True)
    coroners_case_number = models.CharField(max_length=20, blank=True)
    police_case_number = models.CharField(max_length=20, blank=True)
    da_case_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    cause = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    race = models.CharField(max_length=10, blank=True)
    day_of_week = models.CharField(max_length=10)
    neighborhoodv5 = models.ForeignKey('HomicideNeighborhoodv5', null=True, blank=True)
    neighborhoodv6 = models.ForeignKey('HomicideNeighborhoodv6', null=True, blank=True)
    jurisdiction = models.ForeignKey('HomicideJurisdiction', null=True, blank=True)
    coroners_description = models.TextField(blank=True)
    death_date = models.DateField()
    death_time = models.TimeField(null=True, blank=True)
    died_on_scene = models.BooleanField()
    incident_address = models.CharField(max_length=400, blank=True)
    incident_zipcode = models.IntegerField(null=True, blank=True)
    blog_item_url = models.CharField(max_length=500, blank=True)
    image = models.CharField(max_length=100, blank=True)
    officer_involved = models.BooleanField()
    domestic_violence = models.BooleanField()
    ruling = models.CharField(max_length=1, blank=True)
    incident_point_4326 = models.PointField(null=True, blank=True)
    incident_point_900913 = models.PointField(srid=900913, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    formatted_death_date = models.CharField(max_length=100)
    canonical_url = models.CharField(max_length=255)
    objects = models.GeoManager()
    class Meta:
        db_table = 'homicide_homicide'

class HomicideHomicideLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    homicide = models.ForeignKey(HomicideHomicide)
    link = models.ForeignKey('HomicideLink')
    class Meta:
        db_table = 'homicide_homicide_links'

class HomicideJurisdiction(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    class Meta:
        db_table = 'homicide_jurisdiction'

class HomicideLink(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'homicide_link'

class HomicideNeighborhoodv5(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    population = models.FloatField(null=True, blank=True)
    population_source = models.CharField(max_length=50)
    population_source_explainer = models.TextField()
    square_miles = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=50)
    polygon_4326 = models.MultiPolygonField(null=True, blank=True)
    simple_polygon_4326 = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'homicide_neighborhoodv5'

class HomicideNeighborhoodv6(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    has_statistics = models.BooleanField()
    population = models.FloatField(null=True, blank=True)
    population_source = models.CharField(max_length=50)
    population_source_explainer = models.TextField()
    white_percent = models.FloatField(null=True, blank=True)
    white_count = models.FloatField(null=True, blank=True)
    black_percent = models.FloatField(null=True, blank=True)
    black_count = models.FloatField(null=True, blank=True)
    other_percent = models.FloatField(null=True, blank=True)
    other_count = models.FloatField(null=True, blank=True)
    asian_percent = models.FloatField(null=True, blank=True)
    asian_count = models.FloatField(null=True, blank=True)
    latino_percent = models.FloatField(null=True, blank=True)
    latino_count = models.FloatField(null=True, blank=True)
    nonwhite_percent = models.FloatField(null=True, blank=True)
    nonwhite_count = models.FloatField(null=True, blank=True)
    diversityindex = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=300)
    county = models.CharField(max_length=300)
    square_miles = models.FloatField(null=True, blank=True)
    polygon_4326 = models.MultiPolygonField(null=True, blank=True)
    simple_polygon_4326 = models.MultiPolygonField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'homicide_neighborhoodv6'

class HomicidePointofinterest(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500, blank=True)
    post = models.ForeignKey(HomicideBlogpost)
    point_4326 = models.PointField()
    point_900913 = models.PointField(srid=900913, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'homicide_pointofinterest'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = 'spatial_ref_sys'

