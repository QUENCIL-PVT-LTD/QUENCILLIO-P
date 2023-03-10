# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    p1 = models.CharField(max_length=100)
    p2 = models.CharField(max_length=100)
    secques = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'account_user'


class AdminHoneypotLoginattempt(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=39, blank=True, null=True)
    session_key = models.CharField(max_length=50, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    path = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_honeypot_loginattempt'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GameDate(models.Model):
    gm_id = models.CharField(max_length=5, blank=True, null=True)
    game_name = models.CharField(max_length=43, blank=True, null=True)
    game_category = models.CharField(max_length=45, blank=True, null=True)
    released_date = models.CharField(max_length=13, blank=True, null=True)
    additional_date = models.CharField(max_length=15, blank=True, null=True)
    link = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'game_date'


class GamesListing(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(db_column='Genre', max_length=100)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_Date', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    yt = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'games_listing'


class Quengame(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    genre = models.CharField(db_column='Genre', max_length=100)  # Field name made lowercase.
    release_date = models.DateField(db_column='Release_Date')  # Field name made lowercase.
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
    yt = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quengame'
