from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

#I want to validate phone number as either 254 or 07

phone_regex_validate = RegexValidator(
    regex=r'^(2547|07)\d{8}$', # here with start string we "^" and end string we use "$" we are checking if 254 or 07 is present
    message="Phone number you input must be in the format: '2547XXXXXXXX' or '07XXXXXXXX'."
)
# model to save employee data into the database
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=255)
    phone_number = models.CharField(validators=[phone_regex_validate], max_length=15, unique=True)
    hire_date = models.DateField()
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"