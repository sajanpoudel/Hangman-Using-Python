import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gallows import STAGES, gallows


def test_no_misses_shows_the_empty_gallows():
    assert gallows(0, 6) == STAGES[0]
