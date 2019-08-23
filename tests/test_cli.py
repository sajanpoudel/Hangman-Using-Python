import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hangman import build_parser, filter_by_length, main, resolve_attempts, resolve_words
from words import CATEGORIES, WORDS


def parse(*args):
    return build_parser().parse_args(list(args))


def test_defaults():
    args = parse()
    assert args.difficulty == "normal"
    assert args.attempts is None
    assert args.category is None
    assert args.words_file is None
    assert args.seed is None
    assert args.no_color is False


def test_difficulty_and_attempts():
    args = parse("--difficulty", "hard", "--attempts", "4")
    assert (args.difficulty, args.attempts) == ("hard", 4)


def test_category_and_words_file():
    args = parse("--category", "animals", "--words-file", "w.txt")
    assert (args.category, args.words_file) == ("animals", "w.txt")


def test_seed_is_an_integer():
    assert parse("--seed", "42").seed == 42


def test_no_color_flag():
    assert parse("--no-color").no_color is True


def test_a_non_numeric_attempts_value_is_rejected(capsys):
    try:
        parse("--attempts", "many")
    except SystemExit as error:
        assert error.code == 2
    else:
        raise AssertionError("expected the parser to exit")


def test_attempts_come_from_the_difficulty():
    assert resolve_attempts(parse("--difficulty", "easy")) == 8


def test_explicit_attempts_override_the_difficulty():
    assert resolve_attempts(parse("--difficulty", "easy", "--attempts", "2")) == 2


def test_attempts_are_at_least_one():
    assert resolve_attempts(parse("--attempts", "0")) == 1
    assert resolve_attempts(parse("--attempts", "-5")) == 1


def test_words_default_to_the_full_list():
    assert resolve_words(parse()) == WORDS


def test_words_follow_the_category():
    assert resolve_words(parse("--category", "places")) == CATEGORIES["places"]


def test_words_come_from_the_file_when_it_has_words(tmp_path):
    path = tmp_path / "w.txt"
    path.write_text("alpha\nbeta\n")
    assert resolve_words(parse("--words-file", str(path))) == ["alpha", "beta"]


def test_an_empty_word_file_falls_back_to_the_category(tmp_path):
    path = tmp_path / "w.txt"
    path.write_text("\n123\n")
    assert (
        resolve_words(parse("--words-file", str(path), "--category", "animals"))
        == CATEGORIES["animals"]
    )


def test_filter_by_length_keeps_words_inside_the_limits():
    words = ["zoo", "wolf", "donkey", "university"]
    assert filter_by_length(words, 4, 6) == ["wolf", "donkey"]
    assert filter_by_length(words, minimum=7) == ["university"]
    assert filter_by_length(words, maximum=3) == ["zoo"]
    assert filter_by_length(words) == words


def test_resolve_words_applies_the_length_limits():
    args = parse("--min-length", "8")
    assert resolve_words(args) and all(len(word) >= 8 for word in resolve_words(args))


def test_resolve_words_falls_back_when_no_word_fits():
    args = parse("--min-length", "40")
    assert resolve_words(args) == WORDS


def test_show_stats_prints_the_saved_results_without_playing(tmp_path, capsys):
    stats_file = tmp_path / "stats.json"
    stats_file.write_text('{"wins": 3, "losses": 1, "streak": 2, "best_streak": 2}')
    main(["--show-stats", "--stats-file", str(stats_file)])
    assert "Won 3 of 4 (75%)" in capsys.readouterr().out


def test_main_says_goodbye_when_input_ends(tmp_path, capsys, monkeypatch):
    def end_of_input(*args, **kwargs):
        raise EOFError

    monkeypatch.setattr("hangman.play_round", end_of_input)
    main(["--stats-file", str(tmp_path / "stats.json"), "--seed", "1"])
    assert "Goodbye!" in capsys.readouterr().out
