# Generated by Django 5.0.3 on 2024-03-19 22:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_userconfig_is_enable_alter_userconfig_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='userconfig',
            name='file_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
