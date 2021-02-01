import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hangman import build_parser


def parse(*args):
    return build_parser().parse_args(list(args))
