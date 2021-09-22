# How the code is organised

| File | Role |
| --- | --- |
| `hangman.py` | Game rules, `play_round()` and the command line entry point |
| `words.py` | Word list, categories, `words_for()` and `load_words()` |
| `gallows.py` | ASCII drawings for the gallows |
| `scores.py` | `Stats` for wins, losses and streaks, plus JSON load and save |
| `colors.py` | `paint()` for ANSI colours |

`play_round()` takes `ask` and `say` functions, so tests can play a whole round without a keyboard.
