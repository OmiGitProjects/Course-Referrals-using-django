# Generated by Django 3.0.8 on 2021-02-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210215_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='referral_code',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
