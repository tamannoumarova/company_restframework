from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=125)
    number = models.CharField(max_length=13, unique=True)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
        ordering = ["name", "name"]

    def __str__(self):
        return f"{self.name} {self.number}"
