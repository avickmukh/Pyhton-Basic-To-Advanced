"""Retrive and Print words from a URL

usage: 
    Python words.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of stringd contanining the words from the document.
    """
    story_words = []
    #'http://sixty-north.com/c/t.txt'
    with urlopen(url) as story:
        
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_words(items):
    """Print items one per line

    Args:
        items : An iterable series of items
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text document from a URL
    
    Args:
        url : The URL of a UTF-8 text document
    """
    words = fetch_words(url)
    print_words(words)

#python words.py 
if __name__ == '__main__' : main(sys.argv[1])