# Generated by Django 5.0.3 on 2024-03-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_student_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('active', 'активный'), ('archived', 'архив')], max_length=20, verbose_name='Статус'),
        ),
    ]
