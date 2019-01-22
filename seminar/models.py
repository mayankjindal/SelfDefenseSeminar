from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField()
    preferred_location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
