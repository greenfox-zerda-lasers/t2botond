from tkinter import *
root = Tk()
canvas = Canvas(root, width = 600, height = 600)
canvas.pack()
img = PhotoImage(file="floor.png")
canvas.create_image(0,0, anchor=NW, image=img)
root.mainloop()
