from tkinter import *

root=Tk()
canvas1 = Canvas(root, width = 200, height = 100)
canvas1.pack()
blackLine=canvas1.create_line(0, 0, 200, 50)

root.mainloop()
