from django.contrib import admin

# Register your models here.
from analyse.models import Report, Document


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class ReportAdmin(admin.ModelAdmin):
    fields = ('report', 'file_name',)
