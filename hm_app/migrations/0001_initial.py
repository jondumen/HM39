# Generated by Django 5.0.4 on 2024-04-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('last_song', models.CharField(max_length=50)),
                ('popular_song', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=500)),
                ('twitter_username', models.CharField(blank=True, max_length=50, null=True)),
                ('youtube_channel_id', models.CharField(blank=True, max_length=50, null=True)),
                ('soundcloud_username', models.CharField(blank=True, max_length=50, null=True)),
                ('niconico_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
