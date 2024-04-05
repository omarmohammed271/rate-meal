# Generated by Django 5.0.3 on 2024-04-05 12:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'meal')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'meal')},
        ),
    ]
