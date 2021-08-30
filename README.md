# Hangman-Using-Python

A simple command line hangman game written in Python. A random word is picked
and you guess one letter at a time. You have three wrong guesses before the
round ends.

## Run

```
python3 hangman.py
```

No third party packages are needed.

## Tests

```
pip install -r requirements-dev.txt
pytest
```

## How it works

- `WORDS` holds the words the game can choose from.
- `reveal_letter()` fills the board with every position that matches a guess.
- `MAX_ATTEMPTS` controls how many wrong guesses are allowed.
- `play_round()` runs one round and takes replaceable input and output functions, which the tests use.
- `words.py` holds the word list.

## Rules

- A random word is chosen and shown as blanks.
- Type one letter per turn. Correct letters are revealed everywhere they appear.
- A wrong letter costs one of your three attempts. Repeated letters and invalid input are free.
- After a round you can choose to play again.

By Sajan Poudel.

## Options

```
python3 hangman.py [--difficulty easy|normal|hard] [--attempts N]
                   [--category NAME] [--words-file PATH]
                   [--seed N] [--no-color]
```

### Difficulty

| Level | Wrong guesses allowed |
| --- | --- |
| easy | 8 |
| normal | 6 |
| hard | 3 |

`--attempts N` overrides the level and is never lower than 1.

### Categories

`--category` accepts `animals`, `places`, `nature` or `school`. Any other name uses the full list. Use `--words-file words.txt` to play with your own words, one per line. Lines with digits or symbols are ignored.
