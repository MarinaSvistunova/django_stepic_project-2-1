# Generated by Django 3.0.5 on 2020-04-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_auto_20200417_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(default='frontend', max_length=30),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(default='Фронтенд', max_length=100),
        ),
    ]
