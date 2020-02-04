import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import random

from hangman import (
    BLANK,
    WORDS,
    choose_word,
    is_valid_guess,
    new_board,
    normalize_guess,
    play_round,
    reveal_letter,
)


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


def test_new_board_has_one_blank_per_letter():
    assert new_board("hello") == [BLANK] * 5
    assert new_board("") == []


def test_choose_word_comes_from_the_list():
    assert choose_word(["only"]) == "only"


def test_choose_word_is_repeatable_with_a_seeded_rng():
    first = choose_word(WORDS, random.Random(7))
    second = choose_word(WORDS, random.Random(7))
    assert first == second
    assert first in WORDS


def test_normalize_guess_lowercases_and_strips():
    assert normalize_guess("  A ") == "a"


def test_is_valid_guess_accepts_one_letter():
    assert is_valid_guess("a")
    assert is_valid_guess("Z")


def test_is_valid_guess_rejects_other_input():
    for bad in ["", "ab", "1", " ", "!"]:
        assert not is_valid_guess(bad)


def fake_io(answers):
    """Return an ask function fed from answers and a list that collects the output."""
    queue = iter(answers)
    output = []
    return (lambda prompt: next(queue)), output.append, output
