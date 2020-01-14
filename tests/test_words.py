import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from words import CATEGORIES, WORDS, words_for


def test_words_for_a_known_category():
    assert words_for("animals") == CATEGORIES["animals"]
