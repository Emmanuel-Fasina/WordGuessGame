import tkinter as tk
import random


class WordGuessingGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Word Guessing Game")
        self.word_list = ["rainbow", "computer", "science", "programming", "python"]
        self.word = random.choice(self.word_list)
        self.turns = 12
        self.guess = ""

        self.label = tk.Label(window, text="Welcome to Emmanuel's Word Guessing Game", font="20")
        self.label.pack(pady=20)

        self.word_label = tk.Label(window, text="Guess the characters: " + " ".join(["*" for _ in self.word]), font="20")
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(window)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(window, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.turns_label = tk.Label(window, text=f"Turns left: {self.turns}")
        self.turns_label.pack(pady=10)

        self.message_label = tk.Label(window, text="")
        self.message_label.pack(pady=5)

    def update_word_display(self):
        displayed_word = [ch if ch in self.guess else "*" for ch in self.word]
        self.word_label.config(text="Guess the characters: " + " ".join(displayed_word))

    def check_guess(self):
        user_guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(user_guess) != 1 or not user_guess.isalpha():
            self.message_label.config(text="Please enter a single alphabetic character.")
            return

        if user_guess in self.guess:
            self.message_label.config(text="You've already guessed that character.")
            return

        self.guess += user_guess

        if user_guess not in self.word:
            self.turns -= 1
            self.message_label.config(text=f"Wrong guess! Turns left: {self.turns}")
            self.turns_label.config(text=f"Turns left: {self.turns}")
        else:
            self.message_label.config(text="Good guess!")

        self.update_word_display()

        if all(ch in self.guess for ch in self.word):
            self.message_label.config(text=f"You win! The word was: {self.word}")
            self.guess_button.config(state=tk.DISABLED)

        if self.turns == 0:
            self.message_label.config(text=f"You lose! The word was: {self.word}")
            self.guess_button.config(state=tk.DISABLED)


def main():
    window = tk.Tk()
    WordGuessingGame(window)
    window.mainloop()


main()
