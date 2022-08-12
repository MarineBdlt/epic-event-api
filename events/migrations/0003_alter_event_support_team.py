# Generated by Django 4.0.6 on 2022-08-11 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event_support_team_alter_event_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='support_team',
            field=models.ManyToManyField(limit_choices_to={'groups__name': 'support_team'}, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]