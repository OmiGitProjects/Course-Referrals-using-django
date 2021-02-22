# Generated by Django 3.0.8 on 2021-02-16 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0009_course_purchased'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='purchased',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]