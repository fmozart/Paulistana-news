# Generated by Django 5.0.7 on 2024-08-23 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0010_profile_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]