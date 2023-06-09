# Generated by Django 4.2.1 on 2023-06-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Book_name', models.CharField(max_length=40)),
                ('Author_name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Classics', 'classics'), ('crime', 'crime'), ('horror', 'horro'), ('fantasy', 'fantasy'), ('History', 'History')], max_length=20)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
