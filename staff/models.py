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


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Вакансия')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    speciality = models.CharField(max_length=255, verbose_name='Специальность')
    description = models.TextField(verbose_name='Описание вакансии')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    location = models.CharField(max_length=255, verbose_name='Расположение')
    salary = models.IntegerField(verbose_name='Зарплата')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    benefits = models.TextField(blank=True, verbose_name='Преимущества')
    skills = models.JSONField(blank=True, verbose_name='Навыки')
    type_of_employment = models.CharField(max_length=255, blank=True, verbose_name='Тип работы')
    url_for_vacancy = models.URLField(max_length=255, blank=True, verbose_name='Ссылка на вакансию')
    contact_email = models.EmailField(max_length=255, blank=True, verbose_name='Контактный email')
    contact_phone = models.CharField(max_length=255, blank=True, verbose_name='Контактный телефон')
    logo_of_vacancy = models.ImageField(upload_to='logos', blank=True, verbose_name='Лого')
    logo_of_vacancy_small = models.ImageField(upload_to='logos', blank=True, verbose_name='Миниатюра лого')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self): return self.title

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'slug': self.slug})
