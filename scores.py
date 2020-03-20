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
