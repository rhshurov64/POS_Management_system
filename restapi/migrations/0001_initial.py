# Generated by Django 4.2.8 on 2023-12-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('school', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
