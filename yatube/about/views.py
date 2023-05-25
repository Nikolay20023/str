from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name: str = 'about/author.html'
