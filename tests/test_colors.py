import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from colors import RESET, paint


def test_paint_wraps_the_text_in_the_colour_code():
    assert paint("hi", "red") == "\033[31mhi" + RESET


def test_paint_can_be_disabled():
    assert paint("hi", "red", enabled=False) == "hi"


def test_paint_ignores_unknown_colours():
    assert paint("hi", "purple") == "hi"
