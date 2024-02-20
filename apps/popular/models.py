from django.db import models


class Popular(models.Model):
    category = models.CharField(
        max_length=250,
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to="news_image", 
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
    comment = models.TextField(
        max_length=500, 
        verbose_name="Комментарий"
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Активный"
    )


    class Meta:
        verbose_name = "Популярное"
        verbose_name_plural = "Популярные"


    def __str__(self):
        return self.name