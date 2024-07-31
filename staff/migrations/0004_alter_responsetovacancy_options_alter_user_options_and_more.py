# Generated by Django 5.0.6 on 2024-07-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_user_responsetovacancy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsetovacancy',
            options={'verbose_name': 'Отклик', 'verbose_name_plural': 'Отклики'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='published_date',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='responsetovacancy',
            name='status',
            field=models.CharField(choices=[('Applied', 'На рассмотрении'), ('Interview', 'Собеседование'), ('Rejected', 'Отказ'), ('Offered', 'Оффер')], default='Applied', max_length=15, verbose_name='Статус отклика'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='type_of_employment',
            field=models.CharField(choices=[('Full_time', 'Полная занятость'), ('Part_time', 'Частичная занятость'), ('Contract', 'Контракт'), ('Internship', 'Стажировка')], default='Full_time', max_length=20, verbose_name='Вид трудоустройства'),
        ),
    ]
