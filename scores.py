"""Win and loss bookkeeping for a session."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Stats:
    """Results of the rounds played so far."""

    wins: int = 0
    losses: int = 0
    streak: int = 0
    best_streak: int = 0
    points: int = 0

    @property
    def played(self) -> int:
        """Number of rounds played."""
        return self.wins + self.losses

    def record(self, won: bool, points: int = 0) -> None:
        """Add the result of one round and the points it earned."""
        self.points += points
        if won:
            self.wins += 1
            self.streak += 1
            self.best_streak = max(self.best_streak, self.streak)
        else:
            self.losses += 1
            self.streak = 0

    def win_rate(self) -> float:
        """Share of rounds won between 0 and 1 (0 when nothing was played)."""
        return self.wins / self.played if self.played else 0.0

    def summary(self) -> str:
        """One line for the end of a round."""
        return f"Won {self.wins} of {self.played} ({self.win_rate():.0%}), streak {self.streak}, best streak {self.best_streak}"


def round_points(won: bool, word: str, attempts: int) -> int:
    """Ten points per letter of a guessed word, doubled or tripled on the harder levels.

    Three attempts or fewer count triple, up to six attempts double, more than that single.
    A lost round earns nothing.
    """
    if not won:
        return 0
    multiplier = 3 if attempts <= 3 else 2 if attempts <= 6 else 1
    return len(word) * 10 * multiplier


def default_stats_path() -> Path:
    """Where the stats are kept unless --stats-file says otherwise."""
    return Path.home() / ".hangman_stats.json"


def load_stats(path: Path) -> Stats:
    """Read saved stats, starting fresh when the file is missing or unreadable."""
    try:
        data = json.loads(Path(path).read_text())
        # points came later, so files without it are still valid
        required = {key: int(data[key]) for key in asdict(Stats()) if key != "points"}
        return Stats(**required, points=int(data.get("points", 0)))
    except (OSError, ValueError, KeyError, TypeError):
        return Stats()


def save_stats(stats: Stats, path: Path) -> None:
    """Write the stats as JSON, creating the folder when needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(stats), indent=2) + "\n")
