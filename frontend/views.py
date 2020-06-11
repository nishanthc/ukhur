from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['website_name'] = "Ukhur"

        return context


class ReportView(TemplateView):
    template_name = "report.html"

    def get_context_data(self, report_id, *args, **kwargs):
        context = super(ReportView, self).get_context_data(*args, **kwargs)

        context['website_name'] = "Ukhur"
        context["report_id"] = report_id

        return context
