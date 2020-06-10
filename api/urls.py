from django.conf.urls import url

from api.views import FileUpload
from frontend.views import HomeView

urlpatterns = [
    url(r'^file-upload', FileUpload.as_view(), name="file-upload"),
]
