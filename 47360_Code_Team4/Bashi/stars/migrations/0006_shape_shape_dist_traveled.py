# Generated by Django 2.0.7 on 2018-08-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0005_auto_20180815_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='shape_dist_traveled',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
