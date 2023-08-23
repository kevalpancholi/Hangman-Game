# Hangman game

import random
import string

# Change the location of WORDLIST_FILENAME to where you save 'words.txt' file
# Filepath can be found by dragging 'words.txt' to your terminal/command line
WORDLIST_FILENAME = "/Users/kevalpancholi/Documents/words.txt"

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


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    totalGuessed = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            totalGuessed += 1
    if totalGuessed == len(secretWord):
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
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessedWord = secretWord.replace(letter, '_')
            secretWord = guessedWord
        else:
            guessedWord = secretWord
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    # Python compares two lists by going through the lists at the same index
    # therfore, if you want to manipulate lists clone them so that the change in length
    # does not affect what you are trying to do
    alphabet_copy = alphabet[:]
    for char in alphabet_copy:
        if char in lettersGuessed:
            alphabet.remove(char)
    return ''.join(alphabet)

    

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    num_guess = 8
    lettersGuessed = []
    while num_guess != 0:
        print('_____________________________________________\n')
        print ('You have ' + str(num_guess) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        userGuess = input('Please guess a letter: ').lower()
        if userGuess not in lettersGuessed:
            lettersGuessed.append(userGuess)
            if userGuess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                num_guess -= 1 
        else:
            print('Oops! You have already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed):
            break

    if num_guess == 0:
        print ('Sorry you ran out of guesses. The word was '+ str(secretWord))
    else:
        print ('Congratulations, you won!\n')    
    


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)