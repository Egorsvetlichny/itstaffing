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
    username = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    applicant_info = models.OneToOneField('ApplicantInfo', on_delete=models.CASCADE, verbose_name='Соискатель')
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    date_join = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата регистрации')
    resume_url = models.URLField(max_length=255, blank=True, unique=True, verbose_name='Резюме')
    profile_picture = models.ImageField(upload_to='profiles', blank=True, verbose_name='Фото профиля')
    github_profile = models.URLField(max_length=255, blank=True, unique=True, verbose_name='GitHub аккаунт')
    skills = models.JSONField(blank=True, verbose_name='Навыки')
    desired_position = models.CharField(max_length=255, blank=True, verbose_name='Желаемая позиция')
    desired_salary = models.IntegerField(blank=True, verbose_name='Желаемая ЗП')
    desired_location = models.CharField(max_length=255, blank=True, verbose_name='Желаемая локация')

    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self): return self.username

    def get_absolute_url(self):
        return reverse('applicant', kwargs={'slug': self.slug})


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


class ApplicantInfo(models.Model):
    first_name = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, db_index=True, verbose_name='Фамилия')
    email = models.EmailField(max_length=255, db_index=True, unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    telegram = models.CharField(max_length=255, blank=True, verbose_name='Telegram')
    whatsapp = models.CharField(max_length=255, blank=True, verbose_name='WhatsApp')
    birthday = models.DateField(verbose_name='Дата рождения')
    location = models.CharField(max_length=255, blank=True, verbose_name='Расположение')
    about = models.TextField(blank=True, verbose_name='О себе')

    class Meta:
        verbose_name = 'Информация о соискателе'
        verbose_name_plural = 'Информация о соискателях'

    # def __str__(self): return self.username
