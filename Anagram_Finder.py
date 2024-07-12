from random import randrange
from time import time
from os import system

def is_anagram(word1, word2):
    backup1 = word1
    backup2 = word2
    if len(word1) != len(word2):
        return False
    for i in str(word1):
        if i not in str(word2):
            return False
        else:
            word2 = str(word2).replace(i,'',1)
    word1 = str(backup1)
    word2 = str(backup2)
    for i in str(word2):
        if i not in str(word1):
            return False
        else:
            word1 = str(word1).replace(i,'',1)
    return True

def return_to_char(ran, include):
    z = ''
    for i in range(ran):
        x = 0
        letter = randrange(65, 91)
        number = randrange(48, 58)
        if include != 'NO':
            if randrange(0,2) == 0:
                x = letter
            else:
                x = number
        else:
            x = letter
        y = str(chr(x))
        z = y + z
    return z

def get_user_input(prompt):
    user_input = input(prompt).upper()
    return ''.join(c for c in user_input if c.isalnum())

again = 'y'
times_peak = 1
word_scramble = ''
word1 = ''
word2 = ''
col = '\033[0;92m'

while again != 'n':
    system('cls')
    typed = get_user_input('Would you like to SEARCH for an anagram, TYPE an anagram, or SCRAMBLE a word? ')
    include = get_user_input('Include numbers? (Yes/No): ')
    system('cls')
    if typed == 'SEARCH':
        try:
            times_peak = int(input('\033[1mHow many anagrams do you want?'))
            size = int(input('\033[1mHow many letters?'))
            times = 0
        except:
            continue
    elif typed == 'TYPE':
        word1 = get_user_input('\033[1mType the first word: ')
        word2 = get_user_input('\033[1mType the second word: ')
        times = times_peak - 1 if 'times_peak' in locals() else 0
    elif typed == 'SCRAMBLE':
        try:
            word_scramble = get_user_input('\033[1mType the word: ')
            times_peak = int(input('\033[1mHow many anagrams do you want?'))
            times = 0
        except:
            continue
    else:
        continue

    total = 0
    same = 0

    def colora():
        if word1 == word2 or word_scramble == word2:
            col = '\033[0;94m'
        else:
            col = '\033[0;92m'
        return col

    start = time()
    print('\033[1m-' * 40)
    while times < times_peak:
        if typed == 'SEARCH':
            word1 = str(return_to_char(size,include))
            word2 = str(return_to_char(size,include))
        if typed != 'SCRAMBLE':
            if is_anagram(word1, word2) == True:
                col = colora()
                print(f'{col}{word1} | {word2}\033[0m')
                times += 1
            elif is_anagram(word1, word2) == False and typed == 'TYPE':
                print(f'\033[0;91m{word1} | {word2}\033[0m')
                times += 1
        elif typed == 'SCRAMBLE':
            word2 = str(return_to_char(len(word_scramble),include))
            col = colora()
            if is_anagram(word_scramble, word2) == True:
                print(f'{col}{word_scramble} | {word2}\033[0m')
                times += 1
        total += 1
        if word1 == word2 or word_scramble == word2:
            same += 1

    print('\033[1m-' * 40)
    start_end = time()
    print(f'\033[1mThe program searched {total} combinations')
    print(f'\033[1mThe program found {same} ({(same / total):%}) identical combination(s)')
    print(f'\033[1mThe program lasted for {(start_end - start):.2f} seconds')

    again = str(input('Would you like to repeat the program?\033[0m'))