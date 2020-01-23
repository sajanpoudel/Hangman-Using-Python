import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hangman import BLANK, reveal_letter


def test_reveal_letter_fills_the_matching_position():
    word = list("cat")
    board = [BLANK] * 3
    assert reveal_letter("a", word, board) == 1
    assert board == [BLANK, "a", BLANK]


def test_reveal_letter_fills_every_repeated_letter():
    word = list("banana")
    board = [BLANK] * 6
    assert reveal_letter("a", word, board) == 3
    assert board == [BLANK, "a", BLANK, "a", BLANK, "a"]


def test_reveal_letter_returns_zero_for_a_miss():
    word = list("cat")
    board = [BLANK] * 3
    assert reveal_letter("z", word, board) == 0
    assert board == [BLANK] * 3


def test_reveal_letter_keeps_letters_found_earlier():
    word = list("cat")
    board = ["c", BLANK, BLANK]
    reveal_letter("t", word, board)
    assert board == ["c", BLANK, "t"]
