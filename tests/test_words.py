import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from words import CATEGORIES, WORDS, load_words, words_for


def test_words_for_a_known_category():
    assert words_for("animals") == CATEGORIES["animals"]


def test_words_for_ignores_case():
    assert words_for("ANIMALS") == CATEGORIES["animals"]


def test_words_for_falls_back_to_every_word():
    assert words_for("nonsense") == WORDS
    assert words_for(None) == WORDS
    assert words_for("") == WORDS


def test_category_words_are_in_the_full_list():
    for words in CATEGORIES.values():
        assert set(words) <= set(WORDS)


def test_every_word_is_lowercase_letters():
    for word in WORDS:
        assert word.isalpha() and word == word.lower(), word


def test_categories_have_no_duplicates():
    for words in CATEGORIES.values():
        assert len(words) == len(set(words))


def test_load_words_reads_one_word_per_line(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("apple\nbanana\n")
    assert load_words(str(path)) == ["apple", "banana"]


def test_load_words_skips_blank_and_invalid_lines(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("apple\n\n  \nb4d\nkiwi-fruit\nPear\n")
    assert load_words(str(path)) == ["apple", "pear"]


def test_load_words_of_an_empty_file_is_empty(tmp_path):
    path = tmp_path / "words.txt"
    path.write_text("")
    assert load_words(str(path)) == []
