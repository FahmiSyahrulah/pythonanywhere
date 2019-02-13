from django.db import models
from django.utils import timezone

class Blog(models.Model):
    judul = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)
    deskripsi = models.CharField(max_length = 255)
    tanggal = models.DateField(default=timezone.now)

    def __str__(self):
        return self.judul
