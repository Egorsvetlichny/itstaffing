from django.contrib import admin

from staff.models import Company, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'email', 'website_url', 'industry', 'location', 'logo_of_company',
                    'logo_of_company_small',)
    list_display_links = ('id', 'name')
    list_per_page = 6


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'speciality', 'description', 'company', 'location', 'salary',
                    'published_date', 'benefits', 'skills', 'type_of_employment', 'url_for_vacancy', 'contact_email',
                    'contact_phone', 'logo_of_vacancy', 'logo_of_vacancy_small',)
    list_display_links = ('id', 'title')
    list_per_page = 6


# Заголовки главной страницы админ панели
admin.site.site_header = 'Панель администрирования IT Staffing'
admin.site.index_title = 'Приложения и таблицы БД'
