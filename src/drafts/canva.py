# Initialization
from tkinter import *

# Canvas
# Width and height of the main canvas
widthCanva = 1000
heightCanva = 400

# Stem
# Distance between two stems
Distance = widthCanva / 4

# Height of a stem
Top = 4.2 * heightCanva / 5

# Base
# Dimensions of the base
socleL = widthCanva / 10
socleR = 9 * widthCanva / 10
Thick = 20

# Origin of the new coordinate system
Origin = (0, heightCanva)

# Coordinate transformation function
def passage(X, Y, center=Origin):
    return (X + center[0], - Y + center[1])

# Creation of the main window
root = Tk()

# Creation of the main canvas by specifying its width, height, and background
cnv = Canvas(root, width=widthCanva, height=heightCanva, bg="ivory")
cnv.pack()

# Creation of the base
A = passage(socleL, 0)
B = passage(socleR, Thick)
# Create a black rectangle whose height is Thick and width is socleL - socleR
cnv.create_rectangle(A, B, fill="black")

# Creation of the stems
for i in range(3):
    # Position on the x value of the origin
    x = (i + 1) * Distance - Thick / 2
    A = passage(x, 0)
    B = passage(x + Thick, Top)
    # Create a black rectangle whose height is Top and width is Thick.
    cnv.create_rectangle(A, B, fill="black")

# Event handling (main loop)
root.mainloop()
