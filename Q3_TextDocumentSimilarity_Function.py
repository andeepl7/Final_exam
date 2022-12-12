from collections import defaultdict
from gensim import corpora
from gensim import models
from gensim import similarities
from gensim.test.utils import get_tmpfile


def TextDocumentSimilarity(corpus_documents, query_document):
    """
    Given a text corpus and a search document, this function:

    1) computes a dictionary of words for the given text corpus, and

    2) provides a list of documents and their similarity with the given
    search document (sorted in descending order).

    Expected parameters:
    corpus_documents:   A text corpus, represented as a list of strings.
    query_document:     A text document serving as a search document, represented as a string.

    """

    ###### CREATING THE TEXT CORPUS ######

    # Lowercase and tokenize each document of the given text corpus by using whitespace as delimiter for splitting.
    corpus_texts = [document.lower().split() for document in corpus_documents]

    # Create dictionary of word-tf pairs for the given text corpus
    corpus_tf_dict = defaultdict(int)    # Initialize dictionary that assigns the default value 0 to non-existing keys
    for corpus_text in corpus_texts:
        for token in corpus_text:
            corpus_tf_dict[token] += 1
    print("Dictionary of word-tf pairs for the given text corpus:", corpus_tf_dict)

    # Create gensim.corpora.Dictionary to map a unique integer word_id to each word in corpus_texts
    dictionary = corpora.Dictionary(corpus_texts)

    # Create gensim corpus of corpus_texts by converting it into bag-of-words (bow) format /
    # a list of (word_id, tf) tuples / a list of vectors.
    corpus_bow = [dictionary.doc2bow(corpus_text) for corpus_text in corpus_texts]

    ###### CREATING THE QUERY DOCUMENT ######
    # Create gensim corpus of query_document by lowercasing, tokenizing, and converting it
    # into bag-of-words (bow) format / a list of (word_id, tf) tuples / a list of vectors.
    query_bow = dictionary.doc2bow(query_document.lower().split())

    ### CREATING A TRANSFORMATION MODEL ###

    # Create TfidModel using the corpus_bow to transform vectors from bow representation to a vector space,
    # in which words that occur frequently across the documents in the text corpus are down-weighted,
    # and rarely occurring words are up-weighted.
    tf_idf = models.TfidfModel(corpus_bow)

    ### PREPARING FOR SIMILARITY QUERIES ###

    # Use the tf-idf model to transform the corpus_bow and initialize an index for it to prepare for similarity queries.
    index_tmpfile = get_tmpfile("index")    # Full path for output_prefix to store index matrix in.
    index = similarities.Similarity(index_tmpfile, tf_idf[corpus_bow], len(dictionary))

    ### PERFORMING SIMILARITY QUERIES ###

    # Query for document similarity between the query document and each index document of the corpus.
    sims_query_vs_corpus = index[tf_idf[query_bow]]

    # Sort document similarities in descending order and print.
    print("Document similarities between the query document and each index document of the text corpus (0.0 = 0% similar, 1.0 = 100% similar) (descending order):")
    for doc_pos, doc_sim in sorted(enumerate(sims_query_vs_corpus), key=lambda x: x[1], reverse=True):
        print(doc_pos, doc_sim)


### CALLING THE FUNCTION ###
# To call the function, please provide it with arguments for the two required parameters.

# A text corpus, represented as a list of strings.
corpus_documents = []

# A text document serving as a search document, represented as a string.
query_document = ""

# Call the function
TextDocumentSimilarity(corpus_documents, query_document)