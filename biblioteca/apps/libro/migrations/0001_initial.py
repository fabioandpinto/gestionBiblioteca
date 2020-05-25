# Generated by Django 3.0.6 on 2020-05-25 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='nombre-categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('date', models.DateField()),
                ('portrait', models.ImageField(upload_to='portraits/')),
                ('visits', models.PositiveIntegerField()),
                ('authors', models.ManyToManyField(to='autor.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Category')),
            ],
        ),
    ]