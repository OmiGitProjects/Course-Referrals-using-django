# Generated by Django 3.0.8 on 2021-02-16 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20210216_1616'),
        ('profiles', '0009_auto_20210216_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrel_key',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
