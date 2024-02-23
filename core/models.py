from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from PIL import Image , ImageDraw
from django.core.files import File


class Position(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность', unique = True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.position


# Модель работника 
class Employee(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.user.username
    
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ф.И.О')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Курс обучения')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Цена')
    date_start = models.DateField(verbose_name='Дата начала подписки')
    date_end = models.DateField(verbose_name='Дата конца подписки')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Учитель', related_name='courses')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Student(models.Model):
    class StudentStatus(models.IntegerChoices):
        active = 1 
        archived = 2
    name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    course = models.ManyToManyField(Course, related_name= 'students', verbose_name='Курс')
    status = models.IntegerField(choices=StudentStatus.choices, default=1, verbose_name='Статус')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    qr_code = models.ImageField(upload_to= 'students_qr/', blank=True)
    code = models.CharField(max_length=20, blank=True)


    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname =f'qr_code-{self.name}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs) 
        


class Group(models.Model):
    name = models.CharField(max_length=100 , verbose_name = 'Название группы')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name = 'Преподаватель')
    category = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name = 'Курс')
    students = models.ManyToManyField(Student , verbose_name= 'Ученики')

    class Meta:
        verbose_name = 'Группа'  
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = True)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null = True)
    is_income = models.BooleanField(default=True) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null = True)




