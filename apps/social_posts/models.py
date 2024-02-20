from django.db import models


class Social_Posts(models.Model):
    image = models.ImageField(
        upload_to="social_posts_image", 
        verbose_name="Картинка"
    )
    title = models.CharField(
        max_length=250, 
        verbose_name="Название"
    )
    created_at = models.DateField(
        auto_created=True, 
        verbose_name='Категория',
    )


class Meta(models.Model):
    verbose_name = 'Социальный пост'
    verbose_name_plural = 'Социальные посты'

def __str__(self):
    return self.title