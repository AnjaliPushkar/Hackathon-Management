# Generated by Django 3.0 on 2020-05-31 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo', '0005_remove_teamdetail_contact1'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeammemberDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname1', models.CharField(max_length=255)),
                ('lastname1', models.CharField(max_length=255)),
                ('gender1', models.CharField(max_length=40)),
                ('email1', models.CharField(max_length=255)),
                ('contact1', models.IntegerField()),
                ('college1', models.CharField(max_length=300)),
                ('yearofstudy1', models.CharField(max_length=10)),
                ('branch1', models.CharField(max_length=40)),
                ('github1', models.URLField(default='', max_length=250)),
                ('linkedin1', models.URLField(default='', max_length=250)),
                ('firstname2', models.CharField(max_length=255)),
                ('lastname2', models.CharField(max_length=255)),
                ('gender2', models.CharField(max_length=40)),
                ('email2', models.CharField(max_length=255)),
                ('contact2', models.IntegerField()),
                ('college2', models.CharField(max_length=300)),
                ('yearofstudy2', models.CharField(max_length=10)),
                ('branch2', models.CharField(max_length=40)),
                ('github2', models.URLField(default='', max_length=250)),
                ('linkedin2', models.URLField(default='', max_length=250)),
                ('firstname3', models.CharField(max_length=255)),
                ('lastname3', models.CharField(max_length=255)),
                ('gender3', models.CharField(max_length=40)),
                ('email3', models.CharField(max_length=255)),
                ('contact3', models.IntegerField()),
                ('college3', models.CharField(max_length=300)),
                ('yearofstudy3', models.CharField(max_length=10)),
                ('branch3', models.CharField(max_length=40)),
                ('github3', models.URLField(default='', max_length=250)),
                ('linkedin3', models.URLField(default='', max_length=250)),
                ('firstname4', models.CharField(max_length=255)),
                ('lastname4', models.CharField(max_length=255)),
                ('gender4', models.CharField(max_length=40)),
                ('email4', models.CharField(max_length=255)),
                ('contact4', models.IntegerField()),
                ('college4', models.CharField(max_length=300)),
                ('yearofstudy4', models.CharField(max_length=10)),
                ('branch4', models.CharField(max_length=40)),
                ('github4', models.URLField(default='', max_length=250)),
                ('linkedin4', models.URLField(default='', max_length=250)),
                ('pub_date4', models.DateTimeField()),
                ('firstname5', models.CharField(max_length=255)),
                ('lastname5', models.CharField(max_length=255)),
                ('gender5', models.CharField(max_length=40)),
                ('email5', models.CharField(max_length=255)),
                ('contact5', models.IntegerField()),
                ('college5', models.CharField(max_length=300)),
                ('yearofstudy5', models.CharField(max_length=10)),
                ('branch5', models.CharField(max_length=40)),
                ('github5', models.URLField(default='', max_length=250)),
                ('linkedin5', models.URLField(default='', max_length=250)),
                ('pub_date5', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='TeamDetail',
        ),
    ]