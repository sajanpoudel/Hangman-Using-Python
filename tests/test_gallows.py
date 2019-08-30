import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gallows import STAGES, gallows


def test_no_misses_shows_the_empty_gallows():
    assert gallows(0, 6) == STAGES[0]


def test_all_attempts_used_shows_the_full_figure():
    assert gallows(6, 6) == STAGES[-1]


def test_the_drawing_scales_to_the_attempts_allowed():
    assert gallows(1, 2) == STAGES[3]
    assert gallows(3, 3) == STAGES[-1]


def test_misses_beyond_the_limit_are_clamped():
    assert gallows(99, 3) == STAGES[-1]
    assert gallows(-4, 3) == STAGES[0]
