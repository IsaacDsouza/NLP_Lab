import re

def remove_digits(text):
    return re.sub(r'\d+', '', text)

text = "This is a test 123 sentence with numbers 4567."
print(text)  
print(remove_digits(text))  # Output: "This is a test  sentence with numbers ."
