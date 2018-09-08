import base64
from tkinter import *
import tkinter.font as tkFont
import time

def jifen():
    one=two=three=four=five=six=seven= "分数:"
    one_fen=two_fen=three_fen=four_fen=five_fen=six_fen=seven_fen= 0
    
    with open('计分.txt', 'r') as f:
        fen = []
        for lines in f.readlines():
            lines=lines.replace("\n","")
            lines = base64.b64decode(lines.encode('utf-8')).decode('utf-8')
            fen.append(lines)
    print (fen)
    for i in fen:
        if int(i.split(' ',1)[0]) > 7:
            print ("ERROR")
        zu = int(i.split(' ',1)[0])
        print (zu)
        if zu == 1:
            one = one + "\n" + i.split(' ',1)[1]
            one_fen+=int(i.split(' ')[2])
            one_print["text"]=one
            one_put["text"]=one_fen
            if one.count("\n")==5:
                one = one.split("\n",2)[0]+"\n"+one.split("\n",2)[2]
        if zu == 2:
            two = two + "\n" + i.split(' ',1)[1]
            two_fen+=int(i.split(' ')[2])
            two_print["text"]=two
            two_put["text"]=two_fen
            if two.count("\n")==5:
                two = two.split("\n",2)[0]+"\n"+two.split("\n",2)[2]
        if zu == 3:
            three = three + "\n" + i.split(' ',1)[1]
            three_fen+=int(i.split(' ')[2])
            three_print["text"]=three
            three_put["text"]=three_fen
            if three.count("\n")==5:
                three = three.split("\n",2)[0]+"\n"+three.split("\n",2)[2]
        if zu == 4:
            four = four + "\n" + i.split(' ',1)[1]
            four_fen+=int(i.split(' ')[2])
            four_print["text"]=four
            four_put["text"]=four_fen
            if four.count("\n")==5:
                four = four.split("\n",2)[0]+"\n"+four.split("\n",2)[2]
        if zu == 5:
            five = five + "\n" + i.split(' ',1)[1]
            five_fen+=int(i.split(' ')[2])
            five_print["text"]=five
            five_put["text"]=five_fen
            if five.count("\n")==5:
                five = five.split("\n",2)[0]+"\n"+five.split("\n",2)[2]
        if zu == 6:
            six = six + "\n" + i.split(' ',1)[1]
            six_fen+=int(i.split(' ')[2])
            six_print["text"]=six
            six_put["text"]=six_fen
            if six.count("\n")==5:
                six = six.split("\n",2)[0]+"\n"+six.split("\n",2)[2]
        if zu == 7:
            seven = seven + "\n" + i.split(' ',1)[1]
            seven_fen+=int(i.split(' ')[2])
            seven_print["text"]=seven
            seven_put["text"]=seven_fen
            if seven.count("\n")==5:
                seven = seven.split("\n",2)[0]+"\n"+seven.split("\n",2)[2]
        root.update()
        time.sleep(0.2)

        

color = '#00EE00'
color1 = '#CD0000'
root = Tk()
root['bg'] = color

ft =tkFont.Font(family = 'Fixdsys',size = 40,weight = tkFont.BOLD)
ft1 = tkFont.Font(family = 'Fixdsys',size = 20,weight = tkFont.BOLD)

root.title ("分数显示(by FJJ)")

for a in range(1,8):
    b = "第"+str(a)+"组"
    Label(root,text = b,font = ft,bg=color).grid(row=0,column=a)

one_print = Label(root,font = ft1,text= "分数:")
one_print.grid(row=2,column=1)
two_print = Label(root,font = ft1,text= "分数:")
two_print.grid(row=2,column=2)
three_print = Label(root,font = ft1,text= "分数:")
three_print.grid(row=2,column=3)
four_print = Label(root,font = ft1,text= "分数:")
four_print.grid(row=2,column=4)
five_print = Label(root,font = ft1,text= "分数:")
five_print.grid(row=2,column=5)
six_print = Label(root,font = ft1,text= "分数:")
six_print.grid(row=2,column=6)
seven_print = Label(root,font = ft1,text= "分数:")
seven_print.grid(row=2,column=7)

one_put = Label(root,font=ft,text=0,bg=color1)
one_put.grid(row=1,column=1)
two_put = Label(root,font=ft,text=0,bg=color1)
two_put.grid(row=1,column=2)
three_put = Label(root,font=ft,text=0,bg=color1)
three_put.grid(row=1,column=3)
four_put = Label(root,font=ft,text=0,bg=color1)
four_put.grid(row=1,column=4)
five_put = Label(root,font=ft,text=0,bg=color1)
five_put.grid(row=1,column=5)
six_put = Label(root,font=ft,text=0,bg=color1)
six_put.grid(row=1,column=6)
seven_put = Label(root,font=ft,text=0,bg=color1)
seven_put.grid(row=1,column=7)

button = Button(root, text='计分开始', command=jifen)
button.grid(row=3,column=8)

root.mainloop()
