from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Компания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Почтовый ящик')
    website_url = models.URLField(max_length=255, unique=True, blank=True, verbose_name='Веб-сайт')
    industry = models.CharField(max_length=255, blank=True, verbose_name='Сфера')
    location = models.CharField(max_length=255, blank=True, verbose_name='Расположение')
    logo_of_company = models.ImageField(upload_to='logos', blank=True, unique=True, verbose_name='Лого')
    logo_of_company_small = models.ImageField(upload_to='logos', blank=True, unique=True, verbose_name='Миниатюра лого')
    about = models.TextField(blank=True, verbose_name='О компании')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self): return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'slug': self.slug})
