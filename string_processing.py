from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk


def process_tokens(toks):
    # TODO: fill in the functions: process_tokens_1, 
    # process_tokens_2, and process_tokens_3 functions and
    # uncomment the one you want to test below

    # NOTE: make sure to switch back to process_tokens_original
    # and rebuild the index before
    # tackling the other assignment questions

    # return process_tokens_1(toks)
    # return process_tokens_2(toks)
    # return process_tokens_3(toks)
    return process_tokens_original(toks)


# get the nltk stopwords list
stopwords = set(nltk.corpus.stopwords.words("english"))
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')


def process_tokens_original(toks):
    """ Perform processing on tokens. This is the Linguistics Modules
    phase of index construction

    Args:
        toks (list(str)): all the tokens in a single document

    Returns:
        list(str): tokens after processing
    """
    new_toks = []
    for t in toks:
        # ignore stopwords
        if t in stopwords or t.lower() in stopwords:
            continue
        new_toks.append(t)
    return new_toks


def process_tokens_1(toks):
    """ Perform processing on tokens. This is the Linguistics Modules
    phase of index construction

    Args:
        toks (list(str)): all the tokens in a single document

    Returns:
        list(str): tokens after processing
    """
    new_toks = []
    puncs = [',', '.', ':', ';', '?', '!']
    for t in toks:
        # ignore stopwords
        if t in stopwords or t.lower() in stopwords:
            continue

        # TODO: your code should modify t and/or do some sort of filtering

        # remove punctuation at the end of tokens
        if t[len(t) - 1] in puncs:
            t = t[0:len(t) - 1]
        t = t.lower()

        new_toks.append(t)
    return new_toks


def process_tokens_2(toks):
    """ Perform processing on tokens. This is the Linguistics Modules
    phase of index construction

    Args:
        toks (list(str)): all the tokens in a single document

    Returns:
        list(str): tokens after processing
    """
    new_toks = []
    stemmer = PorterStemmer()
    for t in toks:
        # ignore stopwords
        if t in stopwords or t.lower() in stopwords:
            continue

        # TODO: your code should modify t and/or do some sort of filtering
        token_stem = stemmer.stem(t.lower())
        new_toks.append(token_stem)
    return new_toks


def process_tokens_3(toks):
    """ Perform processing on tokens. This is the Linguistics Modules
    phase of index construction

    Args:
        toks (list(str)): all the tokens in a single document

    Returns:
        list(str): tokens after processing
    """
    new_toks = []
    tags = nltk.pos_tag(toks)
    wordnet_tag = lambda t: 'a' if t == 'j' else (t if t in ['n', 'v', 'r'] else 'n')
    lemmatizer = WordNetLemmatizer()
    i=0
    for t in toks:
        # ignore stopwords
        if t in stopwords or t.lower() in stopwords:
            i+=1
            continue

        # TODO: your code should modify t and/or do some sort of filtering
        token_lemma = lemmatizer.lemmatize(t.lower(), wordnet_tag(tags[i][1][0].lower()))
        new_toks.append(token_lemma)
        i += 1
    return new_toks


def tokenize_text(data):
    """Convert a document as a string into a document as a list of
    tokens. The tokens are strings.

    Args:
        data (str): The input document

    Returns:
        list(str): The list of tokens.
    """
    # split text on spaces
    tokens = data.split()
    return tokens
