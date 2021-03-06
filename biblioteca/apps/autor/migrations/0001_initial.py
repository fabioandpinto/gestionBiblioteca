# Generated by Django 3.0.6 on 2020-05-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='apellido')),
                ('country', models.CharField(max_length=30, verbose_name='pais')),
                ('age', models.PositiveIntegerField(verbose_name='edad')),
            ],
        ),
    ]
