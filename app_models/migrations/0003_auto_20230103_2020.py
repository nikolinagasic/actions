# Generated by Django 3.2.16 on 2023-01-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0002_milestone_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='forkers',
            field=models.ManyToManyField(related_name='fork_user', to='app_models.User'),
        ),
        migrations.AddField(
            model_name='repository',
            name='star_givers',
            field=models.ManyToManyField(related_name='star_user', to='app_models.User'),
        ),
    ]
