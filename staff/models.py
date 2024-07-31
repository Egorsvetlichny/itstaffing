from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Компания')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    email = models.EmailField(max_length=255, db_index=True, unique=True, verbose_name='Почтовый ящик')
    phone = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Телефон')
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
    class TypeOfEmployment(models.TextChoices):
        FULL_TIME = 'Full_time', _('Полная занятость')
        PART_TIME = 'Part_time', _('Частичная занятость')
        CONTRACT = 'Contract', _('Контракт')
        INTERNSHIP = 'Internship', _('Стажировка')
        SHIFT_WORK = 'Shift_work', _('Вахтовый метод')

    title = models.CharField(max_length=255, db_index=True, verbose_name='Вакансия')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    speciality = models.CharField(max_length=255, verbose_name='Специальность')
    description = models.TextField(blank=True, verbose_name='Описание вакансии')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Компания')
    location = models.CharField(max_length=255, blank=True, verbose_name='Расположение')
    salary = models.IntegerField(blank=True, verbose_name='Зарплата')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    benefits = models.TextField(blank=True, verbose_name='Преимущества')
    skills = models.JSONField(blank=True, verbose_name='Требуемые навыки')
    type_of_employment = models.CharField(max_length=20, choices=TypeOfEmployment.choices,
                                          default=TypeOfEmployment.FULL_TIME, verbose_name='Вид трудоустройства')
    url_for_vacancy = models.URLField(max_length=255, blank=True, unique=True, verbose_name='Ссылка на вакансию')
    contact_email = models.EmailField(max_length=255, db_index=True, unique=True, verbose_name='Контактный email')
    contact_phone = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Контактный телефон')
    logo_of_vacancy = models.ImageField(upload_to='logos', blank=True, unique=True, verbose_name='Лого')
    logo_of_vacancy_small = models.ImageField(upload_to='logos', blank=True, unique=True, verbose_name='Миниатюра лого')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self): return self.title

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'slug': self.slug})


class JobApplicant(models.Model):
    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'


class ResponseToVacancy(models.Model):
    class Status(models.TextChoices):
        APPLIED = 'Applied', _('На рассмотрении')
        INTERVIEW = 'Interview', _('Собеседование')
        REJECTED = 'Rejected', _('Отказ')
        OFFERED = 'Offered', _('Оффер')

    job_applicant = models.ForeignKey(JobApplicant, on_delete=models.PROTECT, db_index=True, verbose_name='Соискатель')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.PROTECT, db_index=True, verbose_name='Вакансия')
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.APPLIED,
                              verbose_name='Статус отклика')
    cover_letter = models.TextField(blank=True, verbose_name='Сопроводительное письмо')
    send_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата отклика')
    response_date = models.DateTimeField(auto_now=True, verbose_name='Дата ответа на отклик')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self): return f'Соискатель - {self.job_applicant}, вакансия - {self.vacancy}'
