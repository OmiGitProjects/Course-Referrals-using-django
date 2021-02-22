# Generated by Django 3.0.8 on 2021-02-16 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0008_company_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referrel_key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_key', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='referrel_keys',
            field=models.ManyToManyField(blank=True, to='profiles.Referrel_key'),
        ),
    ]
