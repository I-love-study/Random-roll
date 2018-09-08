from tkinter import *
import tkinter.font as tkFont
import time
import random
import gc
import os,sys
import objgraph

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

def a():
    lb.delete(0,END)

def name():
    pict["image"] = huang_gif
    button["text"] = '先别点我'
    fp=open(r"7.txt")
    name=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        name.append(lines)
    fp.close()
    do = len(name)-1
    ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)
    hua = time.time()
    
    a = list(range(0,do))
    random.shuffle(a)
    use = a[0:int(v.get())]
    ren = int(v.get())
    for i in range(ren):
        for a in range(23):
            index = random.randint(0,do)
            echo["text"] = name[index]
            root.update_idletasks()
            time.sleep(1/23-0.003)
        pict['image']= huaji_gif
        echo["text"] = name[use[i]]
        lb.insert(END,name[use[i]])
        root.update_idletasks()
        print ((time.time()-hua))
        for a in range(5):
            root.update
            time.sleep(0.06)
        pict['image']= huang_gif
        print (objgraph.show_growth())
    button["text"] = '开始点名'
    for x in locals().keys():
        del locals()[x]
    gc.collect()
    pict['image']= huaji_gif
    scrolly.update

root = Tk()

root.title ("随机点名器(by FJJ)")

center_window(root, 570, 160)

ft =  tkFont.Font(family = 'Fixdsys',size = 40,weight = tkFont.BOLD)
ft1 =  tkFont.Font(family = 'Fixdsys',size = 80,weight = tkFont.BOLD)
echo = Label(root,text = '我爱学习',font = ft,width = 8 )
echo.grid(row=1,column=1,columnspan=2)
Label(root,text = 'Make by I_love_study').grid(row=3,column=1,columnspan=2)

scrolly=Scrollbar(root)
scrolly.grid(row=1,column=5,rowspan=2,ipady=30)
lb = Listbox(root,yscrollcommand=scrolly.set,exportselection=False,height=6)
lb.grid(row=1,column=3,rowspan=2,columnspan=2,pady=0)
scrolly['command'] = lb.yview

button = Button(root, text='删除所选名字', command=lambda x=lb:x.delete(ACTIVE))
button.grid(row=3,column=3)
button = Button(root, text='删除所有名字', command=a)
button.grid(row=3,column=4)

v = StringVar()
Scale(root,from_=1,to=20,resolution=1,orient=HORIZONTAL,variable=v).grid(row=2,column=1)

data_dir = "tupian"
huaji_gif=PhotoImage(file=resource_path(os.path.join(data_dir, 'huaji.gif')))
huang_gif=PhotoImage(file=resource_path(os.path.join(data_dir, 'huang.gif')))
pict = Label(root,image=huaji_gif)
pict.grid(row=1,column=0,rowspan=3)
button = Button(root, text='开始点名', command=name)
button.grid(row=2,column=2)

root.mainloop()
