from pprint import pprint

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import View
from pathlib import Path

from analyse.helper import process_documents


class FileUpload(View):
    def post(self, request):
        response = {}
        if request.FILES:
            files = request.FILES
        else:
            response["error"] = "No documents were uploaded."
            return JsonResponse(response)

        for file_name, file in files.items():
            if Path(file._name).suffix == '.txt':
                pass
            else:
                response["error"] = "Documents are not .txt files"
                return JsonResponse(response)
        uuid = process_documents(files)
        url = reverse('report', urlconf=None, args=(uuid,), kwargs=None)
        response["url"] = url

        return JsonResponse(response)
