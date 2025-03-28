import re

pattern = r"\b\d{2}/\d{2}/\d{4}\b"

text = "Today's date is 27/03/2025. Yesterday was 26/03/2025, and tomorrow is 28/03/2025."
print(text)
dates = re.findall(pattern, text)
print(dates)
