from textutils import *
from textutils.analyzer import word_count

text = "Hello     WORLD from      Python"
cleaned = normalize_whitespace(text)
print(to_lowercase(cleaned))
print(word_count(text))