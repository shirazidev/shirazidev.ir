from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    Phone = models.CharField(max_length=17, default=+980000000000)
    subject = models.CharField(max_length=30)
    text = models.TextField()
    وضعیت_پاسخگویی = models.BooleanField(default=False)

    def __str__(self):
        status_message = lambda: "رسیدگی شده" if self.وضعیت_پاسخگویی else "رسیدگی نشده"
        return f"{self.name} - {self.email} - {status_message()}"
