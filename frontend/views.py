from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "homepage.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     plans = Product.objects.filter(is_addon=False).values('id', 'name', 'liquid_quantity')
    #     plans = [entry for entry in plans]
    #     context['plans'] = plans
    #     faqs = Faq.objects.values('question', 'answer')
    #     faqs = [entry for entry in faqs]
    #     context['faqs'] = faqs
    #
    #     return context