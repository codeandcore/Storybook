# Generated by Django 4.2.6 on 2023-10-09 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('swapImg', '0006_delete_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='userAnimeAvatar',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
