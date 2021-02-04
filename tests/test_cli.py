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
