# Generated by Django 5.0.2 on 2024-02-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, verbose_name='Дата создания')),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('image', models.ImageField(upload_to='news_images', verbose_name='Картинка')),
                ('by_name', models.CharField(max_length=150, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
