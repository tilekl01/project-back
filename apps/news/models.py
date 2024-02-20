from django.db import models

class News(models.Model):
    category = models.CharField(
        verbose_name='Категория',
        max_length=255,
    )
    title = models.CharField(
        max_length=250, 
        verbose_name="Название"
    )
    image = models.ImageField(
        upload_to="news_images", 
        verbose_name="Картинка"
    )
    by_name = models.CharField(
        max_length=150, 
        verbose_name="Имя"
    )
    created_at = models.DateField(
        auto_created=True, 
        verbose_name="Дата создания"
    )


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    def __str__(self):
        return self.title