import re

def count_digits(text):
    return len(re.findall(r'\d', text))

text = "This is a test 123 sentence with numbers 4567."
print(text)
print(count_digits(text)) 
