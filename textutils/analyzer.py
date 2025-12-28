from .cleaner import normalize_whitespace

def word_count(text: str) -> int:
    cleaned = normalize_whitespace(text)
    return len(cleaned.split())