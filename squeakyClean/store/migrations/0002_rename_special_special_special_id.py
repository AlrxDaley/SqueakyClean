# Generated by Django 4.0.2 on 2022-07-04 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='special',
            old_name='special',
            new_name='special_id',
        ),
    ]