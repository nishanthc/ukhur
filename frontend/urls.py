from django.conf.urls import url
from django.urls import path

from frontend.views import HomeView, ReportView, ReportWordView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    path('report/<uuid:report_id>/', ReportView.as_view(), name="report"),
    path('report/<uuid:report_id>/<str:word>/', ReportWordView.as_view(), name="report_word"),

]
