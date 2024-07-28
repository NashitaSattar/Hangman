import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6

end_of_geme = False

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

display = []

for letter in chosen_word:
    display.append("_")

print(hangman_art.stages[lives])
print(display)

while not end_of_geme: #part of game that is repated

    guess = input("Guess a letter: ").lower()

    if guess in display: #Check if guess has already been guessed
            print(f"You have already guessed {guess}")
            


    for position in range(len(chosen_word)): #Fill in blanks for right guess
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            

    if guess not in chosen_word: #Check if guess is not in chosen word
            lives -= 1
            print(f"{guess} is not in the word. You lose a life.")
            

            if lives == 0:
                end_of_games = True
                print("You Lose!")


    if "_" not in display: #Check if user has won
        end_of_geme = True
        print("You Won!" )

    print(hangman_art.stages[lives])

  
