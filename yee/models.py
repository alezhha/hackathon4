from django.db import models

# Create your models here.

class Letter(models.Model):
    text = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    messages = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"


