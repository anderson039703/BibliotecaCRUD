# Generated by Django 3.2.8 on 2021-10-12 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=50)),
                ('editora', models.CharField(max_length=20)),
                ('idioma', models.CharField(max_length=15)),
            ],
        ),
    ]