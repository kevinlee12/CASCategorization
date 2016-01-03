from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """View that renders the home page."""

    template_name = 'journal/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name, locals())
