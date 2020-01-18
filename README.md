# Hangman-Using-Python

A simple command line hangman game written in Python. A random word is picked
and you guess one letter at a time. You have three wrong guesses before the
round ends.

## Run

```
python3 hangman.py
```

No third party packages are needed.

## How it works

- `WORDS` holds the words the game can choose from.
- `reveal_letter()` fills the board with every position that matches a guess.
- `MAX_ATTEMPTS` controls how many wrong guesses are allowed.

By Sajan Poudel.
