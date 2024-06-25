from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    A view that displays the home page.
    """
    template_name = 'staff/index.html'

    def get_context_data(self, **kwargs):
        """
        Adds custom context data to the view.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['body'] = 'Содержимое главной страницы'
        return context
