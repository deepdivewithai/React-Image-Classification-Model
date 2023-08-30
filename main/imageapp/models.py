from django.db import models

class Image(models.Model):
    file = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return str(self.pk)