# Generated by Django 4.1.5 on 2023-02-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_alter_movies_decs_alter_movies_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='decs',
            field=models.TextField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
