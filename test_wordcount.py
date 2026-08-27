from wordcount import word_count


def test_single_word():
    assert word_count("hello") == {"hello": 1}


def test_repeated_words_case_insensitive():
    assert word_count("Hello hello world") == {"hello": 2, "world": 1}


def test_empty_string_returns_empty_dict():
    assert word_count("") == {}
