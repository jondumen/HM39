# Generated by Django 5.0.4 on 2024-04-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hm_app', '0003_remove_producer_soundcloud_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='picture_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
