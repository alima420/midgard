# Generated by Django 5.0.6 on 2024-07-30 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=20)),
                ('counter', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Machine3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('program', models.CharField(max_length=20)),
                ('counter', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Machine',
            new_name='Machine1',
        ),
    ]
