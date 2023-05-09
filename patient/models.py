
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Patient(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):
        return f"{self.fname} {self.lname} and my age is {self.age}"
