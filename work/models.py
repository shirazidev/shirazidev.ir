from django.db import models

class Work(models.Model):
    id = models.IntegerField(primary_key=True)
    tarikh = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)