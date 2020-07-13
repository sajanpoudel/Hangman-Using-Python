import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scores import Stats, load_stats, save_stats


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


def test_win_rate_is_the_share_of_wins():
    stats = Stats(wins=3, losses=1)
    assert stats.win_rate() == 0.75


def test_summary_mentions_wins_and_streaks():
    stats = Stats(wins=3, losses=1, streak=2, best_streak=3)
    assert stats.summary() == "Won 3 of 4 (75%), streak 2, best streak 3"


def test_stats_round_trip_through_a_file(tmp_path):
    path = tmp_path / "scores.json"
    save_stats(Stats(wins=5, losses=2, streak=1, best_streak=4), path)
    assert load_stats(path) == Stats(wins=5, losses=2, streak=1, best_streak=4)


def test_save_creates_missing_folders(tmp_path):
    path = tmp_path / "deep" / "er" / "scores.json"
    save_stats(Stats(wins=1), path)
    assert path.exists()
