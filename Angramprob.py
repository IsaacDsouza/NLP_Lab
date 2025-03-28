import nltk
from collections import Counter
from nltk.util import ngrams

def ngram_probabilities(text, n):
    words = nltk.word_tokenize(text.lower())
    ngram_counts = Counter(ngrams(words, n))
    total_ngrams = sum(ngram_counts.values())
    return {ngram: count / total_ngrams for ngram, count in ngram_counts.items()}

text = "This is a sample text for n-gram probability calculation."
print(ngram_probabilities(text, 2))  # Example: Bigram probabilities
