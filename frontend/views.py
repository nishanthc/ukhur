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

        context['website_name'] = "Ukhur"
        context["report_id"] = report_id

        report = Report.objects.get(uuid=report_id)
        documents = []
        for document in report.document_set.all():
            documents.append(
                {
                    document.file_name: document.id
                }
            )
        context["documents"] = documents

        total_word_occurrences = OrderedDict(
            sorted(report.word_occurrences_count.items(), key=itemgetter(1), reverse=True))
        context["total_word_occurrences"] = total_word_occurrences
        for x, z in total_word_occurrences.items():
            print(x, z)
        return context


class ReportWordView(TemplateView):
    template_name = "sentences.html"

    def get_context_data(self, report_id, word, *args, **kwargs):
        context = super(ReportWordView, self).get_context_data(*args, **kwargs)

        context['website_name'] = "Ukhur"
        context["report_id"] = report_id

        report = Report.objects.get(uuid=report_id)
        sentences = {}
        documents = []
        for document in report.document_set.all():
            try:
                sentences[document.file_name] = document.word_occurrences_sentence[word]
            except KeyError:
                pass
                documents.append(
                    {
                        document.file_name: document.id
                    }
                )

        context["documents"] = documents
        context["sentences"] = sentences
        context["word"] = word

        return context


class DocumentWordView(TemplateView):
    template_name = "report.html"

    def get_context_data(self, report_id, document_id, *args, **kwargs):
        context = super(DocumentWordView, self).get_context_data(*args, **kwargs)

        context['website_name'] = "Ukhur"
        context["report_id"] = report_id

        report = Report.objects.get(uuid=report_id)
        documents = []
        for document in report.document_set.all():
            documents.append(
                {
                    document.file_name: document.id
                 }
            )
        context["documents"] = documents

        document_obj = Document.objects.get(id=document_id)
        total_word_occurrences = OrderedDict(
            sorted(document_obj.word_occurrences_count.items(), key=itemgetter(1), reverse=True))
        context["total_word_occurrences"] = total_word_occurrences
        for x, z in total_word_occurrences.items():
            print(x, z)
        return context
