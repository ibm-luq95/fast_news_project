from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home Page"
        return context


class AboutView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "About Page"
        return context


# Function based view
# def home(request):
#     return render(request, "home/home.html", {'title': "Home page"})

# def about(request):
#     return render(request, "home/about.html")
