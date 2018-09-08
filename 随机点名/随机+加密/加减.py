import base64
from tkinter import *

def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    print(size)  
    root.geometry(size)

def give_it():
    to_name = de[int(str(lb.curselection())[1:-2])]
    give = zu + " " + to_name + " " + s.get()
    print (give)
    
    with open('计分.txt', "a") as f:
        f.write(base64.b64encode(give.encode('utf-8')).decode("utf-8"))
        f.write("\n")

def zu():
    global zu,de
    zu = str(v.get())
    lb.delete(0,END)
    fp=open("组\%s.txt" % (zu))
    de=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        lb.insert(END,lines)
        de.append(lines)
    fp.close()
    

root = Tk()
center_window(root, 300, 300)

lb=Listbox(root,exportselection=False)
lb.grid(row=0,column=0,padx=(5,5),pady=10)

s = StringVar()
Scale(root,from_=-6,to=6,resolution=1,variable=s,label="打分").grid(row=0,column=1)
v = StringVar()
Scale(root,from_=1,to=7,resolution=1,orient=HORIZONTAL,variable=v,label="选择组").grid(row=1,column=0)

button = Button(root, text='刷新组', command=zu)
button.grid(row=1,column=1)
button = Button(root, text='打分', command=give_it)
button.grid(row=1,column=2)

root.mainloop()
