from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=25)
    desc = models.TextField(max_length=35)
    image = models.ImageField(upload_to="project", null=True, default='null')

    def __str__(self):
        return self.title


class Navbar(models.Model):
    title = models.CharField(max_length=50)
    nav = models.IntegerField(default=0)
