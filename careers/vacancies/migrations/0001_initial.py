# Generated by Django 3.0.5 on 2020-04-13 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('logo', models.URLField()),
                ('description', models.CharField(max_length=300)),
                ('employee_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('picture', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название вакансии')),
                ('skills', models.TextField()),
                ('description', models.CharField(max_length=300, verbose_name='описание вакансии')),
                ('salary_min', models.IntegerField(verbose_name='зарплата от')),
                ('salary_max', models.IntegerField(verbose_name='зарплата до')),
                ('publish_date', models.DateField(verbose_name='дата публикации')),
                ('company', models.ForeignKey(default=1581229120, on_delete=django.db.models.deletion.CASCADE, related_name='company_vacancies', to='vacancies.Company')),
                ('specialty', models.ForeignKey(default=1581229120, on_delete=django.db.models.deletion.CASCADE, related_name='speciality_vacancies', to='vacancies.Specialty')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
            },
        ),
    ]
