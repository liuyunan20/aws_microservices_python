import wikipedia
from textblob import TextBlob


def wiki(name="war Goddess", length=2):
    """wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """return phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
