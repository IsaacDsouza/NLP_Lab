import re

def extract_digits(text):
    return re.findall(r'\d+', text)

text = "This is a test 123 sentence with numbers 4567."
print(text)
print(extract_digits(text))  # Output: ['123', '4567']
