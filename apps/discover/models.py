from django.db import models

class Discover(models.Model):
    image = models.ImageField(
        upload_to="discover_image", 
        verbose_name="Картинка"
    )
    title = models.CharField(
        max_length=250, 
        verbose_name="Название"
    )

class Meta(models.Model):
    verbose_name = 'dicover'
    verbose_name_plural = 'discovers'

def __str__(self):
    return self.title
