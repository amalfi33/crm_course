# Generated by Django 5.0.1 on 2024-02-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_employee_phone_number_remove_employee_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='core.course', verbose_name='Курс обучения'),
        ),
    ]