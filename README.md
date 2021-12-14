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
                   [--min-length N] [--max-length N]
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

`--category` accepts `animals`, `places`, `nature`, `school`, `technology` or `food`. `--list-categories` prints them with the number of words. Any other name uses the full list. Use `--words-file words.txt` to play with your own words, one per line. Lines with digits or symbols are ignored.

### Guessing the whole word

Type the full word instead of a letter. A correct guess wins the round at once, a wrong one costs an attempt.

### Word length

`--min-length 6` and `--max-length 9` keep only words with that many letters. If no word fits, the game falls back to the full list.

### Hints

Type `?` to reveal a random hidden letter. A hint costs one attempt and is not available on your last attempt.

### Points

A won round earns ten points per letter, doubled with up to six attempts and tripled with three or fewer. The total is part of the saved statistics.

### Statistics

Wins, losses and streaks are saved to `~/.hangman_stats.json` after every round. Use `--stats-file PATH` to keep them somewhere else, and `--show-stats` to print them without playing.

### Repeatable games

`--seed 7` always starts with the same word, which is handy when you want to show the game to someone else.

## More documentation

- [Architecture](docs/architecture.md)
- [Testing](docs/testing.md)
- [Changelog](docs/changelog.md)
