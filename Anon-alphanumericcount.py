import re

def count_non_alnum(text):
    return len(re.findall(r"\W", text))

# Example usage
text = "Hello, World! 123 @#$"
print(text)
print(count_non_alnum(text))
