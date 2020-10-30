from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Employee'

    def __str__(self):
        return self.emp_name

