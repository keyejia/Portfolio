# Generated by Django 2.0.2 on 2018-06-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='SourceURL',
            field=models.URLField(max_length=400),
        ),
    ]
