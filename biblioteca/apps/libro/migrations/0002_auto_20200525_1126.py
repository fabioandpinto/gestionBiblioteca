# Generated by Django 3.0.6 on 2020-05-25 16:26

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_book', to='libro.Category'),
        ),
    ]
