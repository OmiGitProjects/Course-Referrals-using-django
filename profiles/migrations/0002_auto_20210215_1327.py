# Generated by Django 3.0.8 on 2021-02-15 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlanA',
            new_name='Plan_A_Model',
        ),
        migrations.AlterField(
            model_name='plan_a_model',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.UserCounter'),
        ),
    ]
