# Generated by Django 3.0.8 on 2021-02-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_company_bank'),
        ('courses', '0008_remove_course_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='purchased',
            field=models.ManyToManyField(blank=True, to='profiles.Profile'),
        ),
    ]
