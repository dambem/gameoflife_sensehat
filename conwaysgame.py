from sense_hat import SenseHat
import numpy as np
import time
import random

sense = SenseHat()
# Let's set the matrix, the datatype inside the matrix will be 3 integers to represent each color
gamematrix = np.zeros((8,8), dtype='i,i,i')
# r g b, red for dying, and green for alive
live = (0,255,0)
dead = (0,0,0)
dying =(255,0,0)

# generate random living squares, if above the set life percentage, will create a new spot
lifeperc = 0.5
for x in range(8):
 for y in range(8):
     if (random.random() >= lifeperc):
         gamematrix[x][y] = live

# Small helper function to check if living, uses 255 as you can't directly check two tuples
def islive(living):
    if (living[1] == live(1)):
        return True
    else:
        return False

# Function that checks for how many neighbours a cell has
def neighbours(matrix, posx, posy):
    # We only check the neighbouring couple (change this for more effects!)    
    offsets= (0,-1,1)
    #Initialise neighbour count at 0
    neighbour_count = 0
    for x in offsets:
        for y in offsets:
            try:
              # We are not a neighbour of ourselves!
              if (x==0 and y==0):
                  next
              # If there's a living neighbour, add it to the list            
              elif (islive(matrix[posx+x][posy+y])):
                  neighbour_count+=1
            except IndexError:
                next
    return neighbour_count

#Let's create the game of life
def gameoflife(matrix):
    # Before showing, we need to flatten our matrix into a single dimension     
    show = (matrix.flatten())
    # This displays the matrix on the sensehat    
    sense.set_pixels(show)
    # We start a new empty matrix    
    new_matrix = np.zeros((8,8), dtype='i,i,i')
    for x in range(8):
        for y in range(8):
            # For each cell, we check the amount of neighbours            
            num_live = neighbours(matrix,x,y)
            # Rule 1 of Conway's Game Of Life            
            if (islive(matrix[x][y])):
                if (num_live == 2 or num_live == 3):
                    new_matrix[x][y] = live
                else:
#                    Rule 3 of Conway's Game Of Life
                    new_matrix[x][y] = dying
            #   Rule 2 Of Conway's Game Of Life       
            else:
                if (num_live == 3):
                    new_matrix[x][y] = live
#    Pause slightly to allow for refresh
    time.sleep(1)
#    Recursive call with new matrix
    gameoflife(new_matrix)

#Finally, let's start the game!
gameoflife(gamematrix)
