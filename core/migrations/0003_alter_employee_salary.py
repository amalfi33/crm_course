# Generated by Django 5.0.1 on 2024-02-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_teacher_options_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(max_length=15, verbose_name='Зарплата'),
        ),
    ]
