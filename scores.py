"""Win and loss bookkeeping for a session."""

from dataclasses import dataclass


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
