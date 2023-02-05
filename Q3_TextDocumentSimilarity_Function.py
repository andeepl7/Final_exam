import math

""" READ DOCUMENTS and FORMATTING SECTION """
#This function opens a document(plain text .txt) return all text.
def getting_text(document_to_compare):
    try:
        with open(document_to_compare) as D:
            text = D.read()
            return text
    except:
        raise TypeError("This document cannot be read it")

#This function gave the right format to the text, removing special characters, lowercase and splitting the text into
#words.
def formatting_text(text):
    text_new = text
    characters_to_replace = ['\"', '-', '.', '!', ',','(',')',':']
    for char in characters_to_replace:
        text_new = text_new.replace(char, ' ')
        text_new = text_new.lower()
    word_list = text_new.split()
    return word_list

#This functiong count the unique words per document to compare.
def unique_word_frequency(word_list):
    dic_uwords = {}
    for new_word in word_list:
        if new_word in dic_uwords:
            dic_uwords[new_word] = dic_uwords[new_word] + 1
        else:
            dic_uwords[new_word] = 1
    return dic_uwords

""" DISTANCE CALCULATIONS """
#This function calculates the dotproduct distance between two documents.
def dotproduct_distance(dict_1, dict_2):
    dotproduct = 0.0
    for key in dict_1:
        if key in dict_2:
            dotproduct += (dict_1[key] * dict_2[key])
    return dotproduct

#This function calculates the euclidean distance between two documents.
def euclidean_distance(dict_1, dict_2):
    dist = 0.0
    for key in dict_1:
        if key in dict_2:
            dist += math.pow((dict_1[key] - dict_2[key]), 2)
    return math.sqrt(dist)

#These functions calculate the cosine distance between two documents.
#Euclidean lengths and cosine distance
def v_magnitude(d):
    return math.sqrt(sum([math.pow(v, 2) for k, v in d.items()]))

def cosine_distance(dict1, dict2):
    return dotproduct_distance(dict1, dict2)/(v_magnitude(dict1)*v_magnitude(dict2))

"""PRINTING RESULTS"""

#This function gets the dictionary of unique words per document.
def getting_dicts(document):
    all_text = getting_text(document)
    text_format = formatting_text(all_text)
    doc_dict = unique_word_frequency(text_format)
    return doc_dict

#In order to test our functions, the testing will be perform with 3 documents, where the first one is compared with the
#other two documents.

#Callable function
metric_computation = {'dotproduct': dotproduct_distance,
          'euclidean': euclidean_distance,
          'cosine': cosine_distance
          }

#The principal document is call reference document, the other two documents are auxiliar
def test_doc_similarity(ref_doc,aux_doc,metric):
    ref_dict = getting_dicts(ref_doc)
    aux_dict= getting_dicts(aux_doc)
    return metric_computation[metric](ref_dict, aux_dict)

#Sort results in descending order
def sort_dict(d, reverse):
    return sorted(d.items(), key=lambda x: x[1], reverse=reverse)

#Function to print the number of unique words and the similarity of the text and the results of the
#documents similarities
def print_info_docs(doc1,doc2,doc3):
    documents_to_compare= doc1,doc2,doc3
    for doc in documents_to_compare:
        dct = getting_dicts(doc)
        unique_words = len(dct)
        print(f"Your file: {doc} got {unique_words} unique words")
        print('-' *50)
    ref_doc = doc1
    aux_docs = {'Doc1': doc1, 'Doc2': doc2, 'Doc3': doc3}
    results_dotproduct = {}
    results_euclidean = {}
    results_cosine = {}
    for k, v in aux_docs.items():
        results_dotproduct[k] = test_doc_similarity(ref_doc, v, 'dotproduct')
        results_euclidean[k] = test_doc_similarity(ref_doc, v, 'euclidean')
        results_cosine[k] = test_doc_similarity(ref_doc, v, 'cosine')
    print('DOT PRODUCT')
    print(sort_dict(results_dotproduct, reverse=True))
    print('EUCLIDEAN')
    print(sort_dict(results_euclidean, reverse=False))
    print('COSINE')
    print(sort_dict(results_cosine, reverse=True))

"""Testing Section """

document1 = "Doc_Test_1.txt"
document2 = "Doc_Test_2.txt"
document3 = "Doc_Test_3.txt"

print_info_docs(document1,document2,document3)


