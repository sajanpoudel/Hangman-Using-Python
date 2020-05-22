import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scores import Stats


def test_new_stats_are_empty():
    stats = Stats()
    assert (stats.wins, stats.losses, stats.played) == (0, 0, 0)
