from django.db import models

class Mentee(models.Model):
    nama = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)
    quote = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama
