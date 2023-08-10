from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    number = models.CharField(max_length=13, unique=True)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employee"
        ordering = ["firstname", "lastname"]

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
