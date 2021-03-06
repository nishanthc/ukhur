from django.contrib import admin
from analyse.models import Report, Document


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(Document)
class ReportAdmin(admin.ModelAdmin):
    fields = ('report',
              'file_name',
              'text',
              'word_occurrences_count',
              'word_occurrences_sentence'
              )
