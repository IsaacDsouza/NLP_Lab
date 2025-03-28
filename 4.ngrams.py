from collections import Counter
from nltk.util import ngrams
import nltk

nltk.download('punkt')

def word_frequencies(text, n):
    words = nltk.word_tokenize(text.lower())
    return Counter(ngrams(words, n))

# Example usage
text = "This is a sample sentence with sample words in a sentence."
print(word_frequencies(text, 2))  # Bigram frequencies
