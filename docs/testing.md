# Testing

```
pip install -r requirements-dev.txt
pytest
```

Tests are grouped by module: `test_hangman.py` for the rules, `test_gallows.py`, `test_words.py`, `test_scores.py`, `test_colors.py` and `test_cli.py` for the options. A fake keyboard (`fake_io` in `test_hangman.py`) feeds scripted guesses to `play_round()`.
