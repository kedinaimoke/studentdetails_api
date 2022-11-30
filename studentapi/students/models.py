from django.db import models


# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    matric_number = models.CharField(max_length=7)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name}: {self.matric_number}'
