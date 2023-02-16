# Initialization
from tkinter import *

# Canvas
# Width and height of the main canvas
widthCanva = 1000
heightCanva = 400

# Rods
# Distance between two rods
Distance = widthCanva / 4

# Height of a rod
Top = 4.2 * heightCanva / 5

# Base
# Dimensions of the base
socleL = widthCanva / 10
socleR = 9 * widthCanva / 10
Thick = 20

# Disk
# Width of the largest disk
Base = widthCanva / 4.2

# Width offset between two disks
Offset = 20

# Height of a disk
Height = 40

# Space between two disks
Separateur = 4

# Origin of the new reference frame
Origin = (0, heightCanva)

# Change of reference
def passage(X, Y, center=Origin):
    return (X + center[0], - Y + center[1])

# Creation of the main window
root = Tk()

# Creation of the main canvas by specifying its width, height and background
cnv = Canvas(root, width=widthCanva, height=heightCanva, bg="ivory")
cnv.pack()

# Creation of the base
A = passage(socleL, 0)
B = passage(socleR, Thick)
cnv.create_rectangle(A, B, fill="black")

# Creation of the rods
for i in range(3):
    x = (i + 1) * Distance - Thick / 2
    A = passage(x, 0)
    B = passage(x + Thick, Top)
    cnv.create_rectangle(A, B, fill="black")

# Disks
# Initially there are 4 disks
n = 4
# Initially the width of the rectangle is Base
w = Base

x = Distance - w / 2
y = Height / 2 + Separateur

# Initialize the list of disks to empty
ids = []

for _ in range(n):
    A = passage(x, y, Origin)
    B = passage(x + w, y + Height, Origin)
    rect = cnv.create_rectangle(A, B, fill="red", outline="")
    ids.append(rect)
    x += Offset
    y += Height + Separateur
    w -= 2 * Offset

# Move a disk
def move(nro, src, des):
    i, hi = src
    j, hj = des
    dx = (j - i) * Distance
    dy = -(hj - hi) * Height
    cnv.move(ids[nro], dx, dy)

# Test 1
move(2, (0,2), (1, 4))
# Test 2
move(0, (0,0), (2, 0))

# Event management (main loop)
root.mainloop()
