import wikipedia


def wiki(name="war Goddess", length=2):
    """wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results
