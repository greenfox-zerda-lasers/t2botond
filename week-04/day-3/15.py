# create a 300x300 canvas.
# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
from tkinter import *
import time
root = Tk()
p=300
canva = Canvas(root,width = p, height = p)
canva.pack()

def connector(lista):
    a=list[0][0]
    b=list[0][1]
    for i in lista:
        canva.create_line(i[0],i[1],a,b,fill = "green")
        a=i[0]
        b=i[1]
        time.sleep(0.2)
        canva.update()
    canva.create_line(a,b,list[0][0],list[0][1],fill = "green")
list = [[10,90],[65,86],[299,87],[159,279],[110,290],[165,186],[99,287],[159,29]]
connector(list)
def box(lista2):
        canva.create_line(lista2[0][0],lista2[0][1],lista2[1][0],lista2[1][1])
        time.sleep(0.2)
        canva.update()
        canva.create_line(lista2[1][0],lista2[1][1],lista2[2][0],lista2[2][1])
        time.sleep(0.2)
        canva.update()
        canva.create_line(lista2[2][0],lista2[2][1],lista2[3][0],lista2[3][1])
        time.sleep(0.2)
        canva.update()
        canva.create_line(lista2[3][0],lista2[3][1],lista2[0][0],lista2[0][1])
list2 = [[10, 10], [290,  10], [290, 290], [10, 290]]
box(list2)

def connector(list3):
    a=list3[0][0]
    b=list3[0][1]
    for i in list3:
        canva.create_line(i[0],i[1],a,b,fill = "green")
        a=i[0]
        b=i[1]
        time.sleep(0.2)
        canva.update()
    canva.create_line(a,b,list3[0][0],list3[0][1],fill = "green")
list3 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],[120, 100], [85, 130], [50, 100]]
connector(list3)
root.mainloop()
