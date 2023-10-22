from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    # icon = models.ImageField(null=True, upload_to='uploads/')

    def __str__(self):
        return f"{self.name} - {self.desc[:30]}..."