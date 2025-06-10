import tkinter as tk
from tkinter import messagebox
import random

# Word list
word_list = ["apple", "robot", "house", "light", "brain"]
secret_word = random.choice(word_list)
guessed_letters = set()
attempts_left = 6

def update_display():
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    word_label.config(text=display_word)
    attempts_label.config(text=f"Attempts Left: {attempts_left}")

def guess_letter():
    global attempts_left
    guess = entry.get().lower()
    entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Repeated", f"You already guessed '{guess}'")
        return

    guessed_letters.add(guess)

    if guess not in secret_word:
        attempts_left -= 1

    update_display()

    if all(letter in guessed_letters for letter in secret_word):
        messagebox.showinfo("🎉 You Win!", f"The word was '{secret_word}'")
        root.destroy()

    elif attempts_left == 0:
        messagebox.showinfo("💀 Game Over", f"You ran out of attempts! The word was '{secret_word}'")
        root.destroy()

# GUI setup
root = tk.Tk()
root.title("Hangman Game")

word_label = tk.Label(root, text="_ " * len(secret_word), font=("Helvetica", 24))
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts Left: {attempts_left}", font=("Helvetica", 14))
attempts_label.pack()

update_display()
root.mainloop()
