from django.db import models

# Create your models here.
class React(models.Model):
    employees = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employees} - {self.department}"