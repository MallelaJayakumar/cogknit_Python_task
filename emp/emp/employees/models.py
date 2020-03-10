from django.db import models

class Employee(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    title = models.TextField()
    department = models.TextField()
    birthdate = models.TextField()