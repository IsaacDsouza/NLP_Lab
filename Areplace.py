import re

def replace_non_alnum(text, char):
    return re.sub(r"\W", char, text)

# Example usage
text = "Hello, World! 123 @#$"
print(text)
print(replace_non_alnum(text, "*"))
