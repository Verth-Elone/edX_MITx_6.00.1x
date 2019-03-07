# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord: str, lettersGuessed: list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in lettersGuessed:
        secretWord = secretWord.replace(char, '')
    if len(secretWord) == 0:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    if guessed_word[-1] == ' ':
        guessed_word = guessed_word[0:-1]
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    not_used_letters = string.ascii_lowercase
    for letter in lettersGuessed:
        not_used_letters = not_used_letters.replace(letter, '')
    return not_used_letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    word_so_far = getGuessedWord(secretWord, letters_guessed)
    number_of_guesses = 8
    incorrect_guesses = 0
    game_in_progress = True
    while game_in_progress:
        print('-------------')
        print(f'You have {number_of_guesses} guesses left.')
        print(f'Available letters: {getAvailableLetters(letters_guessed)}')
        guess = input('Please guess a letter: ').lower()
        if len(guess) != 1:
            print('Wrong number of characters! Make sure that you guess just one letter.')
        elif guess not in string.ascii_lowercase:
            print('Wrong character! Use letters from English standard alphabet.')
        elif guess in letters_guessed:
            print(f'Oops! You\'ve already guessed that letter: {word_so_far}')
        else:
            letters_guessed.append(guess)
            word_after_this_guess = getGuessedWord(secretWord, letters_guessed)
            if word_so_far == word_after_this_guess:
                incorrect_guesses += 1
                number_of_guesses -= 1
                print(f'Oops! That letter is not in my word: {word_so_far}')
            else:
                word_so_far = word_after_this_guess
                print(f'Good guess: {word_so_far}')
        if word_so_far == secretWord:
            print('-------------')
            print('Congratulations, you won!')
            game_in_progress = False
        elif number_of_guesses < 1:
            print('-------------')
            print('Sorry, you ran out of guesses. The word was else.')
            game_in_progress = False




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
