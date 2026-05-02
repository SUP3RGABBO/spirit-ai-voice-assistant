from rapidfuzz import fuzz

WAKE_WORDS = ["spirit", "hey spirit"]
SIMILARITY_THRESHOLD = 90


def is_wake_word(text):

    similarity = max(fuzz.partial_ratio(w, text.lower()) for w in WAKE_WORDS)
    return similarity >= SIMILARITY_THRESHOLD
