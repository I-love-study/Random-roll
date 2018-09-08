from tkinter import *
import tkinter.font as tkFont
import time
import random
import gc
import os,sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    print(size)  
    root.geometry(size)

def name():
    pict["image"] = huang_gif
    button["text"] = '先别点我'
    if v.get()=="0":
        choose = "组\%s.txt" % (random.randint(1,7))
    else:
        choose = "组\%s.txt" % (str(v.get()))

    fp=open(choose)
    de=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        de.append(lines)
    fp.close()
    print (de)
        
    fp=open("组\%s.txt" % (str(v.get())))
    name=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        name.append(lines)
    fp.close()
    do = len(name)-1
    la = len(de)-1
    ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)
    hua = time.time()
    
    for i in range(3):
        num["text"] = 3-i
        for a in range(23):
            index = random.randint(0,do)
            echo["text"] = name[index]
            root.update_idletasks()
            time.sleep(1/23-0.003)
    num["text"] = 0
    root.update_idletasks()
        
    number = list(range(0,la+1))
    print (number)
    random.shuffle(number)
    print (number)
    number = number[random.randint(0,la)]
    
    index = random.randint(0,do)
    echo["text"] = name[index]
    root.update_idletasks()
    print ((time.time()-hua))
    for a in range(5):
        root.update
        time.sleep(0.06)

    random.shuffle(de)
    print(de)
    fp=open(choose,'w')
    for i in de:
        fp.write(i)
        fp.write("\n")
    fp.close()
    
    
    echo["text"] = de[number]
    button["text"] = '开始点名'
    for x in locals().keys():
        del locals()[x]
    gc.collect()
    pict.configure(image = huaji_gif)

color = '#40E0D0'
root = Tk()
root['bg'] = color

root.title ("随机点名器(by FJJ)")

center_window(root, 500, 150)

ft =  tkFont.Font(family = 'Fixdsys',size = 40,weight = tkFont.BOLD)
ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)

echo = Label(root,text = '我爱学习',font = ft,width = 8,bg = color)
echo.grid(row=1,column=1,columnspan=2)

Label(root,text = 'Make by I_love_study',bg = color).grid(row=3,column=1,columnspan=2)

Label(root,text = '★',font = ft1,bg = color).grid(row=1,column=3,rowspan=4)
num = Label(root,text = '0',font = ft1,bg = color)
num.grid(row=1,column=3,rowspan=3)

v = StringVar()
Scale(root,from_=0,to=7,resolution=1,orient=HORIZONTAL,variable=v,bg = color).grid(row=2,column=1)

data_dir = "tupian"
huaji_gif=PhotoImage(file=resource_path(os.path.join(data_dir, 'huaji.gif')))
huang_gif=PhotoImage(file=resource_path(os.path.join(data_dir, 'huang.gif')))
pict = Label(root,image=huaji_gif)
pict.grid(row=1,column=0,rowspan=3)

button = Button(root, text='开始点名', command=name)
button.grid(row=2,column=2)

root.mainloop()
