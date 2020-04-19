# Generated by Django 3.0.5 on 2020-04-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_auto_20200416_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='grade',
            field=models.CharField(choices=[('intern', 'Стажер'), ('junior', 'Джуниор'), ('middle', 'Миддл'), ('senior', 'Синьор'), ('lead', 'Лид')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='status',
            field=models.CharField(choices=[('stop_search', 'Не ищу работу'), ('active', 'Рассматриваю предложения'), ('search', 'Ищу работу')], max_length=100, null=True),
        ),
    ]