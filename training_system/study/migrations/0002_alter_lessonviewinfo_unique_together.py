# Generated by Django 4.2.5 on 2023-09-30 19:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lessonviewinfo',
            unique_together={('lesson', 'user')},
        ),
    ]
