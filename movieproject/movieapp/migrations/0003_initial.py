# Generated by Django 4.1.5 on 2023-01-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movieapp', '0002_delete_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('decs', models.TextField()),
            ],
        ),
    ]
