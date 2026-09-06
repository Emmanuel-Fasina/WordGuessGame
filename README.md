# Word Guessing Game

A Tkinter-based GUI word guessing game where players guess the letters of a randomly selected hidden word within 12 turns, with real-time feedback and win/lose detection.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Project Structure](#project-structure)
- [License](#license)

## Overview
Word Guessing Game is a classic hangman-style game: the app randomly selects a hidden word from a predefined list, and the player tries to reveal it one letter at a time before running out of turns.

## Features
- 🖥️ Graphical interface built with Tkinter
- 🎲 Random word selection from a predefined word list
- ⏳ 12 turns to guess the full word
- ⚡ Real-time feedback on each guess
- 🏆 Automatic win/lose detection

## Installation
```bash
git clone https://github.com/Emmanuel-Fasina/WordGuessGame.git
cd WordGuessGame
```
Requires Python 3.11+ with Tkinter (included in most standard installs).

## How to Play
```bash
python main.py
```
1. The game randomly selects a hidden word (e.g. from: `rainbow`, `computer`, `science`, `programming`, `python`).
2. Type a single letter into the input field and click **Guess**.
3. Correct guesses reveal that letter in the word display.
4. Incorrect guesses reduce your remaining turns.
5. Guess the full word before your turns run out to win.

## Game Rules
- Only single alphabetic characters are accepted per guess.
- Duplicate guesses of the same letter are not allowed.
- The game ends — win or lose — and disables further guesses once decided.

## Project Structure
```
WordGuessGame/
├── main.py       # Game logic and GUI
└── README.md     # Project documentation
```

## License
This project was built for educational and learning purposes.

---
Built by [Emmanuel Fasina](https://github.com/Emmanuel-Fasina)
