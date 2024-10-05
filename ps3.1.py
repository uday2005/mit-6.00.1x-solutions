import string 
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r') # open file in read
    # line: string
    line = inFile.readline() 
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = loadWords()

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord,lettersGuessed):
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter

    if word == secretWord:
        return True
    else:
        return False


def getWordGuessed(secretWord,lettersGuessed):
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess += "_ "

    return guess
    
def getAvailableLetters(lettersGuessed):
    all = "abcdefghijklmnopqrstuvwxyz"
    available = ""
    # for letter in all:
    #     if letter in lettersGuessed:
    #         all = all.replace(lettersGuessed,"")
    #     return all

    # for letter in lettersGuessed:
    #     all = all.replace(letter,"")  # to replace the  letetr we need the string not the list what i was doing up
    # return all

    for letter in all:    
        if letter not in lettersGuessed:
                available += letter
    return available

secretWord = chooseWord(wordlist).lower()
def hangman(secretWord):
    
    secretWord = chooseWord(wordlist).lower()

    print(f"Given the number of letter in words {len(secretWord)}")
    print("------------------------------")
    guess_left = 8
    
    lettersGuessed =""
    while True:
        
        print("you have now " + str(guess_left) + "left")
        print("Available Letters:",getAvailableLetters(lettersGuessed))
        guess = input("what is your letter : ")

        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print("Good guess:" ,getWordGuessed(secretWord,lettersGuessed))
        elif guess in lettersGuessed:
            print("we already have these",getWordGuessed(secretWord,lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Oops! That letter is not in my word: " , getWordGuessed(secretWord, lettersGuessed))
        guess_left -= 1
        print ("------------")




        if guess_left <0:
            print("oops you ran out of guesses " + "word is : " + secretWord + ".")
            break
        if isWordGuessed (secretWord,lettersGuessed):
            print("perfect:" + "your answer is " + secretWord + "." )
            break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)