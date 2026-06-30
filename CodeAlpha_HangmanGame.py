import random

WORDS = ["python", "hangman", "computer", "elephant", "guitar"]
MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {MAX_WRONG_GUESSES} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            wrong_guesses += 1
            print(f"Wrong guess! ({wrong_guesses}/{MAX_WRONG_GUESSES})\n")

    else:
        # Loop ended because wrong_guesses reached the max (while-else)
        print(f"\nGame over! You've used all {MAX_WRONG_GUESSES} incorrect guesses.")
        print(f"The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()