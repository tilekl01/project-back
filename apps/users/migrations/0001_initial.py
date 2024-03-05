# Generated by Django 5.0.2 on 2024-03-02 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=256, null=True)),
                ('gender', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=256, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('tiktok', models.URLField(blank=True, null=True)),
                ('apple_id', models.CharField(max_length=256)),
            ],
        ),
    ]
