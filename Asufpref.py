def prefixes_suffixes(word):
    return [word[:i] for i in range(1, len(word) + 1)], [word[i:] for i in range(len(word))]

# Example usage
word = "CARRIED"
print(word)
prefixes, suffixes = prefixes_suffixes(word)
print("Prefixes:", prefixes)
print("Suffixes:", suffixes)
