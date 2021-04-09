import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hangman import build_parser


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
