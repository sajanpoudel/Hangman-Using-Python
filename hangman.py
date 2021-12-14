"""A small command line Hangman game."""

import argparse
import random
import sys
from pathlib import Path

from colors import paint
from gallows import gallows
from scores import default_stats_path, load_stats, save_stats
from words import WORDS, load_words, words_for

BANNER_WIDTH = 103


def banner_lines(width: int = BANNER_WIDTH) -> list[str]:
    """Build the welcome box with every line of text centred between the borders."""
    inner = width - 2
    rows = ["WELCOME TO HANGMAN", "", "SAMPLE EXAMPLE BY SAJAN POUDEL", ""]
    border = "*" * width
    return [border] + ["*" + row.center(inner) + "*" for row in rows] + [border]


def print_banner(attempts: int = 3) -> None:
    """Show the welcome message and the rules of the game."""
    print("\n".join(banner_lines()))
    print(f"\n\nYOU HAVE TO GUESS THE WORDS IN {attempts} attempts")


MAX_ATTEMPTS = 3
BLANK = "_"
HINT_COMMAND = "?"

# Attempts allowed for each difficulty level.
DIFFICULTIES = {"easy": 8, "normal": 6, "hard": 3}


def reveal_letter(guess: str, word: list[str], board: list[str]) -> int:
    """Fill in every position of the board that matches the guess.

    Returns the number of positions that were revealed.
    """
    revealed = 0
    for position, letter in enumerate(word):
        if letter == guess:
            board[position] = guess
            revealed += 1
    return revealed


def normalize_guess(text: str) -> str:
    """Lowercase the guess and drop the spaces around it."""
    return text.strip().lower()


def is_valid_guess(guess: str) -> bool:
    """A guess is valid when it is a single letter."""
    return len(guess) == 1 and guess.isalpha()


def attempts_for(difficulty: str) -> int:
    """Return the attempts for a difficulty level (unknown names count as normal)."""
    return DIFFICULTIES.get(difficulty.lower(), DIFFICULTIES["normal"])


def hidden_positions(word: list[str], board: list[str]) -> list[int]:
    """Positions on the board that are still blank."""
    return [i for i, shown in enumerate(board) if shown == BLANK]


def pick_hint(word: list[str], board: list[str], rng: random.Random = random) -> str | None:
    """Choose a letter that is still hidden, or None when everything is shown."""
    positions = hidden_positions(word, board)
    if not positions:
        return None
    return word[rng.choice(positions)]


def new_board(word: str | list[str]) -> list[str]:
    """Return a board of blanks as long as the word."""
    return [BLANK] * len(word)


def choose_word(words: list[str] = WORDS, rng: random.Random = random) -> str:
    """Pick the word for a round. A different rng makes the choice repeatable."""
    return rng.choice(words)


def play_round(
    chosen_word: str, ask=input, say=print, attempts: int = MAX_ATTEMPTS, color: bool = False
) -> bool:
    """Run one round for chosen_word and return True when the player wins.

    ask and say can be replaced, which makes the round testable without a keyboard.
    """
    word = list(chosen_word)
    board = new_board(word)

    say(board)  # show the empty board first

    attempts_left = attempts
    guessed = set()

    while attempts_left > 0 and board != word:
        guess = normalize_guess(ask("\nPLEASE GUESS THE WORD > "))

        if guess == HINT_COMMAND:
            if attempts_left <= 1:
                say("No hints on your last attempt.")
                continue
            hint = pick_hint(word, board)
            attempts_left -= 1
            guessed.add(hint)
            reveal_letter(hint, word, board)
            say(f"Hint: '{hint}' ({attempts_left} left)")
            say(board)
            continue

        if len(guess) > 1 and guess.isalpha():
            if guess == chosen_word:
                board[:] = word
                break
            attempts_left -= 1
            say(paint(f"'{guess}' is not the word ({attempts_left} left)\n", "red", color))
            say(gallows(attempts - attempts_left, attempts))
            continue

        if not is_valid_guess(guess):
            say("Please enter a single letter or the whole word.")
            continue

        if guess in guessed:
            say(f"You already tried '{guess}'.")
            continue
        guessed.add(guess)

        if reveal_letter(guess, word, board) == 0:
            attempts_left -= 1
            say(paint(f"Wrong Word. Try Again ({attempts_left} left)\n", "red", color))
            say(gallows(attempts - attempts_left, attempts))

        say(board)
        if guessed:
            say("Tried: {}".format(" ".join(sorted(guessed))))

    if board == word:
        say(paint(f"YOUR GUESS {chosen_word} WAS RIGHT: ", "green", color))
        return True
    say(paint(f"NEXT TRY!!! \n the correct answer was: {chosen_word}", "yellow", color))
    return False


def wants_another_round(ask=input) -> bool:
    """Ask the player whether to play again."""
    return ask("\nPlay again? (y/n) > ").strip().lower().startswith("y")


def build_parser() -> argparse.ArgumentParser:
    """Command line options of the game."""
    parser = argparse.ArgumentParser(description="Play Hangman in the terminal.")
    parser.add_argument("--difficulty", default="normal", help="easy, normal or hard")
    parser.add_argument(
        "--attempts", type=int, help="wrong guesses allowed (overrides the difficulty)"
    )
    parser.add_argument("--category", help="animals, places, nature or school")
    parser.add_argument("--words-file", help="text file with one word per line")
    parser.add_argument("--seed", type=int, help="seed for the random word choice")
    parser.add_argument("--stats-file", help="where wins and losses are kept between sessions")
    parser.add_argument("--no-color", action="store_true", help="turn off coloured output")
    return parser


def resolve_attempts(args: argparse.Namespace) -> int:
    """--attempts wins over --difficulty, and the result is never below one."""
    attempts = args.attempts if args.attempts is not None else attempts_for(args.difficulty)
    return max(1, attempts)


def resolve_words(args: argparse.Namespace) -> list[str]:
    """Words from --words-file, else from --category, else the full list."""
    if args.words_file:
        words = load_words(args.words_file)
        if words:
            return words
    return words_for(args.category)


def main(argv: list[str] | None = None) -> None:
    """Play rounds until the player decides to stop."""
    args = build_parser().parse_args(argv)
    rng = random.Random(args.seed) if args.seed is not None else random
    attempts = resolve_attempts(args)
    words = resolve_words(args)
    use_color = not args.no_color and sys.stdout.isatty()
    stats_path = Path(args.stats_file) if args.stats_file else default_stats_path()
    stats = load_stats(stats_path)
    print_banner(attempts)
    while True:
        won = play_round(choose_word(words, rng), attempts=attempts, color=use_color)
        stats.record(won)
        save_stats(stats, stats_path)
        print(stats.summary())
        if not wants_another_round():
            break


if __name__ == "__main__":
    main()
