from django.contrib import admin

from staff.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'email', 'website_url', 'industry', 'location', 'logo_of_company',
                    'logo_of_company_small',)
    list_display_links = ('id', 'name')
    list_per_page = 6
