# Generated by Django 4.0.2 on 2022-07-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_special_special_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='special',
            name='special_id_1',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='special',
            name='special_id_2',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='special',
            name='special_id_3',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
