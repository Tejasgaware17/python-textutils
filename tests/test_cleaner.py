from textutils import normalize_whitespace, to_lowercase


def test_normalize_whitespace():
    assert normalize_whitespace("Hello   World") == "Hello World"


def test_to_lowercase():
    assert to_lowercase("HELLO") == "hello"
