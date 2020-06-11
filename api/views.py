from pprint import pprint

from django.http import HttpResponse
from django.views import View
from pathlib import Path

from analyse.helper import process_documents


class FileUpload(View):
    def post(self, request):
        if request.FILES:
            files = request.FILES
        else:
            return HttpResponse(status=402)

        for file_name, file in files.items():
            if Path(file._name).suffix == '.txt':
                pass
            else:
                return HttpResponse(status=402)

        process_documents(files)

        return HttpResponse('result')
