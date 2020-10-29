"""Small helpers for coloured terminal output."""

RESET = "\033[0m"
CODES = {"red": "\033[31m", "green": "\033[32m", "yellow": "\033[33m", "bold": "\033[1m"}


def paint(text: str, color: str, enabled: bool = True) -> str:
    """Wrap text in an ANSI colour. Returns the text unchanged when disabled or unknown."""
    if not enabled or color not in CODES:
        return text
    return f"{CODES[color]}{text}{RESET}"
