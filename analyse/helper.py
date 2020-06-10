from collections import Counter
from pprint import pprint

import nltk

from nltk.corpus import stopwords


def read_file(file_location):
    """ Takes a file location and returns the file name and it's contents. """
    f = open(file_location, "r")
    return f.name, f.read()


def create_document_dictionary(files):
    """ Takes a list of files and returns a dictionary containing their names and file contents """
    document_dictionary = {}
    for file in files:
        document_dictionary[read_file(file)[0]] = read_file(file)[1]
    return document_dictionary


def extract_words(document_dictionary):
    """ Takes a dictionary containing file names and file content and returns a list containing a dictionary
        containing document_name, document_text, extracted_words and word_occurrences for each document.
    """
    # >>> import nltk
    # >>> nltk.download('stopwords')
    # >>> nltk.download('punkt')
    stop_word_list = stopwords.words('english')
    stop_word_set = set(stop_word_list)
    extracted_words_list_of_dicts = []
    for document_name, document_text in document_dictionary.items():
        #  to quickly test if a word is not a stop word, use a set:
        tokens = nltk.word_tokenize(document_text)
        extracted_words = []

        for word in tokens:
            if word.lower() not in stop_word_set and word.isalpha():
                extracted_words.append(word)
        extracted_words_list_of_dicts.append(
            {
                "document_name": document_name,
                "document_text": document_text,
                "extracted_words": extracted_words,
                "word_occurrences": word_occurrences(extracted_words),
                "word_contexts": get_context(document_text, extracted_words)
            })
    return extracted_words_list_of_dicts


def word_occurrences(extracted_words):
    """ Takes a list of words and returns a Counter of each word in the list. """
    word_occurrences = Counter(extracted_words)
    return word_occurrences


def all_document_word_occurrences(extracted_words_list_of_dicts):
    """ Takes a list containing multiple word occurrence count dictionaries and combines them to create a total."""
    total_word_occurrences = Counter()
    for extracted_word_dict in extracted_words_list_of_dicts:
        total_word_occurrences = total_word_occurrences + Counter(extracted_word_dict["extracted_words"])
    return total_word_occurrences


def process_documents(files):
    """ Takes a list of files and processes them all """
    document_dictionary = create_document_dictionary(files)
    document_reports = extract_words(document_dictionary)
    all_document_word_occurrences_count = all_document_word_occurrences(document_reports)
    pprint(document_reports)


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

# files = ['sample/doc1.txt','sample/doc2.txt']
# process_documents(files)
