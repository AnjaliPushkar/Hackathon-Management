# Generated by Django 3.0 on 2020-05-31 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo2', '0003_auto_20200601_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='statusid1',
            new_name='statusid',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='teamname1',
            new_name='teamname',
        ),
    ]
