# Generated by Django 3.0.8 on 2021-02-16 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0010_referrel_key_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='recommanded_to',
            field=models.ManyToManyField(blank=True, related_name='recommand_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
