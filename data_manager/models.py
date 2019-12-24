from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} {self.code}'

