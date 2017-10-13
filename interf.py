from tkinter import *
import time
from random import randint
import csv

def button_clicked(event):
    global stt, okf, p, c, namein , name, root, score, lang, d, nums, hard, res, replay, right_trans, place, place2, n, num, question, v, your, true_ans
    if len(nums) >0:
        trans = v.get()
        your['text'] = trans
        v.delete(first=0, last = len(trans))

        if trans in right_trans:
            your['fg'] = 'green'
            res += 1
        else:
            your['fg'] = 'red'
        
        true_ans['text'] = str(d[num][place2]) + ' - ' + str(d[num][place])
    score['text'] = str(res)+ ' of '+ str(n)
    if len(nums) < n:
        if len(nums) ==0:
            v.grid()
            stt.grid_remove()
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
        question['text'] = str('Translate to ' + lang +' : '+s)
        right_trans = d[num][place2].split(' / ')
    elif len(nums) == n:
        v.grid_remove()
        root.after(4000, stop_test)
        
def stop_test():
    global okf, c, namein, name, p,root 
    p = (res/n)
    
    c=Toplevel(root)
    c.title( 'Result')
    
    if name == 'Yes':
        text4 = Label(c, text='What is your name?')
        text4.grid(row=0, column = 0, columnspan = 1)
        namein = Entry(c)
        namein.grid(row=0, column = 1, columnspan = 1)
        #okf = Button(c, text = 'OK', command = newname_res)
        #okf.grid(row=0, column = 2, columnspan = 1)
        c.bind("<Return>", newname_res)
        
def newname_res(event=None):
    global namein, c , name, p , okf
    #print('new')
    if name == 'Yes':
        #okf.grid_remove()
        name = namein.get()
    elif name == 'No':
        name = ''
    text5 = Label(c, text='Is is all. Your result: '+ score['text']+ ' or '+ str(round(p*100,1))+ ' %')
    text5.grid(row=1, column = 0, columnspan = 3)
    inf = [{'lang':lang, 'inter':inter, 'n':n, 'res':res, 'name':name}]
    with open('res.csv', 'at') as f:
        table= csv.DictWriter(f, ['lang', 'inter', 'n', 'res', 'name'])
        table.writerows(inf)
        
    #time.sleep(1)
    newtest = Button(c, text='New test' , command=new_test )
    newtest.grid(row = 3 , column = 0)

    ex = Button(c, text='EXIT' , command=exit_test )
    ex.grid(row = 3 , column = 2)

    sett = Button(c, text = 'Setting', command = new_setting)
    sett.grid(row=3, column = 1)

def exit_test():
    global root
    root.destroy()
def new_test():
    global c, root
    c.destroy()
    start_test()
    
def cl(event):
    if true_ans['text'] != '':
        true_ans['text'] = ''
        your['text'] = ''

def MAIN():
    global question, v, your, true_ans, score ,root, stt
    root=Tk()
    root.title('Test')
    root.withdraw()
    setting()
    
    score = Label()
    score.config( text = '')
    score.grid(row=6, column = 0)
    '''
    button = Button()
    button.configure( text='OK', command=button_clicked(None))
    button.grid(row = 1, column = 5)
    '''
    root.bind("<Return>", button_clicked)
    root.bind("<Key>", cl)

    v = Entry()
    v.config(fg='blue')
    v.grid(row = 1, column = 1, columnspan = 3)
    v.grid_remove()

    text1 = Label()
    text1.config(text = 'Your answer:')
    text1.grid(row = 1, column = 0)

    your = Label()
    your.config()
    your.grid(row = 2, column = 1, columnspan = 3)

    text2 = Label()
    text2.config(text = 'True answer:')
    text2.grid(row = 3, column = 0)

    true_ans = Label()
    true_ans.config()
    true_ans.grid(row = 3, column = 1, columnspan = 4)

    question = Label()
    question.config( text = '')
    question.grid(row=0, column = 0, columnspan = 5)

    stt = Button()
    stt.configure(text='Start', command=start_test)
    stt.grid(row = 6, column = 5)

    root.mainloop()

def new_setting():
    global c, root
    c.destroy()
    setting()
    start_test()

def setting_f():
    global SETTING, root, lang, n, inter, hard, replay, name, var , ENum, EInt
    if ENum.get() != '':
        n = int(ENum.get())
    if EInt.get() !='':
        inter = EInt.get()
        if inter  != 'all':
            inter = inter[1:-1]
            inter = inter.split(',')
            inter = [int(inter[0]), int(inter[1])]
    #print(var)
    if str(var) =='PY_VAR0':
        lang = 'Russian'
    elif str(var) == 'PY_VAR1':
        lang = 'English'
        
    SETTING.destroy()
    root.deiconify()
    #start_test()

def setting():
    global SETTING, root, lang, n, inter, hard, replay, name, var, ENum, EInt
    
    lang = 'English'
    n = 20
    inter = 'all'
    hard = 0
    replay = 'No'
    name = 'Yes'
    
    SETTING=Toplevel(root)
    SETTING.title( 'Setting')
    
    FrLang = Frame (SETTING, bg = '#b6e1fc', bd = 4)
    FrLang.grid(row = 0,column = 0)
    text7 = Label(FrLang, text = 'Language',font = 'Calibri 11')
    text7.pack(side = 'top')
    var=IntVar ()
    
    RadLang1 =Radiobutton (FrLang,text='Russian',variable =var,value =1, font = 'Calibri 11')
    RadLang2 =Radiobutton (FrLang,text='English',variable =var,value =2, font = 'Calibri 11')
    RadLang1.pack(side = 'top')
    RadLang2.pack(side = 'top')

    FrN = Frame (SETTING, bg = '#b6e1fc', bd = 10)
    FrN.grid(row = 0,column = 1)
    text8 = Label(FrN, text = 'Number of words', font = 'Calibri 11')
    text8.pack(side = 'top')
    ENum = Entry(FrN, font = 'Calibri 11')
    ENum.pack(side = 'top')
    text11 = Label(FrN, text = '20', font = 'Calibri 11')
    text11.pack(side = 'top')

    FrInter = Frame (SETTING, bg = '#b6e1fc', bd = 10)
    FrInter.grid(row = 0,column = 2)
    text9  = Label(FrInter, text = 'Interval', font = 'Calibri 11')
    text9.pack(side = 'top')
    EInt = Entry(FrInter, font = 'Calibri 11')
    EInt.pack(side = 'top')
    text10 = Label(FrInter, text = '(s, f) / all', font = 'Calibri 11')
    text10.pack(side = 'top')
    
    OK = Button(SETTING)
    OK.config(text = 'OK', font = 'Calibri 11', command = setting_f, width = 15)
    OK.grid(row = 2,column = 2)
    
def start_test ():
    global lang, n, inter, d, place, place2, res, nums, hard, replay, name, p, d 
    '''
    
    '''
    res=0
    p=0
    d=0
    res = 0
    nums = []
    name = 'Yes'

    print('test started')
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
    
    button_clicked(None)
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
MAIN()
