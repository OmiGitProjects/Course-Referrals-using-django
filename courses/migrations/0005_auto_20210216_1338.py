# Generated by Django 3.0.8 on 2021-02-16 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_company_bank'),
        ('courses', '0004_auto_20210216_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
