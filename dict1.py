#from interf import *
def newdict():
    print('Write "time_of_words" (new or last)')
    time_of_words = str(input())
    with open('dict.txt', 'rt') as f:
            new = f.readlines()
    f = open('dict.txt', 'wt')
    f.close()
    for i in range(0, len(new)):
        new[i] = new[i][:-1]
    trans = ''
    stop = len(new)
    i = 0
    while (i < stop) and trans != 'stop239':
        print ('Translate to English: ',new[i])
        trans = str(input())
        if trans == 'stop239':
            with open('dict.txt', 'wt') as f:
                for j in range(i, len(new)):
                    print (new[j], file=f)
            stop = i
        new[i] = (new[i] ,trans)
        i += 1
    if time_of_words == 'last':
        with open('dict2.txt', 'at') as f:
            for i in range(0, stop):
                print (new[i], file=f)
    elif time_of_words == 'new':
        with open('dict2.txt', 'rt') as f:
            last = f.readlines()
        with open('dict2.txt', 'wt') as f:
            for i in range(0, stop):
                print (new[i], file=f)
            for i in range(0, len(last)):
                print (last[i][:-1], file=f)
    
def opendict(interval):
    f = open('dict2.txt', 'rt')
    lines = f.readlines()
    f.close()
    d = list()
    if interval == 'all':
        INTER = 0, len(lines)
    else:
        INTER = interval
    for i in range(INTER[0], INTER[1]):
       l = lines[i][1:-2]
       l = str(l)
       l = l.split(', ')
       l[0] = l[0][1:-1]
       l[1] = l[1][1:-1]
       d.append(l)
    return d

def test(lang = 'English', n = 20, replay = 'No', hard = 0, inter = 'all', name = 'Yes'):
    from random import randint
    import csv
    if n == 'all' :
        n = inter[1] - inter[0]
    if inter != 'all' and inter[1] - inter[0]< n:
        n = inter[1] - inter[0]
    d = opendict(inter)
    if lang == 'English' :
        place = 0
        place2 = 1
    else:
        place = 1
        place2 = 0
    res = 0
    nums = []
    for i in range(0, n):
        num = randint(0, len(d)-1)
        if replay == 'No':
            while num in nums:
                num = randint(0, len(d)-1)
        nums.append(num)
        if hard > 0:  
            q = d[num][place].split (' / ')
            s = q[randint(0 , len(q)-1)]
        elif hard == 0 :
            s = d[num][place]
        print ('Translate to ',lang,' : ', s)
        #que = str('Translate to' + lang +':'+s)
        trans = str(input())
        right_trans = d[num][place2].split(' / ')
        if trans in right_trans:
            print('--- Yes')
            res += 1
        else :
            print('--- No, it is ', d[num][place2])
    p = (res/n )
    if name == 'Yes':
        print('What is your name?')
        name = input()
    elif name == 'No':
        name = ''
    print('Is is all. Your result: ', res, 'or', p*100, '%')
    inf = [{'lang':lang, 'inter':inter, 'n':n, 'res':res, 'name':name}]
    with open('res.csv', 'at') as f:
        c= csv.DictWriter(f, ['lang', 'inter', 'n', 'res', 'name'])
        c.writerows(inf)

def dictionary(translate_to='English'):
    print('stop239 - exit, re239 - change languache')
    d = dict(opendict('all'))
    qd = {}
    for n in list(d.keys()):
        qd[d[n]] = n
    if translate_to in ['English', 'E']:
        words = list(d.keys())
        dic = d
    elif translate_to in ['Russian', 'R']:
        words = list(d.values())
        dic = qd
    word = ''
    stop = 're239'
    
    while word != 'stop239':
        print('Your word: ')
        word = str(input())
        if word == stop:
            if dic == d:
                dic = qd
                print('English')
            elif dic == qd:
                dic = d
                print('Russian')
        elif word != 'stop239':
            translate(stop, dic, word)
        
def translate(stop, d, word):
    trans = d.get(word, "I don't now this word")
    print(word, ' - ' , trans)
