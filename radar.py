#    HAKAN AYDIN         #
#    hakayd28@gmail.com  #

import Tkinter as tk
from random import randint
import time
import random

W = 542
H = 542
counter  = 0

root = tk.Tk()
canvas = tk.Canvas(root, width=W, height=H, borderwidth=0, highlightthickness=0, bg="black")
canvas.grid()

#####################################################################################
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle = _create_circle

#####################################################################################
def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x - r, y - r, x + r, y + r, **kwargs)


tk.Canvas.create_circle_arc = _create_circle_arc

#####################################################################################
def draw():
    for i in range(6):
        canvas.create_circle_arc(W / 2, H / 2, 45 + i * 45, style="arc", outline="green", width=1, start=0, end=359)

    canvas.create_line(W / 2, 0, W / 2, H, fill="green")
    canvas.create_line(0, H / 2, W, H / 2, fill="green")

#####################################################################################

def go(counter_q):
    canvas.create_circle_arc(W / 2, H / 2, H / 2, fill= "red", outline= "", start= 0 + counter_q, end= 3 + counter_q)
#####################################################################################
def clear():
    canvas.delete("all")

#####################################################################################
def create_object(random_object):

    count = 1
    colors = create_color_array()

    print random_object
    while count<random_object:
        r = create_random_coordinate()
        canvas.create_oval( r, r , r+20, r + 20, fill = colors[count % len(colors)])
        time.sleep(.04)

        count += 1

#####################################################################################

def create_random_object():
    return random.randint(1, 5)
#####################################################################################

def create_random_coordinate():
    return random.randint(100, 300)
#####################################################################################

def create_color_array():
    colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7', '#F6CC1D']

    return  colors
#####################################################################################
def animate():
    draw()
    create_object( create_random_object() )
    canvas.update()
    time.sleep(.04)
    clear()
    draw()
    go(counter)
    #canvas.create_circle_arc(W / 2, H / 2, H / 2, fill="red", outline="", start=0 + counter, end=3+ counter);
    print "hakan"

while True:
    animate()
    counter += 3

root.wm_title("Circles and Arcs")
root.mainloop()
