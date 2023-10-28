from django.db import models


class Visitor(models.Model):
    count = models.PositiveIntegerField(default=0)
