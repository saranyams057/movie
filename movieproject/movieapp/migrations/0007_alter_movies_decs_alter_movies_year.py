# Generated by Django 4.1.5 on 2023-02-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_alter_movies_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='decs',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='movies',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
