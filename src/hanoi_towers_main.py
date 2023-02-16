# -*- coding: utf-8 -*-
"""! This file contains the main procedure for
to execute the methods used in the algorithm of the towers of hanoi.

@author KESKES Nazim
@version 1.0.0
@since 15 Septembre 2022
"""
#Initialization
from tkinter import *

#Canvas
#Height and width of the main canvas
widthCanva = 1000
heightCanva = 400

#Rod
#Distance between two rods
Distance = widthCanva / 4

#Height of a rod
Top = 4.2 * heightCanva / 5

#Base
#Dimensions of the base
socleL = widthCanva / 10
socleR = 9 * widthCanva / 10
Thick = 20

#Disc
#Width of the largest disc
Base = widthCanva / 4.2

#Width offset between two discs
Offset = 20

#Height of a disc
Height = 40
#Spacing between two discs
Separator = 4

#Origin of the new coordinate system
Origin = (0, heightCanva)

# Creating the main window
root = Tk()





# Coordinate system transformation
def passage(X, Y, center=Origin):
    """! Function allowing to pass the coordinates (x,y) in a new base with new coordinates (x1,y1).
             @param tuple (x,y).
             @return tuple (x1,y1).
    """
    return (X + center[0], - Y + center[1])

# Moving a disc
def move(nro, src, des):
    """Function allowing to pass the coordinates of the source and the destination and calculate a new coordinates (dx,dy).
    Which represent the "dx" Distance and the "dy" Height that we have to move our initial canva. It's a recursive algorithm
    """
    i, hi = src
    j, hj = des
    # Move the target disc of index nro by the difference between the 2 indices (src - des) * the distance between the 2 rods
    dx = (j - i) * Distance
    # Move the target disc in y by the height of a disc * the difference between the 2 heights
    dy = -(hj - hi) * Height
    # Move the target
    cnv.move(ids[nro], dx, dy)

# Implement the Hanoi algorithm
def hanoi(ids, source, destination, temp, heights, done):
    """method that allows us to realise the hanoi algorithm in a list of disks (rectangles since they're already built).
    When a displacement is made, the height of the source rod is decreased and increased in the destination rod.
    """
    if ids:
        A = hanoi(ids[1:], source, temp, destination, heights, False)
        B = [(ids[0], (source, heights[source] - 1), (destination, heights[destination]))]
        heights[source] -= 1
        heights[destination] += 1
        C = hanoi(ids[1:], temp, destination, source, heights, False)
        if done:
            moves = list(enumerate(A + B + C))
            for (i, (nro, src, des)) in moves:
                cnv.after(1000 * (i + 1), move, nro, src, des)
        return A + B + C
    return []

# Creating the main canvas by specifying the height, width, and background
cnv = Canvas(root, width=widthCanva, height=heightCanva, bg="ivory")
cnv.pack()

#Creating the base
A = passage(socleL, 0)
B = passage(socleR, Thick)
#Creating a black rectangle with a height of Thick and a width of socleL-socleR
cnv.create_rectangle(A, B, fill="black")
print(A,B)

#Creating the rods
for i in range(3):
    #Positioning on an x-value of the origin
    x = (i + 1) * Distance - Thick / 2
    A = passage(x, 0)
    B = passage(x + Thick, Top)
    #Creating a black rectangle with a height of Top and a width of Thick
    cnv.create_rectangle(A, B, fill="black")

#The discs
#Initially, the number of discs is 4
n = 4
#Initially, the width of the rectangle is Base
w = Base

x = Distance - w / 2
y = Height / 2 + Separator

#Initializing the list of discs to an empty list
ids = []

for _ in range(n):
    A = passage(x, y, Origin)
    B = passage(x + w, y + Height, Origin)
    #Creating a red rectangle with a height of Height and a width of w
    rect = cnv.create_rectangle(A, B, fill="red", outline="")
    #Adding a disc to the list of discs
    ids.append(rect)
    #The new starting point for creating the rectangle shifts by Offset on x
    #and it rises by Height + a Separator to separate between the 2 discs with a small space
    x += Offset
    y += Height + Separator
    #The width of the rectangle is decreased by an Offset value on both ends
    w -= 2 * Offset

# Test the Hanoi algorithm for n = 4
hanoi(list(range(n)), 0, 1, 2, [n, 0, 0], True)
# Event handling (main loop)
root.mainloop()
