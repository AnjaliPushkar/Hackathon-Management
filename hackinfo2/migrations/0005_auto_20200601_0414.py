# Generated by Django 3.0 on 2020-05-31 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo2', '0004_auto_20200601_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='password',
            new_name='password11',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='username',
            new_name='user',
        ),
    ]
