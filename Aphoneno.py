import re

pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b"

text = """
Call me at 123-456-7890 or (123) 456-7890. My office number is +1 123 456 7890. 
You can also reach me at 123.456.7890 or 1234567890.
"""
print(text)
phones = re.findall(pattern, text)
print(phones)
