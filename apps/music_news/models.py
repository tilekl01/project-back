from django.db import models

class Music_News(models.Model):
    category = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to="music_style_image", 
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
    text = models.TextField(
        max_length=500, 
        verbose_name="Текст"
    )
    comment = models.TextField(
        max_length=500, 
        verbose_name="Комментарий"
    )

    class Meta:
        verbose_name = 'Музыкальная новость'
        verbose_name_plural = 'Музыкальные новости'
    
    def __str__(self):
        return self.title