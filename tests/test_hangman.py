import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import random

from hangman import (
    BLANK,
    DIFFICULTIES,
    WORDS,
    attempts_for,
    choose_word,
    hidden_positions,
    is_valid_guess,
    new_board,
    normalize_guess,
    pick_hint,
    play_round,
    reveal_letter,
    unused_letters,
    wants_another_round,
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


def test_play_round_is_won_when_every_letter_is_found():
    ask, say, output = fake_io(["c", "a", "t"])
    assert play_round("cat", ask, say) is True
    assert any("WAS RIGHT" in str(line) for line in output)


def test_play_round_is_lost_after_three_wrong_guesses():
    ask, say, output = fake_io(["x", "y", "z"])
    assert play_round("cat", ask, say) is False
    assert any("the correct answer was: cat" in str(line) for line in output)


def test_wrong_guesses_are_counted_but_right_ones_are_free():
    ask, say, _ = fake_io(["x", "c", "y", "a", "t"])
    assert play_round("cat", ask, say) is True


def test_upper_case_guesses_count():
    ask, say, _ = fake_io(["C", "A", "T"])
    assert play_round("cat", ask, say) is True


def test_invalid_guesses_do_not_use_up_attempts():
    ask, say, output = fake_io(["", "12", "!", "c", "a", "t"])
    assert play_round("cat", ask, say) is True
    assert sum("single letter" in str(line) for line in output) == 3


def test_guessing_the_whole_word_wins_the_round():
    ask, say, _ = fake_io(["Cat"])
    assert play_round("cat", ask, say) is True


def test_a_wrong_whole_word_costs_an_attempt():
    ask, say, output = fake_io(["dog", "cow", "pig"])
    assert play_round("cat", ask, say) is False
    assert any("not the word" in str(line) for line in output)


def test_repeating_a_wrong_letter_is_not_charged_twice():
    ask, say, output = fake_io(["x", "x", "y", "c", "a", "t"])
    assert play_round("cat", ask, say) is True
    assert any("already tried" in str(line) for line in output)


def test_wrong_guess_message_shows_the_attempts_left():
    ask, say, output = fake_io(["x", "c", "a", "t"])
    play_round("cat", ask, say)
    assert any("2 left" in str(line) for line in output)


def test_wants_another_round_accepts_yes_in_any_case():
    for answer in ["y", "Y", "yes", " Yes "]:
        assert wants_another_round(lambda prompt, a=answer: a)


def test_wants_another_round_treats_everything_else_as_no():
    for answer in ["n", "no", "", "maybe"]:
        assert not wants_another_round(lambda prompt, a=answer: a)


def test_more_attempts_allow_more_misses():
    ask, say, _ = fake_io(["x", "y", "z", "q", "c", "a", "t"])
    assert play_round("cat", ask, say, attempts=5) is True


def test_a_single_attempt_ends_the_round_after_one_miss():
    ask, say, _ = fake_io(["x"])
    assert play_round("cat", ask, say, attempts=1) is False


def test_the_gallows_is_drawn_after_a_miss():
    ask, say, output = fake_io(["x", "c", "a", "t"])
    play_round("cat", ask, say)
    assert any("+---+" in str(line) for line in output)


def test_no_gallows_is_drawn_without_misses():
    ask, say, output = fake_io(["c", "a", "t"])
    play_round("cat", ask, say)
    assert not any("+---+" in str(line) for line in output)


def test_attempts_for_known_levels():
    assert attempts_for("easy") == 8
    assert attempts_for("normal") == 6
    assert attempts_for("hard") == 3


def test_attempts_for_ignores_case_and_defaults_to_normal():
    assert attempts_for("EASY") == DIFFICULTIES["easy"]
    assert attempts_for("impossible") == DIFFICULTIES["normal"]


def test_harder_levels_allow_fewer_attempts():
    assert DIFFICULTIES["easy"] > DIFFICULTIES["normal"] > DIFFICULTIES["hard"]


def test_hidden_positions_lists_the_blanks():
    assert hidden_positions(list("cat"), ["c", BLANK, BLANK]) == [1, 2]


def test_hidden_positions_is_empty_when_solved():
    assert hidden_positions(list("cat"), list("cat")) == []


def test_pick_hint_returns_a_hidden_letter():
    hint = pick_hint(list("cat"), ["c", BLANK, "t"], random.Random(1))
    assert hint == "a"


def test_pick_hint_returns_none_when_nothing_is_hidden():
    assert pick_hint(list("cat"), list("cat")) is None


def test_a_hint_costs_one_attempt_and_reveals_a_letter():
    ask, say, output = fake_io(["?", "x", "y", "c", "a", "t"])
    assert play_round("cat", ask, say, attempts=4) is True
    assert any("Hint:" in str(line) for line in output)


def test_no_hint_is_given_on_the_last_attempt():
    ask, say, output = fake_io(["?", "x"])
    assert play_round("cat", ask, say, attempts=1) is False
    assert any("No hints" in str(line) for line in output)


def test_tried_letters_are_listed_in_order():
    ask, say, output = fake_io(["t", "a", "x", "c"])
    play_round("cat", ask, say)
    assert "Tried: a c t x" in [str(line) for line in output]


def test_unused_letters_skips_the_tried_ones():
    remaining = unused_letters({"a", "e", "z"})
    assert remaining.startswith("b c d f")
    assert "a" not in remaining.split() and "z" not in remaining.split()
    assert len(remaining.split()) == 23


def test_round_output_lists_the_unused_letters():
    ask, say, output = fake_io(["x", "c", "a", "t"])
    assert play_round("cat", ask, say) is True
    assert any(str(line).startswith("Unused: ") for line in output)
