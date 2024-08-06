# Generated by Django 5.0.6 on 2024-07-28 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=20)),
                ('counter', models.IntegerField()),
            ],
        ),
    ]