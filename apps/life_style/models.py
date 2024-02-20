from django.db import models

class Life_Style(models.Model):
    category = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to="popular_image_image", 
        verbose_name="Картинка"
    )
    title = models.CharField(
        max_length=250, 
        verbose_name="Название"
    )
    created_at = models.DateField(
        auto_created=True, 
        verbose_name="Дата создания"
    )

class Meta(models.Model):
    verbose_name = 'Популярный пост'
    verbose_name_plural = 'Популярные посты'

def __str__(self):
    return self.title