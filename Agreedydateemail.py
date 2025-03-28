import re

def tokenize_priority(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|\d{1,2}/\d{1,2}/\d{2,4}|\w+[-.]\w+|\w+'
    return re.findall(pattern, text)

text = "Contact me at test.email@example.com by 12/04/2024 or visit example-site.com."
print(tokenize_priority(text))
