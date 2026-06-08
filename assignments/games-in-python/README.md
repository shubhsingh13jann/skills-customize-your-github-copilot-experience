
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a terminal Hangman game that demonstrates string manipulation, loops, conditionals, and user input handling. The program should present a hidden word, accept letter guesses, and end with a clear win or lose outcome.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Use the provided `starter-code.py` as a starting point (if present) or build from scratch. The program should randomly choose a word, display progress with underscores for unguessed letters, accept single-letter guesses, and track remaining attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from an in-code list or a local data file.
- Accept single-letter guesses and ignore invalid or repeated entries.
- Display the current progress using underscores for unknown letters (e.g., `_ a _ g _ a _`).
- Track and display remaining incorrect attempts.
- End the game when the word is fully guessed or attempts are exhausted, showing a win/lose message and the correct word.
- Provide a `main()` entry so the assignment can be run with `python starter-code.py` or `python3 starter-code.py`.

#### Example

```bash
$ python starter-code.py
Welcome to Hangman!
Word: _ _ _ _ _
Guesses remaining: 6
Enter a letter: a
Good guess! Word: _ a _ _ _
```

---

If you need a starting scaffold, add a `starter-code.py` file in this folder and reference it from the README. Keep any sample data (if used) inside this assignment folder.
