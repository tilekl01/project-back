from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=250, 
        verbose_name="Название"
    )

class Meta:
    verbose_name = 'Категория'
    verbose_name = 'Категории'

def __str__(self):
    return self.title