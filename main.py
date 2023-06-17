from initial import *
from moves import *


# Description: This is the main file for the Rubics Cube Solver
#This is going to be a Rubics cube solving alogirthm
#The cube will be represented as a 6x3x3 array



#This is the cube in its solved state
def PrintCube():
    print("                 ",  TOP[0])
    print("                 ",  TOP[1])
    print("                 ",  TOP[2])
    print(" ")
    print(LEFT[0]," ",  FRONT[0]," ", RIGHT[0]," ", BACK[0])
    print(LEFT[1]," ",  FRONT[1]," ", RIGHT[1]," ", BACK[1])
    print(LEFT[2]," ",  FRONT[2]," ", RIGHT[2]," ", BACK[2])
    print(" ")
    print("                 ", BOTTOM[0])
    print("                 ", BOTTOM[1])
    print("                 ", BOTTOM[2])


PrintCube()
front()
print("________________  ________________  ________________  ________________")
PrintCube()