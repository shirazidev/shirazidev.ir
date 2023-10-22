from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=25)
    text = models.TextField()
    وضعیت_پاسخگویی = models.BooleanField(default=False)

    def __str__(self):
        status_message = lambda: "رسیدگی شده" if self.وضعیت_پاسخگویی else "رسیدگی نشده"
        return f"{self.name} - {self.email} - {status_message()}"
