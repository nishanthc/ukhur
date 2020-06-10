from pprint import pprint

from django.http import HttpResponse
from django.views import View


class FileUpload(View):
    def post(self, request):
        files = request.FILES
        pprint(files)
        for file_name,file in files.items():
            pprint(file._name)
            print(file.read().decode('utf-8'))
        return HttpResponse('result')
