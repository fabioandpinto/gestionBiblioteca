# Generated by Django 3.0.6 on 2020-05-25 17:43

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20200525_1126'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
