import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z']

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def correct(answer):
    for i in range (len(answer)):
        if (answer[i] not in alphabet):
            return False
    return True

def getans():
    myfile = open('vocabulary.txt')
    english = []
    while (True):
        a = myfile.readline()
        if (a == ''):
            break
        if (a[0] in alphabet):
            english.append(a.split(' ')[0])
            
    length = len(english)
    num = random.randint(0,length-1)
    while (correct(english[num]) == False):
        num = random.randint(0, length-1)
    return english[num]

def correctformat(my, answer):
    if (len(answer) != len(my)):
        print('輸入的答案長度錯誤。')
        return False
    for i in range (len(my)):
        if (my[i] not in alphabet):
            print('請勿輸入小寫英文字母以外的字串')
            return False
    return True

def getcolor(answer, my):
    color = ['BLACK' for i in range (len(answer))]
    not_green = []
    for i in range (len(my)):
        if (answer[i] == my[i]):
            color[i] = 'GREEN'
        else:
            not_green.append(answer[i])
    for i in range (len(my)):
        if (color[i] == 'GREEN'):
            continue
        if (my[i] in not_green):
            color[i] = 'YELLOW'
            not_green.remove(my[i])
    return color

def printguess(guessed):
    print()
    for j in range (len(guessed)):
        (my, color) = (guessed[j][0], guessed[j][1])
        for i in range (len(my)):
            if (color[i] == 'BLACK'):
                print(my[i], end = '')
            if (color[i] == 'YELLOW'):
                print(f"\033[93m{my[i]}\033[0m", end = '')
            if (color[i] == 'GREEN'):
                print(f"\033[92m{my[i]}\033[0m", end = '')
        print()
    return

def changeboard(keyboard, my, color):
    for i in range (len(my)):
        if (keyboard[my[i]] == 'YELLOW'):
            if (color[i] == 'GREEN'):
                keyboard[my[i]] = 'GREEN'
        if (keyboard[my[i]] == 'WHITE'):
            keyboard[my[i]] = color[i]
    return keyboard

def printboard(keyboard):
    order = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
             ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
             ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    for i in range (3):
        for j in range (i):
            print(' ', end = '')
        for j in range (len(order[i])):
            if (keyboard[order[i][j]] == 'WHITE'):
                print(order[i][j], end = '   ')
            elif (keyboard[order[i][j]] == 'YELLOW'):
                print(f"\033[93m{order[i][j]}\033[0m", end = '   ')
            elif (keyboard[order[i][j]] == 'GREEN'):
                print(f"\033[92m{order[i][j]}\033[0m", end = '   ')
            else:
                print(' ', end = '   ')
        print()
    return
    
'''
print(f"{bcolors.OK}File Saved Successfully!{bcolors.RESET}")
print(f"{bcolors.WARNING}Warning: Are you sure you want to continue?{bcolors.RESET}")
print(f"{bcolors.FAIL}Unable to delete record.{bcolors.RESET}")
'''
            
a = input('我是wordle模擬器。我會從高中七千單之中，抽出一個每個字母都不一樣的英文單字'
          '(但是單字的長度不固定，不過單字不會出現重複的字母)。請用wordle的規則來猜出這個單字'
          '(綠：字母和位置都對。黃：字母對但位置不對。黑：答案裡沒有這個字母)。'
          '(如果想放棄，請輸入BAD) (想快速查看英文字母，請輸入SEE) (按enter以繼續)')
answer = getans()
times = 1
print('\n這題的答案長度為', len(answer), '\n')
win = 0
keyboard = {alphabet[i]:'WHITE' for i in range (26)}
guessed = []
while (win == 0):
    print('\n\n第', times, '次。')
    my = input('請輸入你的答案：')
    if (my == 'BAD'):
        win = -1
        break
    if (my == 'SEE'):
        printboard(keyboard)
        continue
    if (correctformat(my, answer) == False):
        continue
    color = getcolor(answer, my)
    if (color == ['GREEN' for i in range (len(answer))]):
        win = 1
    keyboard = changeboard(keyboard, my, color)
    guessed.append((my, color))
    printguess(guessed)
    times += 1
if (win == 1):
    print('\n\n恭喜你找到答案。你總共猜了', times-1, '次')
if (win == -1):
    print('\n\n你放棄了。答案是', answer)
