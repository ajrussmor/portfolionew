# Generated by Django 3.2.6 on 2021-08-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desciption',
            new_name='description',
        ),
    ]
