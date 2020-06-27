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

    @property
    def played(self) -> int:
        """Number of rounds played."""
        return self.wins + self.losses

    def record(self, won: bool) -> None:
        """Add the result of one round."""
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
        return "Won {} of {} ({:.0%}), streak {}, best streak {}".format(
            self.wins, self.played, self.win_rate(), self.streak, self.best_streak
        )


def load_stats(path: Path) -> Stats:
    """Read saved stats, starting fresh when the file is missing or unreadable."""
    try:
        data = json.loads(Path(path).read_text())
        return Stats(**{key: int(data[key]) for key in asdict(Stats())})
    except (OSError, ValueError, KeyError, TypeError):
        return Stats()


def save_stats(stats: Stats, path: Path) -> None:
    """Write the stats as JSON, creating the folder when needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(stats), indent=2) + "\n")
