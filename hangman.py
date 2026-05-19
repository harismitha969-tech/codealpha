import random
words = ["apple", "tiger", "pizza", "robot", "chair"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
display_word = ["_"] * len(secret_word)
print("Welcome to Hangman Game!")
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("⚠ You already guessed this letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("✅ Correct Guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\n Game Over! The word was:", secret_word)