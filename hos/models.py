from django.db import models

from django.contrib.auth.models import AbstractUser

#creating a model User:
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False, verbose_name='Доктор')

#creating a model Diagnose:
class Diagnose(models.Model):
    name_of_diagnoses = models.CharField(max_length=127, verbose_name= 'Диагноз')

#returning a string:
    def __str__(self):
        return self.name_of_diagnoses

#creating a model Patient:
class Patient(models.Model):
    name = models.CharField(max_length=123,verbose_name='Имя')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    diagnoses = models.ManyToManyField(Diagnose)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')

#returning a string:
    def __str__(self):
        return f'{self.date_of_birth}, {self.diagnoses}, {self.created_at}'



