# Generated by Django 2.0.2 on 2018-06-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0002_auto_20180628_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='Music Reccord Application', max_length=200),
            preserve_default=False,
        ),
    ]
