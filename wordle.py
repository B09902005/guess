import random

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def correct(word):
    length = len(word)
    for i in range (length):
        for j in range (i):
            if (word[i] == word[j]):
                return False
    return True

'''
print(f"{bcolors.OK}File Saved Successfully!{bcolors.RESET}")
print(f"{bcolors.WARNING}Warning: Are you sure you want to continue?{bcolors.RESET}")
print(f"{bcolors.FAIL}Unable to delete record.{bcolors.RESET}")
'''

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
a = input('我是wordle模擬器。我會從高中七千單之中，抽出一個每個字母都不一樣的英文單字'
          '(但是單字的長度不固定，不過單字不會出現重複的字母)。請用wordle的規則來猜出這個單字'
          '(綠：字母和位置都對。黃：字母對但位置不對。黑：答案裡沒有這個字母)。(按enter以繼續)')
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
