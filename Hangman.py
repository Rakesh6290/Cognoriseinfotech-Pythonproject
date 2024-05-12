import random

word_list = ["india", "america", "island", "australia", "pakistan", "china", "brazil", "france", "japan"]

def select_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    print("Welcome to Hangman!")
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 5
    
    while incorrect_guesses < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_attempts - incorrect_guesses, "attempts left.")
        else:
            print("Correct guess!")
        
        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break
    
    if incorrect_guesses == max_attempts:
        print("You've run out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing Hangman!")

hangman()
