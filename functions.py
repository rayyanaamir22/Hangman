# FUNCTIONS

# Modules
import random
import os

# Other files
import categories as c

def wordCategory():
  # This function runs at the start of the program. The user must choose a category from which the secret word will be selected.
  global category
  category = ''
  print('\nAnimals | Science | Math | Computer Science | Sports | Movies | Movie Characters | TV Shows | Random | Custom')
  while category not in ['ANIMALS', 'SCIENCE', 'MATH', 'COMPUTER SCIENCE', 'SPORTS', 'MOVIES', 'MOVIE CHARACTERS', 'TV SHOWS', 'RANDOM', 'CUSTOM']:
    print('Select a category')
    category = input().upper()
  

def getSecretWord():
  global secretWord
  temp = secretWord # Previous secretWord
  
  # Ensure the secreWord is different from the previous one
  while secretWord == temp:
    if category == 'ANIMALS':
      secretWord = getRandomWord(c.animals)
    elif category == 'SCIENCE':
      secretWord = getRandomWord(c.science)
    elif category == 'MATH':
      secretWord = getRandomWord(c.math)
    elif category == 'COMPUTER SCIENCE':
      secretWord = getRandomWord(c.compSci)
    elif category == 'SPORTS':
      secretWord = getRandomWord(c.sports)
    elif category == 'MOVIES':
      secretWord = getRandomWord(c.movies)
    elif category == 'MOVIE CHARACTERS':
      secretWord = getRandomWord(c.movieCharacters)
    elif category == 'TV SHOWS':
      secretWord = getRandomWord(c.tvShows)
    elif category == 'RANDOM':
      secretWord = getRandomWord(c.randomCategory)
    elif category == 'CUSTOM':
      secretWord = getRandomWord(c.customCategory)
    else: 
      return None


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    # Make sure to subtract 1 because indexing begins at zero
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

global winStreak
winStreak = 0

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    # This allows the program to print the correct hangman picture based on the amount of incorrect guesses from the player.

    print('Category: ' + category)
    #print(category).centre(width)
    print(f'Win streak: {winStreak}')
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    # Determine the amount of letters in the secret word and print that amount of blank spaces
    # If the secret word contains any characters that are not letters (space, dash, colon, apostrophe), they must be accounted for.
    blanks = '_' * len(secretWord)

    # Assign non-letter characters as global variables
    global spaces
    global dashes
    global colons
    global apostrophes
    spaces = ' '  
    dashes = '-'
    colons = ':'
    apostrophes = '\''

    # When displaying the word, give any correctly guessed letters or special characters to the user, since they do not have to guess those letters.
    for i in range(len(secretWord)):  
      # Letters
      if secretWord[i] in correctLetters:
        # Maintain blank spaces before and after the correctly guessed letter, but replace the correct blank with the letter.
        blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
      # Spaces
      if secretWord[i] in spaces:
        blanks = blanks[:i] + secretWord[i] + blanks[i +1:]
      # Dashes
      if secretWord[i] in dashes:
        blanks = blanks[:i] + secretWord[i] + blanks[i +1:]
      # Colons
      if secretWord[i] in colons:
        blanks = blanks[:i] + secretWord[i] + blanks[i +1:]
      # Apostrophes
      if secretWord[i] in apostrophes:
        blanks = blanks[:i] + secretWord[i] + blanks[i +1:]



    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.

    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    # To restart the game, the player must enter anything that starts with the letter Y

    print('Do you want to play in this category again? (yes or no)')
    
    while True:
      playAgain = input()
      if playAgain.lower().startswith('y'):
        return True
      elif playAgain.lower().startswith('n'):
        return False
      else:
        print('Invalid input')

def changeCategory():
  # This function asks the player if they want to change their word category or exit the game entirely
  os.system('clear')
  while True:
    print('Return to main menu? (yes or no)')
    diff = input()
    if diff.lower().startswith('y'):
      return True
    elif diff.lower().startswith('n'):
      return False
    else: 
      print('Invalid input')
  # Code block at the end of the game loop comprehends the returned value and breaks or continues the loop.
