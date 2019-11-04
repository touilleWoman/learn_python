import string
import sys

def count(str):
    upper = 0
    space = 0
    lower = 0
    punc = 0
    for x in str:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x == ' ':
            space += 1
        elif x in string.punctuation:
            punc += 1
    print("The text contains", len(str), "characters:")
    print("-", upper, "upper letters")
    print("-", lower, "lower letters")
    print("-", punc, "punctuation marks")
    print("-", space, "spaces")

def text_analyzer(str = "empty"):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if str == "empty":
        str = input("What is the text to analyse?\n")
    count(str)

if __name__ == '__main__':
     text_analyzer()

# doubts about input(), how to have a new prompt?