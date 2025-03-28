import nltk
from nltk.util import ngrams

def reverse_ngrams(text, n):
    words = nltk.word_tokenize(text.lower())[::-1]  # Reverse words
    return list(ngrams(words, n))

text = "This is a sample text for reverse n-grams."
print(reverse_ngrams(text, 2))  # Example: Reverse bigrams
