from django.db import models

# Create your models here.
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    teacher = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name