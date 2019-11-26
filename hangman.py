"""A small command line Hangman game."""

import random

from gallows import gallows
from words import WORDS


def print_banner() -> None:
    """Show the welcome message and the rules of the game."""
    print(
        "**********************************WELCOME TO HANGMAN***************************************************"
    )
    print(
        "*                                                                                                     *"
    )
    print(
        "*                            SAMPLE EXAMPLE BY SAJAN POUDEL                                           *"
    )
    print(
        "*                                                                                                     *"
    )
    print(
        "*                                                                                                     *"
    )
    print(
        "*******************************************************************************************************"
    )
    print("\n\nYOU HAVE TO GUESS THE WORDS IN 3 attempts")


MAX_ATTEMPTS = 3
BLANK = "_"

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


def new_board(word: str | list[str]) -> list[str]:
    """Return a board of blanks as long as the word."""
    return [BLANK] * len(word)


def choose_word(words: list[str] = WORDS, rng: random.Random = random) -> str:
    """Pick the word for a round. A different rng makes the choice repeatable."""
    return rng.choice(words)


def play_round(chosen_word: str, ask=input, say=print, attempts: int = MAX_ATTEMPTS) -> bool:
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

        if not is_valid_guess(guess):
            say("Please enter a single letter.")
            continue

        if guess in guessed:
            say("You already tried '{}'.".format(guess))
            continue
        guessed.add(guess)

        if reveal_letter(guess, word, board) == 0:
            attempts_left -= 1
            say("Wrong Word. Try Again ({} left)\n".format(attempts_left))
            say(gallows(attempts - attempts_left, attempts))

        say(board)

    if board == word:
        say("YOUR GUESS {} WAS RIGHT: ".format(chosen_word))
        return True
    say("NEXT TRY!!! \n the correct answer was: {}".format(chosen_word))
    return False


def wants_another_round(ask=input) -> bool:
    """Ask the player whether to play again."""
    return ask("\nPlay again? (y/n) > ").strip().lower().startswith("y")


def main():
    """Play rounds until the player decides to stop."""
    while True:
        play_round(choose_word())
        if not wants_another_round():
            break


if __name__ == "__main__":
    print_banner()
    main()
