# Generated by Django 3.2.9 on 2021-11-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(editable=False, max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]