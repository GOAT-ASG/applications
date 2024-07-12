    # ROAD GAME by Adrian

    # Bibliotecas
import random
import time
from threading import Thread
from threading import Timer
import sys
import msvcrt
leaderboard = {}

while True:
    print('\033[1;37mPress any key to start\nUse the buttons [1/2/3/4]\033[1;37m')
    start = msvcrt.getch()

    # Variaveis
    p = 0
    empty = '\033[1;37m   '
    fill = '\033[1;31m[*]\033[1;37m'
    x = '\033[1;37m   '
    xx = '\033[1;37m   '
    xxx = '\033[1;37m   '
    xxxx = '\033[1;37m   '
    warn = '\033[1;33m...\033[1;37m'
    fake = '\033[1;35m===\033[1;37m'
    place = 0
    t = Timer(0 , time.sleep(0.2))
    failsafe = False
    score = 0
    timeout = 2.5
    mindiff = -5
    diff = 11

    # Final
    def fail(score, leaderboard):
        score = (score - 1) * 10000
        score = int(score)
        print('\033[1;31;40m+' * 17)
        print('\033[1;31;40m' + ('+' * 5) + 'Failure' + ('+' * 5))
        print('+' * 17 + '\033[1;37;48m')
        print(f'Score: {score}')
        name = str(input('Type your name: '))
        print('')
        time.sleep(0.2)
        leaderboard[name] = score
        leaderboard = sorted(leaderboard.items(), key=lambda x:x[1], reverse=True)
        for key in leaderboard:
            print(f'{key[0]} : {key[1]}')
        time.sleep(0.2)
        score = 0
        again = str(input('\nPLAY AGAIN?\033[0m')).casefold()
        if again == 'no':
            sys.exit()
        else:
            return score

    # Obstaculos
    def obstacles(player, place):
        p = player
        match place:
            case 1:
                print(f'|{empty}:{fill}:{fill}:{empty}|')
                if p != 2 and p != 3 and p != 100:
                    print(f'|{x}:{fill}:{fill}:{xxxx}|')
                elif p == 100:
                    print(f'|{empty}:{warn}:{warn}:{empty}|')
                else:
                    return False
                
            case 2:
                print(f'|{empty}:{empty}:{fill}:{empty}|')
                if p != 3 and p != 100:
                    print(f'|{x}:{xx}:{fill}:{xxxx}|')
                elif p == 100:
                    print(f'|{empty}:{empty}:{warn}:{empty}|')
                else:
                    return False
                
            case 3:
                print(f'|{empty}:{empty}:{empty}:{fill}|')
                if p != 4 and p != 100:
                    print(f'|{x}:{xx}:{xxx}:{fill}|')
                elif p == 100:
                    print(f'|{empty}:{empty}:{empty}:{warn}|')
                else:
                    return False
                
            case 4:
                print(f'|{fill}:{empty}:{empty}:{empty}|')
                if p != 1 and p != 100:
                    print(f'|{fill}:{xx}:{xxx}:{xxxx}|')
                elif p == 100:
                    print(f'|{warn}:{empty}:{empty}:{empty}|')
                else:
                    return False
                
            case 5:
                print(f'|{empty}:{fill}:{empty}:{empty}|')
                if p != 2 and p != 100:
                    print(f'|{x}:{fill}:{xxx}:{xxxx}|')
                elif p == 100:
                    print(f'|{empty}:{warn}:{empty}:{empty}|')
                else:
                    return False
                
            case 6:
                print(f'|{fill}:{empty}:{fill}:{empty}|')
                if p != 1 and p != 3 and p != 100:
                    print(f'|{fill}:{xx}:{fill}:{xxxx}|')
                elif p == 100:
                    print(f'|{warn}:{empty}:{warn}:{empty}|')
                else:
                    return False
                
            case 7:
                print(f'|{empty}:{fill}:{empty}:{fill}|')
                if p != 2 and p != 4 and p != 100:
                    print(f'|{x}:{fill}:{xxx}:{fill}|')
                elif p == 100:
                    print(f'|{empty}:{warn}:{empty}:{warn}|')
                else:
                    return False
                
            case 8:
                print(f'|{empty}:{empty}:{fill}:{fill}|')
                if p != 3 and p != 4 and p != 100:
                    print(f'|{x}:{xx}:{fill}:{fill}|')
                elif p == 100:
                    print(f'|{empty}:{empty}:{warn}:{warn}|')
                else:
                    return False
                
            case 9:
                print(f'|{fill}:{fill}:{empty}:{empty}|')
                if p != 1 and p != 2 and p != 100:
                    print(f'|{fill}:{fill}:{xxx}:{xxxx}|')
                elif p == 100:
                    print(f'|{warn}:{warn}:{empty}:{empty}|')
                else:
                    return False
                
            case 10:
                print(f'|{fill}:{empty}:{empty}:{fill}|')
                if p != 1 and p != 4 and p != 100:
                    print(f'|{fill}:{xx}:{xxx}:{fill}|')
                elif p == 100:
                    print(f'|{warn}:{empty}:{empty}:{warn}|')
                else:
                    return False
            
            case 11:
                print(f'|{fill}:{fill}:{empty}:{fill}|')
                if p != 1 and p != 2 and p != 4 and p != 100:
                    print(f'|{fill}:{fill}:{xxx}:{fill}|')
                elif p == 100:
                    print(f'|{warn}:{warn}:{empty}:{warn}|')
                else:
                    return False
            
            case 12:
                print(f'|{fill}:{empty}:{fill}:{fill}|')
                if p != 1 and p != 3 and p != 4 and p != 100:
                    print(f'|{fill}:{xx}:{fill}:{fill}|')
                elif p == 100:
                    print(f'|{warn}:{empty}:{warn}:{warn}|')
                else:
                    return False
            
            case 13:
                print(f'|{empty}:{fill}:{fill}:{fill}|')
                if p != 2 and p != 3 and p != 4 and p != 100:
                    print(f'|{x}:{fill}:{fill}:{fill}|')
                elif p == 100:
                    print(f'|{empty}:{warn}:{warn}:{warn}|')
                else:
                    return False
            
            case 14:
                print(f'|{fill}:{fill}:{fill}:{empty}|')
                if p != 1 and p != 2 and p != 3 and p != 100:
                    print(f'|{fill}:{fill}:{fill}:{xxxx}|')
                elif p == 100:
                    print(f'|{warn}:{warn}:{warn}:{empty}|')
                else:
                    return False
                
            case 15:
                print(f'|{fill}:{fill}:{empty}:{fill}|')
                if p != 1 and p != 2 and p != 4 and p != 100:
                    print(f'|{fill}:{fill}:{xxx}:{fill}|')
                elif p == 100:
                    print(f'|{warn}:{empty}:{fake}:{warn}|')
                else:
                    return False
            
            case 16:
                print(f'|{fill}:{empty}:{fill}:{fill}|')
                if p != 1 and p != 3 and p != 4 and p != 100:
                    print(f'|{fill}:{xx}:{fill}:{fill}|')
                elif p == 100:
                    print(f'|{warn}:{fake}:{empty}:{warn}|')
                else:
                    return False
            
            case 17:
                print(f'|{empty}:{fill}:{fill}:{fill}|')
                if p != 2 and p != 3 and p != 4 and p != 100:
                    print(f'|{x}:{fill}:{fill}:{fill}|')
                elif p == 100:
                    print(f'|{fake}:{empty}:{warn}:{warn}|')
                else:
                    return False
            
            case 18:
                print(f'|{fill}:{fill}:{fill}:{empty}|')
                if p != 1 and p != 2 and p != 3 and p != 100:
                    print(f'|{fill}:{fill}:{fill}:{xxxx}|')
                elif p == 100:
                    print(f'|{empty}:{warn}:{warn}:{fake}|')
                else:
                    return False
            
            case _:
                print(f'|{empty}:{empty}:{empty}:{empty}|')
                print(f'|{x}:{xx}:{xxx}:{xxxx}|')

    # Loop Principal
    while obstacles(p, place) != False:
        t.cancel()
        score = float(score)
        score += 1
        
        if score >= 10 and score < 20:
            timeout = 2
        elif score >= 20 and score < 30:
            mindiff = -2
        elif score >= 30 and score < 40:
            diff = 15
        elif score >= 40 and score < 50:
            timeout = 1.5
        elif score >= 50 and score < 60:
            print('\033[1;37;40m', end= '')
            score += 0.5
            timeout = 1
        elif score >= 60 and score < 70:
            mindiff = 0
        elif score >= 70 and score < 80:
            score += 0.5
            timeout = 0.75
        elif score >= 80 and score < 90:
            score += 0.5
            diff = 19
        elif score >= 90 and score < 100:
            score += 0.5
            mindiff = 10
        elif score >= 100:
            score += 0.5
            timeout = 0.5

        place = random.randrange(mindiff,diff)
        if place > 10 and place < 15:
            score += 0.5
        if place >= 15:
            score += 1
        obstacles(100, place)

        try:
            t = Timer(timeout, lambda: time.sleep(0.2))
            t.start()
            if failsafe == False:
                p = int(msvcrt.getch())
            else:
                t.cancel()
                time.sleep(5)
                sys.exit()
            if p != 1 and p != 2 and p != 3 and p != 4:
                t.cancel()
            if 'stopped' in str(t):
                p = 0
                print('\033[1;33m----TIME--OUT----')
            z = p
        except:
            p = 0
            z = p
            t.cancel()

        if p == 1:
            x = '\033[1;32m<^>\033[1;37m'
            xx = '\033[1;37m   '
            xxx = '\033[1;37m   '
            xxxx = '\033[1;37m   '
            z = p
        elif p == 2:
            x = '\033[1;37m   '
            xx = '\033[1;32m<^>\033[1;37m'
            xxx = '\033[1;37m   '
            xxxx = '\033[1;37m   '
            z = p
        elif p == 3:
            x = '\033[1;37m   '
            xx = '\033[1;37m   '
            xxx = '\033[1;32m<^>\033[1;37m'
            xxxx = '\033[1;37m   '
            z = p
        elif p == 4:
            x = '\033[1;37m   '
            xx = '\033[1;37m   '
            xxx = '\033[1;37m   '
            xxxx = '\033[1;32m<^>\033[1;37m'
            z = p
        else:
            fail(score, leaderboard)
            score = 0
            failsafe = True

    if failsafe == False:
        fail(score, leaderboard)
        score = 0