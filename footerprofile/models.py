from django.db import models


class Person(models.Model):
    name = models.CharField(default="null",max_length=350)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"{self.name}"
