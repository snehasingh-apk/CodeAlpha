import random

# Predefined word list
word_list = ["apple", "robot", "house", "light", "brain"]
secret_word = random.choice(word_list)

# Game setup
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))  # Initial blank word display

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempts left.")

    # Display the current state of the word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check win
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break

# If loop exits and user hasn't won
if attempts == 0:
    print("💀 Game over! The word was:", secret_word)
