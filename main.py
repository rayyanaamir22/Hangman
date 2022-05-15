'''
Name: Rayyan Aamir
Date: November 17, 2021
Program: Hangman (Game Design Club Project)
'''

# Modules
import os
import functions as f
from images import HANGMANPICS

missedLetters = ''
correctLetters = ''
gameIsDone = False

while True: 
  # This part is like the main menu: The game starts here, and the player may return to this page to switch the word category.
  print('H A N G M A N')
  # Player selects category from which the random word is drawn.
  f.wordCategory()
  # Game loop for chosen category begins.
  while True:
    os.system('clear')
    f.displayBoard(HANGMANPICS, missedLetters, correctLetters, f.secretWord)

    # Let the player type in a letter.
    guess = f.getGuess(missedLetters + correctLetters)

    if guess in f.secretWord:
        # The program must count the non-letter characters as filled out spaces
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(f.secretWord)):
            # Ignore non-letter characters when determining the amount of correct guesses
            if f.secretWord[i] not in f.spaces and f.secretWord[i] not in f.dashes and f.secretWord[i] not in f.apostrophes and f.secretWord[i] not in .colons:
              if f.secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            os.system('clear')
            f.winStreak += 1
            f.displayBoard(HANGMANPICS, missedLetters, correctLetters, f.secretWord)
            print('Yes! The secret word is "' + f.secretWord +
                  '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            os.system('clear')
            f.winStreak = 0
            f.displayBoard(HANGMANPICS, missedLetters, correctLetters,f.secretWord)
            # Inform user they have lost, and present the amount of correct and incorrect guesses
            # If the amount of correct guesses is 1, say "1 correct guess" instead of "1 correct guesses"
            if int(len(correctLetters)) != 1:
              print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + f.secretWord + '"')
            elif int(len(correctLetters)) == 1:
              print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guess, the word was "' + f.secretWord + '"')
            else:
              continue

            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if f.playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            # If the player wants to do the same category again, select another random word from the current category
            f.nextSecretWord()
        else: 
          break

  # Ask the player if they want to return to main menu
  if not f.changeCategory():
    # If the user wants to exit the entire program, the loop breaks here
    os.system('clear')
    print('Thanks for playing!')
    break
  else:
    os.system('clear') # Refresh before next iteration
    
    # Reset the key values for next iteration
    missedLetters = ''
    correctLetters = ''
    gameIsDone = False

    # If user says yes to changing the game category and playing again, continue to the next iteration of the loop
    continue

# End of game


'''
IDEAS:
- Allow the user to create their own category and save it using SQL
'''
