from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'staff/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['body'] = 'Содержимое главной страницы'
        return context
