# Word Guessing Game

A simple word guessing game built with Python and Tkinter. Guess the letters of a hidden word within a limited number of turns to win!

## Features

- Graphical user interface using Tkinter
- Random word selection from a predefined list
- 12 turns to guess the word
- Real-time feedback on guesses
- Win/lose detection

## Requirements

- Python 3.11+
- Tkinter (included with Python standard library)

## How to Run

1. Ensure Python 3.x is installed on your system.
2. Navigate to the project directory.
3. Run the game with: `python main.py`

## How to Play

1. The game selects a random word from the list: rainbow, computer, science, programming, python.
2. Guess one letter at a time by typing it in the input field and clicking "Guess".
3. Correct guesses reveal the letter in the word display.
4. Incorrect guesses reduce your remaining turns.
5. Win by guessing all letters before running out of turns.
6. Lose if you exhaust all 12 turns without guessing the word.

## Game Rules

- Only single alphabetic characters are accepted.
- Duplicate guesses are not allowed.
- The game ends when you win or lose, disabling further guesses.

## Author

Emmanuel

Enjoy the game!