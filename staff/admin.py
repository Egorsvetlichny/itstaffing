from django.contrib import admin

from staff.models import Company, Vacancy, JobApplicant, ResponseToVacancy, ApplicantInfo, VacancyStatistic


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'email', 'website_url', 'industry', 'location', 'logo_of_company',
                    'logo_of_company_small',)
    list_display_links = ('id', 'name',)
    list_per_page = 6


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'speciality', 'description', 'company', 'location', 'salary',
                    'publish_date', 'benefits', 'skills', 'type_of_employment', 'url_for_vacancy', 'contact_email',
                    'contact_phone', 'logo_of_vacancy', 'logo_of_vacancy_small',)
    list_display_links = ('id', 'title',)
    list_per_page = 6


@admin.register(JobApplicant)
class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'slug', 'applicant_info', 'is_admin', 'date_join', 'resume_url',
                    'profile_picture', 'github_profile', 'skills', 'desired_position', 'desired_salary',
                    'desired_location',)
    list_display_links = ('id', 'username', 'slug',)
    list_per_page = 6


@admin.register(ResponseToVacancy)
class ResponseToVacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_applicant', 'vacancy', 'status', 'cover_letter', 'send_date', 'response_date',)
    list_display_links = ('id', 'job_applicant', 'vacancy',)
    list_per_page = 6


@admin.register(ApplicantInfo)
class ApplicantInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'birthday', 'location', 'about')
    list_display_links = ('id', 'first_name', 'last_name',)
    list_per_page = 6


@admin.register(VacancyStatistic)
class VacancyStatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'vacancy_views', 'number_of_resp', 'number_of_invited',)
    list_display_links = ('id', 'title',)
    list_per_page = 6


# Заголовки главной страницы админ панели
admin.site.site_header = 'Панель администрирования IT Staffing'
admin.site.index_title = 'Приложения и таблицы БД'
