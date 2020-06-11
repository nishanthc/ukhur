from django.conf.urls import url
from django.urls import path

from frontend.views import HomeView, ReportView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    path('report/<uuid:report_id>/', ReportView.as_view(), name="report"),
]
