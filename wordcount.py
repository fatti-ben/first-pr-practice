def word_count(text):
    """Count occurrences of each word in text, case-insensitive."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
