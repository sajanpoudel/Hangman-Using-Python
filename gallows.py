"""ASCII art for the hangman gallows."""

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def gallows(wrong: int, allowed: int) -> str:
    """Return the drawing for `wrong` misses out of `allowed` attempts.

    The drawing is scaled so the last stage appears exactly when the attempts run out.
    """
    if allowed <= 0:
        return STAGES[-1]
    wrong = max(0, min(wrong, allowed))
    index = round(wrong / allowed * (len(STAGES) - 1))
    return STAGES[index]
