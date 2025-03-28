import re

def clean_text(text):
    return re.sub(r"^\W+|\W+$", "", text)

# Example usage
text = "!Hello, World?!"
print(text)
print(clean_text(text))
