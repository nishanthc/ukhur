from collections import OrderedDict
from operator import itemgetter
from pprint import pprint

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from analyse.models import Report, Document


class HomeView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['website_name'] = "Ukhur"

        return context


class ReportView(TemplateView):
    template_name = "report.html"

    def get_context_data(self, report_id, *args, **kwargs):
        context = super(ReportView, self).get_context_data(*args, **kwargs)
        document_id = self.request.GET.get('document', '')
        context['website_name'] = "Ukhur"
        context["report_id"] = report_id
        report = Report.objects.get(uuid=report_id)
        context["documents"] = create_list_of_documents(report)
        if not document_id:
            total_word_occurrences = OrderedDict(
                sorted(report.word_occurrences_count.items(), key=itemgetter(1), reverse=True))
            context["total_word_occurrences"] = total_word_occurrences
        else:
            context["page_document_id"] = int(self.request.GET.get('document', ''))
            document_obj = Document.objects.get(id=document_id)
            total_word_occurrences = OrderedDict(
                sorted(document_obj.word_occurrences_count.items(), key=itemgetter(1), reverse=True))
            context["total_word_occurrences"] = total_word_occurrences

        return context


class ReportWordView(TemplateView):
    template_name = "sentences.html"

    def get_context_data(self, report_id, word, *args, **kwargs):
        context = super(ReportWordView, self).get_context_data(*args, **kwargs)
        document_id = self.request.GET.get('document', '')

        context['website_name'] = "Ukhur"
        context["report_id"] = report_id

        report = Report.objects.get(uuid=report_id)
        sentences = {}
        if not document_id:
            for document in report.document_set.all():
                try:
                    sentences[document.file_name] = document.word_occurrences_sentence[word]
                except KeyError:
                    pass
            context["sentences"] = sentences
        else:

            document_obj = Document.objects.get(id=document_id)
            context["page_document_id"] = int(self.request.GET.get('document', ''))
            context["page_file_name"] = document_obj.file_name
            context["sentences"] = document_obj.word_occurrences_sentence
        context["documents"] = create_list_of_documents(report)
        context["word"] = word

        return context




def create_list_of_documents(report):
    documents = []
    for document in report.document_set.all():
        documents.append(
            {
                document.file_name: document.id
            }
        )
    return documents
