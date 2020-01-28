"""A small command line Hangman game."""

import string
import random

WORDS = [
    "cres",
    "adult",
    "advice",
    "arrangement",
    "attempt",
    "august",
    "autumn",
    "border",
    "breeze",
    "brick",
    "calm",
    "canal",
    "casey",
    "cast",
    "chose",
    "claws",
    "coach",
    "constantly",
    "contrast",
    "cookies",
    "customs",
    "damage",
    "danny",
    "deeply",
    "depth",
    "discussion",
    "doll",
    "donkey",
    "egypt",
    "ellen",
    "essential",
    "exchange",
    "exist",
    "explanation",
    "facing",
    "film",
    "finest",
    "fireplace",
    "floating",
    "folks",
    "fort",
    "garage",
    "grabbed",
    "grandmother",
    "habit",
    "happily",
    "harry",
    "heading",
    "hunter",
    "illinois",
    "image",
    "independent",
    "instant",
    "January",
    "kids",
    "label",
    "lee",
    "lungs",
    "manufacturing",
    "Martin",
    "mathematics",
    "melted",
    "memory",
    "mill",
    "mission",
    "monkey",
    "mount",
    "mysterious",
    "neighborhood",
    "norway",
    "nuts",
    "occasionally",
    "official",
    "ourselves",
    "palace",
    "pennsylvania",
    "philadelphia",
    "plates",
    "poetry",
    "policeman",
    "positive",
    "possibly",
    "practical",
    "pride",
    "promised",
    "recall",
    "relationship",
    "remarkable",
    "require",
    "rhyme",
    "rocky",
    "rubbed",
    "rush",
    "sale",
    "satellites",
    "satisfied",
    "scared",
    "selection",
    "shake",
    "shaking",
    "shallow",
    "shout",
    "silly",
    "simplest",
    "slight",
    "slip",
    "slope",
    "soap",
    "solar",
    "species",
    "spin",
    "stiff",
    "swung",
    "tales",
    "thumb",
    "tobacco",
    "toy",
    "trap",
    "treated",
    "tune",
    "university",
    "vapor",
    "vessels",
    "wealth",
    "wolf",
    "zoo",
]


def print_banner():
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


def reveal_letter(guess, word, board):
    """Fill in every position of the board that matches the guess.

    Returns the number of positions that were revealed.
    """
    revealed = 0
    for position, letter in enumerate(word):
        if letter == guess:
            board[position] = guess
            revealed += 1
    return revealed


def normalize_guess(text):
    """Lowercase the guess and drop the spaces around it."""
    return text.strip().lower()


def is_valid_guess(guess):
    """A guess is valid when it is a single letter."""
    return len(guess) == 1 and guess.isalpha()


def new_board(word):
    """Return a board of blanks as long as the word."""
    return [BLANK] * len(word)


def choose_word(words=WORDS, rng=random):
    """Pick the word for a round. A different rng makes the choice repeatable."""
    return rng.choice(words)


def main():
    """Play one round: pick a random word and let the player guess letters."""
    chosen_word = choose_word()
    word = list(chosen_word)
    board = new_board(word)

    print(board)  # show the empty board first

    attempts_left = MAX_ATTEMPTS

    while attempts_left > 0 and board != word:
        guess = input("\nPLEASE GUESS THE WORD > ")

        if reveal_letter(guess, word, board) == 0:
            attempts_left -= 1
            print("Wrong Word. Try Again \n")

        print(board)

    if board == word:
        print("YOUR GUESS {} WAS RIGHT: ".format(chosen_word))
    else:
        print("NEXT TRY!!! \n the correct answer was: {}".format(chosen_word))


if __name__ == "__main__":
    print_banner()
    main()
