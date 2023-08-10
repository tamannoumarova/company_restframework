from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=125)
    number = models.CharField(max_length=13, unique=True)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name", "name"]

    def __str__(self):
        return f"{self.name} {self.number}"
