# Generated by Django 3.2.5 on 2021-07-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisyphusapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeboardConstructionCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=200)),
                ('floodzone', models.CharField(max_length=100)),
                ('parish', models.CharField(max_length=100)),
                ('no_floors', models.CharField(max_length=10)),
            ],
        ),
    ]
