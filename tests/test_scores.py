import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scores import Stats


def test_new_stats_are_empty():
    stats = Stats()
    assert (stats.wins, stats.losses, stats.played) == (0, 0, 0)


def test_a_win_counts_and_extends_the_streak():
    stats = Stats()
    stats.record(True)
    stats.record(True)
    assert (stats.wins, stats.streak, stats.best_streak) == (2, 2, 2)


def test_a_loss_resets_the_streak_but_keeps_the_best():
    stats = Stats()
    for result in [True, True, False, True]:
        stats.record(result)
    assert (stats.streak, stats.best_streak, stats.losses) == (1, 2, 1)


def test_win_rate_is_zero_before_any_round():
    assert Stats().win_rate() == 0.0
