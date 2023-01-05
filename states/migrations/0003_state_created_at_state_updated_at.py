# Generated by Django 4.1.4 on 2023-01-05 04:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_auto_20230104_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
