import random

def random_splits(word):
    positions = random.sample(range(1, len(word)), len(word) - 1)
    return [(word[:i], word[i:]) for i in positions]

# Example usage
word = "CARRIED"
print(word)
print(random_splits(word))
