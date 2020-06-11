from collections import Counter
from pprint import pprint

import nltk

from nltk.corpus import stopwords

from analyse.models import Report, Document


def read_file(file_location):
    """ Takes a file location and returns the file name and it's contents. """
    f = open(file_location, "r")
    return f.name, f.read()


def create_documents(files, report):
    """ Takes a list of files and returns a dictionary containing their names and file contents """
    for file_name, file in files.items():
        text = file.read().decode('utf-8')
        document = Document()
        document.report = report
        document.file_name = file._name
        document.text = text
        document.save()
    return True


def analyse_word_occurrences(report):
    """ Takes a dictionary containing file names and file content and returns a list containing a dictionary
        containing document_name, document_text, extracted_words and word_occurrences for each document.
    """
    # >>> import nltk
    # >>> nltk.download('stopwords')
    # >>> nltk.download('punkt')
    stop_word_list = stopwords.words('english')
    stop_word_set = set(stop_word_list)
    extracted_words_list_of_dicts = []
    for document in report.document_set.all():
        #  to quickly test if a word is not a stop word, use a set:
        tokens = nltk.word_tokenize(document.text)
        extracted_words = []
        for word in tokens:
            if word.lower() not in stop_word_set and word.isalpha():
                extracted_words.append(word)
        document.word_occurrences_count = calculate_word_occurrences(extracted_words)
        document.word_occurrences_sentence = get_context(document.text, extracted_words)
        document.save()
    return True


def calculate_word_occurrences(extracted_words):
    """ Takes a list of words and returns a Counter of each word in the list. """
    word_occurrences = Counter(extracted_words)
    return word_occurrences


def calculate_total_word_occurrences(report):
    """ Takes a list containing multiple word occurrence count dictionaries and combines them to create a total."""
    total_word_occurrences = Counter()
    for document in report.document_set.all():
        total_word_occurrences = total_word_occurrences + Counter(document.word_occurrences_count)
    report.word_occurrences_count = total_word_occurrences
    report.save()
    return total_word_occurrences


def process_documents(files):
    """ Takes a list of files and processes them all """
    report = Report()
    report.save()
    create_documents(files, report)
    analyse_word_occurrences(report)
    calculate_total_word_occurrences(report)
    # pprint(document_reports)
    return str(report.uuid)


def get_context(document_text, extracted_words):
    """ Takes document text and a list of extracted words and returns a dictionary containing a list of sentences
        containing each word.
    """
    extracted_words = list(set(extracted_words))
    sentences = nltk.sent_tokenize(document_text)
    context = {}
    for extracted_word in extracted_words:
        context[extracted_word] = []
    for sentence in sentences:
        for extracted_word in extracted_words:
            if extracted_word in sentence.split():
                context[extracted_word].append(sentence)
    return context
