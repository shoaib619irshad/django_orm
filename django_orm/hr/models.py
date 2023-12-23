from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.phone
    

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True , blank=True)

    def __str__(self):
        return self.name


class Compensation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    compensations = models.ManyToManyField(Compensation)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'