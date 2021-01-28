import random
from random_words import RandomWords
rw = RandomWords()

drawing = ['''
    +---+
        |
        |
        |
   =====''', '''
    +---+
    O   |
        |
        |
   =====''', '''
    +---+
    O   |
    |   |
        |
   =====''', '''
    +---+
    O   |
   /|   |
        |
   =====''', '''
    +---+
    O   |
   /|\  |
        |
   =====''', '''
    +---+
    O   |
   /|\  |
   /    |
   =====''', '''
    +---+
    O   |
   /|\  |
   / \  |
   =====''']

def display(missed_letters, correct_letters, word):
    print(drawing[len(missed_letters)]); print(''); print('failed attempts:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print(''); blank_letters = '_' * len(word)
    for i in range(len(word)): 
        if word[i] in correct_letters:
            blank_letters = blank_letters[:i] + word[i] + blank_letters[i+1:]
    for letter in blank_letters: 
        print(letter, end=' ')
    print('')

def guesser(guessed):
    while True:
        print('guess if you dare...'); guess = input(); guess = guess.lower()
        if len(guess) != 1:
            print('just one letter')
        elif guess in guessed:
            print('guess a new letter')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('guess a LETTER')
        else:
            return guess

def restart():
    print('Want to try again?')
    return input().startswith('y')


def main():
    print('Lets play: HANGMAN')
    missed_letters = ''; correct_letters = ''; word = rw.random_word(); finished = False
    while True:
        display(missed_letters, correct_letters, word); guess = guesser(missed_letters + correct_letters)
        if guess in word:
            correct_letters = correct_letters + guess
            won = True
            for i in range(len(word)):
                if word[i] not in correct_letters:
                    won = False; break
            if won:
                print('Congrats, you saved them!'); finished = True
        else:
            missed_letters = missed_letters + guess
            if len(missed_letters) == len(drawing) - 1:
                display(missed_letters, correct_letters, word); print('Oof, you lost. BTW the word was '+word); finished = True

        if finished:
            if restart():
                missed_letters = ''; correct_letters = ''; finished = False; word = rw.random_word()
            else:
                break

if __name__ == "__main__":
	main()