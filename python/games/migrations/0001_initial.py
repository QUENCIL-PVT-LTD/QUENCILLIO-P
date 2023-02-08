# Generated by Django 4.1.5 on 2023-01-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(blank=True, db_column='gm_id', max_length=5, null=True)),
                ('b', models.CharField(blank=True, db_column='game_name', max_length=43, null=True)),
                ('c', models.CharField(blank=True, db_column='game_category', max_length=45, null=True)),
                ('d', models.CharField(blank=True, db_column='released_date', max_length=13, null=True)),
                ('e', models.CharField(blank=True, db_column='additional_date', max_length=15, null=True)),
                ('f', models.CharField(blank=True, db_column='link', max_length=50)),
            ],
            options={
                'db_table': 'game_date',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='gamesdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Genre', models.CharField(max_length=100)),
                ('Release_Date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=100)),
                ('yt', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'quengame',
            },
        ),
    ]
