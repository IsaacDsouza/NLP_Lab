import re

def split_text(text):
    return re.findall(r"\b\w+\b", text)

# Example usage
text = "This is a sample text,with some punctuation marks! Also, newlines and  carriage returns.Let's split it."
print(split_text(text))
