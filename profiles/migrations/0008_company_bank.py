# Generated by Django 3.0.8 on 2021-02-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210216_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
