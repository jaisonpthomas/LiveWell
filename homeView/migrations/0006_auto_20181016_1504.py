# Generated by Django 2.1 on 2018-10-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeView', '0005_auto_20181016_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdata',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]