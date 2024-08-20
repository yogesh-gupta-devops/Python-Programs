# Generated by Django 4.2.13 on 2024-07-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BngJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligiblity', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HydJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligiblity', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PuneJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligiblity', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
