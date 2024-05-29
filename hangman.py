#Step 5
import random
import hangman_art
import hangman_words
import os

def hangman():
    #Update the word list to use the 'word_list' from hangman_words.py
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    #Import the logo from hangman_art.py and print it at the start of the game.
    print(hangman_art.logo)
    #Testing code
    #print(f'Pssst, the solution is {chosen_word}.')

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        os.system('cls')
        
        if guess in display:
            print(f'You have already guessed {guess}')

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            '''print(
                f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
            )'''
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            print(
                f'The letter {guess} is not in the word. You lose a life, so you have {lives} lives left'
            )
        elif lives == 1:
            print(f'The letter {guess} is not in the word. You lose a life, so you have {lives} live left')
        elif lives == 0:
            end_of_game = True
            print("Game over :(")
            print(f'The word was {chosen_word}.')

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(hangman_art.stages[lives])
