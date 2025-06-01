import random

#  List of predefined words
word_list = ["apple", "tiger", "house", "robot", "chair"]

#  Randomly select one word
secret_word = random.choice(word_list)

#  Variables to track progress
guessed_letters = []
tries = 6

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time. You have 6 incorrect guesses.\n")

#  Game loop
while tries > 0:
    # Show the current guessed word with underscores for unguessed letters
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
    print("Word:", display_word)

    # Check for win
    if display_word == secret_word:
        print(" Congratulations! You guessed the word correctly.")
        break

    # Ask user for a letter
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only a single alphabet letter.\n")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter. Try a different one.\n")
        continue

    # Add guess to guessed_letters
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print(" Good guess!\n")
    else:
        tries -= 1
        print(f" Wrong guess. You have {tries} tries left.\n")

# a
# aa End of game
if display_word != secret_word:
    print(f"💀 Game Over! The word was: {secret_word}")

