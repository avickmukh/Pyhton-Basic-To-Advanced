"""Get count of word in a sentence and Print word each per line in a sentence

usage: 
    Python words.py <myString>
"""
import sys

def word_count(myString):
    """It will count Number of words in a string

    Args:
        myString : user given string
    """
    words = myString.split()

    return len(words)


def print_words(myString):
    """Print words one per line

    Args:
        myString : User given sentence
    """
    for word in myString.split():
        print(word)

def main(myString):
    """Get count of words and print different words in separate line
    
    Args:
        myString : User given string
    """
    wordCount = word_count(myString)
    print('In this sentence total word count: {}'.format(wordCount))
    print_words(myString)

#python words.py 
if __name__ == '__main__' : main(sys.argv[1])
#if __name__ == '__main__' : main('my name is avick')
