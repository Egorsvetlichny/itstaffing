from django.conf import settings


def admin_context_processor(request):
    return {
        'admin_browser_title': 'Админ панель IT Staffing',
    }
