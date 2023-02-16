# Initialization
from tkinter import *

# Canvas
# Main canvas width and height
widthCanva = 1000
heightCanva = 400

# Rod
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
# The widest disk
Base = widthCanva / 4.2

# Width offset between two disks
Offset = 20

# Height of a disk
Height = 40
# Spacing between two disks
Separateur = 4

# Origin of the new coordinate system
Origin = (0, heightCanva)

# Change of coordinate system
def passage(X, Y, center=Origin):
    return (X + center[0], - Y + center[1])

# Create the main window
root = Tk()

# Create the main canvas specifying width, height, and background
cnv = Canvas(root, width=widthCanva, height=heightCanva, bg="ivory")
cnv.pack()

# Create the base
A = passage(socleL, 0)
B = passage(socleR, Thick)
# Create a black rectangle whose height is Thick and whose width is socleL - socleR
cnv.create_rectangle(A, B, fill="black")

# Create the rods
for i in range(3):
    # Move to a value x of the origin
    x = (i + 1) * Distance - Thick / 2
    A = passage(x, 0)
    B = passage(x + Thick, Top)
    # Create a black rectangle whose height is Top and whose width is Thick
    cnv.create_rectangle(A, B, fill="black")

# The disks
# Initially, the number of disks is 4
n = 4
# Initially, the width of the rectangle is Base
w = Base

x = Distance - w / 2
y = Height / 2 + Separateur

# Initialize the list of disks to be empty
ids = []

for _ in range(n):
    A = passage(x, y, Origin)
    B = passage(x + w, y + Height, Origin)
    # Create a red rectangle whose height is Height and whose width is w
    rect = cnv.create_rectangle(A, B, fill="red", outline="")
    # Add a disk to the list of disks
    ids.append(rect)
    # The new starting point for creating a rectangle is shifted by Offset on x
    # and it moves up by Height + a separator to separate between the 2 disks with a small space
    x += Offset
    y += Height + Separateur
    # Decrease the width of the rectangle by a value Offset at both ends
    w -= 2 * Offset

# Main event loop
root.mainloop()
