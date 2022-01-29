import random

def correct(word):
    length = len(word)
    for i in range (length):
        for j in range (i):
            if (word[i] == word[j]):
                return False
    return True

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
a = input('我是hangman模擬器。我會從高中七千單之中，抽出一個英文單字為答案，請用hangman的規則來猜出這個單字。'
          '一開始，我只會告訴你答案(單字)的長度，不會告訴你單字中的任何一個字母。'
          '你一共有十條命，每次猜測可以猜一個英文字母。如果答案之中包含那個猜測的字母，我會告訴你那個字母的位置，'
          '如果沒有那個字母，那你會減少一條命。如果你在用光十條命之前猜出答案的所有字母，則你贏得遊戲，反之，你輸掉遊戲。(按enter以繼續)')
num = 0
while (correct(english[num]) == False):
    num = random.randint(0,length-1)
(answer, my) = (english[num], '')
times = 1
print('這題的答案長度為', len(answer))
while (answer != my):
    print('第', times, '次。')
    my = input('請輸入你的答案：')
    if (len(answer) != len(my)):
        print('輸入的答案長度錯誤。')
        continue
    color = ['BLACK' for i in range (len(answer))]
    for i in range (len(my)):
        for j in range (len(answer)):
            if (my[i] == answer[j]):
                if (i == j):
                    color[i] = 'GREEN'
                else:
                    color[i] = 'YELLOW'
        if (color[i] == 'BLACK'):
            print(my[i], end = '')
        if (color[i] == 'YELLOW'):
            print(f"{bcolors.WARNING}{my[i]}{bcolors.RESET}", end = '')
        if (color[i] == 'GREEN'):
            print(f"{bcolors.OK}{my[i]}{bcolors.RESET}", end = '')
    times += 1
print('恭喜你找到答案。你總共猜了', times-1, '次')
