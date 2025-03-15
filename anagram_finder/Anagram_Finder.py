from random import randrange
from os import system
from msvcrt import getch

def search(letter,times,number):
    alpha = []

    for i in range(26):
        alpha.append(chr(65 + i))
    if number.upper() == 'YES':
        for i in range(10):
            alpha.append(chr(48 + i))
        
    for i in range(times):
        full_word = ''

        for j in range(letter):
            full_word += alpha[randrange(len(alpha))]

        scramble(full_word,1)

def scramble(full_word,times):
    for i in range(times):
        final_word = ''
        word = []
        used = []
        while len(word) != len(full_word):
            number = randrange(0, len(full_word))
            if number not in used:
                used.append(number)
                word.append(full_word[number])
    
        for i in range(len(word)):
            final_word += word[i]
            
        if final_word == full_word:
            color = '\033[92m'
        else:
            color = '\033[91m'

        print(color + full_word + ' | ' + final_word)

def typed(word1,word2):
    if len(word1) != len(word2):
        print('NOT ENOUGH LETTERS!')
        return

    counter = 0
    correct = 0
    while counter < len(word1):
        for i in range(len(word1)):
            if word1[i] == word2[counter]:
                correct += 1
        counter += 1

    if correct == len(word1):
        print('\033[92m' + 'CORRECT!\n' + word1 + ' | ' + word2 + '\nIS AN ANAGRAM')
    else:
        print('\033[91m' + 'INCORRECT!\n' + word1 + ' | ' + word2 + '\nIS NOT AN ANAGRAM')

while True:
    opt = str(input('\033[0mWHAT TO DO?:\n1-SEARCH\n2-SCRAMBLE\n3-TYPE\n'))
    system('cls')

    match opt:
        case '1':
            letter = int(input('HOW MANY LETTERS?: '))
            number = str(input('INCLUDE NUMBERS?\n'))
            times = int(input('HOW MANY TIMES?\n'))

            search(letter,times,number)
        case '2':
            full_word = str(input('SCRAMBLE: '))
            times = int(input('HOW MANY TIMES?\n'))

            scramble(full_word,times)
        case '3':
            first_word = str(input('FIRST WORD: '))
            second_word = str(input('SECOND WORD: '))

            typed(first_word,second_word)
        case _:
            continue

    getch()
    system('cls')