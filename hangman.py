import random

myfile = open('vocabulary.txt')
english = []
while (True):
    a = myfile.readline()
    if (a == ''):
        break
    if (a[0] in {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z'}):
        english.append(a.split(' ')[0])
            
length = len(english)
print('我是hangman模擬器。我會從高中七千單之中，抽出一個英文單字為答案，請用hangman的規則來猜出這個單字。')
print('一開始，我只會告訴你答案(單字)的長度，不會告訴你單字中的任何一個字母。'
      '你一共有十條命，每次猜測可以猜一個英文字母。如果答案之中包含那個猜測的字母，我會告訴你那個字母的位置，'
      '如果沒有那個字母，那你會減少一條命。')
a = input('如果你在用光十條命之前猜出答案的所有字母，則你贏得遊戲，反之，你輸掉遊戲。(按enter以繼續)')

num = random.randint(0,length-1)
answer = english[num]
status = ['_' for i in range (len(answer))]
live = 10
correct = 0
win = 0
guessed = []
while (win == 0):
    print('\n目前的狀態：', end = '')
    for i in range (len(answer)):
        print(status[i], end = '')
    print('\n以下是你目前有猜過的字母：', end = ' ')
    for i in range (len(guessed)):
        print(guessed[i], end = ' ')
    print('\n你還剩下', live, '條命。', end = '')
    guess = input('請猜一個小寫英文字母：')
    if (guess not in {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p','q','r','s','t','u','v','w','x','y','z'}):
        a = input('這不是一個小寫英文字母(按enter以繼續)')
        continue
    guessed.append(guess)
    die = True
    for i in range (len(answer)):
        if ((answer[i] == guess) and (status[i] == '_')):
            status[i] = guess
            correct += 1
            die = False
    if (die == True):
        live -= 1
    if (live == 0):
        win = -1
    if (correct == len(answer)):
        win = 1
if (win == 1):
    print('\n正確答案是', answer, '，恭喜你贏了！')
if (win == -1):
    print('\n正確答案是', answer, '，你輸了...')
