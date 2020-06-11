from django.conf.urls import url
from django.urls import path

from frontend.views import HomeView, ReportView, ReportWordView, DocumentWordView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    path('report/<uuid:report_id>/', ReportView.as_view(), name="report"),
    path('report/<uuid:report_id>/<str:word>', ReportWordView.as_view(), name="report_word"),
    path('report/<uuid:report_id>/document/<int:document_id>', DocumentWordView.as_view(), name="document_word"),
    # path('report/<uuid:report_id>/<str:word>/<str:file_name>', ReportWordView.as_view(), name="report_word_file_name"),

]
