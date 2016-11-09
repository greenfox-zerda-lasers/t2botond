# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.
from tkinter import *
import random
import time
root = Tk()
p=600
ca = Canvas(root, width = p, height = p)
i = 0
print(ca["width"])

def generate_color():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color
ca.pack()

while i < p/2:
    ca.create_line(0,i,(p/2)-i,0, fill=generate_color())
    ca.create_line((p/2),(p/2)-i,i,(p/2), fill=generate_color())

    ca.create_line(0+(p/2),i,(p/2)-i+(p/2),0, fill=generate_color())
    ca.create_line((p/2)+(p/2),(p/2)-i,i+(p/2),(p/2), fill=generate_color())

    ca.create_line(0,i+(p/2),(p/2)-i,0+(p/2), fill=generate_color())
    ca.create_line((p/2),(p/2)-i+(p/2),i,(p/2)+(p/2), fill=generate_color())

    ca.create_line(0+(p/2),i+(p/2),(p/2)-i+(p/2),0+(p/2), fill=generate_color())
    ca.create_line((p/2)+(p/2),(p/2)-i+(p/2),i+(p/2),(p/2)+(p/2), fill=generate_color())
    time.sleep(0.2)
    ca.update()
    i+=5
root.mainloop()
