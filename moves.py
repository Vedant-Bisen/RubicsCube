from initial import *

#This is where all the moves will be stored

def front():
    temp1 = FRONT[0][0]
    temp2 = FRONT[0][1]

    FRONT[0][0] = FRONT[2][0]
    FRONT[0][1] = FRONT[1][0]

    FRONT[2][0] = FRONT[2][2]
    FRONT[1][0] = FRONT[2][1]

    FRONT[2][2] = FRONT[0][2]
    FRONT[2][1] = FRONT[1][2]

    FRONT[0][2] = temp1
    FRONT[1][2] = temp2


    tmp1 = TOP[2][0]
    tmp2 = TOP[2][1]
    tmp3 = TOP[2][2]

    TOP[2][0] = LEFT[0][2]
    TOP[2][1] = LEFT[1][2]
    TOP[2][2] = LEFT[2][2]

    LEFT[0][2] = BOTTOM[0][0]
    LEFT[1][2] = BOTTOM[0][1]
    LEFT[2][2] = BOTTOM[0][2]

    BOTTOM[0][0] = RIGHT[2][0]
    BOTTOM[0][1] = RIGHT[1][0]
    BOTTOM[0][2] = RIGHT[0][0]

    RIGHT[2][0] = tmp1
    RIGHT[1][0] = tmp2
    RIGHT[0][0] = tmp3

def back():
    temp1 = BACK[0][0]
    temp2 = BACK[0][1]

    BACK[0][0] = BACK[2][0]
    BACK[0][1] = BACK[1][0]

    BACK[2][0] = BACK[2][2]
    BACK[1][0] = BACK[2][1]

    BACK[2][2] = BACK[0][2]
    BACK[2][1] = BACK[1][2]

    BACK[0][2] = temp1
    BACK[1][2] = temp2


    tmp1 = TOP[0][0]
    tmp2 = TOP[0][1]
    tmp3 = TOP[0][2]

    TOP[0][0] = RIGHT[2][2]
    TOP[0][1] = RIGHT[1][2]
    TOP[0][2] = RIGHT[0][2]

    RIGHT[2][2] = BOTTOM[2][0]
    RIGHT[1][2] = BOTTOM[2][1]
    RIGHT[0][2] = BOTTOM[2][2]

    BOTTOM[2][0] = LEFT[0][0]
    BOTTOM[2][1] = LEFT[1][0]
    BOTTOM[2][2] = LEFT[2][0]

    LEFT[0][0] = tmp1
    LEFT[1][0] = tmp2
    LEFT[2][0] = tmp3

def top():
    temp1 = TOP[0][0]
    temp2 = TOP[0][1]

    TOP[0][0] = TOP[2][0]
    TOP[0][1] = TOP[1][0]

    TOP[2][0] = TOP[2][2]
    TOP[1][0] = TOP[2][1]

    TOP[2][2] = TOP[0][2]
    TOP[2][1] = TOP[1][2]

    TOP[0][2] = temp1
    TOP[1][2] = temp2


    tmp1 = FRONT[0][0]
    tmp2 = FRONT[0][1]
    tmp3 = FRONT[0][2]

    FRONT[0][0] = RIGHT[0][0]
    FRONT[0][1] = RIGHT[0][1]
    FRONT[0][2] = RIGHT[0][2]

    RIGHT[0][0] = BACK[0][0]
    RIGHT[0][1] = BACK[0][1]
    RIGHT[0][2] = BACK[0][2]

    BACK[0][0] = LEFT[0][0]
    BACK[0][1] = LEFT[0][1]
    BACK[0][2] = LEFT[0][2]

    LEFT[0][0] = tmp1
    LEFT[0][1] = tmp2
    LEFT[0][2] = tmp3

def bottom():
    temp1 = BOTTOM[0][0]
    temp2 = BOTTOM[0][1]

    BOTTOM[0][0] = BOTTOM[2][0]
    BOTTOM[0][1] = BOTTOM[1][0]

    BOTTOM[2][0] = BOTTOM[2][2]
    BOTTOM[1][0] = BOTTOM[2][1]

    BOTTOM[2][2] = BOTTOM[0][2]
    BOTTOM[2][1] = BOTTOM[1][2]

    BOTTOM[0][2] = temp1
    BOTTOM[1][2] = temp2


    tmp1 = FRONT[2][0]
    tmp2 = FRONT[2][1]
    tmp3 = FRONT[2][2]

    FRONT[2][0] = LEFT[2][0]
    FRONT[2][1] = LEFT[2][1]
    FRONT[2][2] = LEFT[2][2]

    LEFT[2][0] = BACK[2][0]
    LEFT[2][1] = BACK[2][1]
    LEFT[2][2] = BACK[2][2]

    BACK[2][0] = RIGHT[2][0]
    BACK[2][1] = RIGHT[2][1]
    BACK[2][2] = RIGHT[2][2]

    RIGHT[2][0] = tmp1
    RIGHT[2][1] = tmp2
    RIGHT[2][2] = tmp3

def left():
    temp1 = LEFT[0][0]
    temp2 = LEFT[0][1]

    LEFT[0][0] = LEFT[2][0]
    LEFT[0][1] = LEFT[1][0]

    LEFT[2][0] = LEFT[2][2]
    LEFT[1][0] = LEFT[2][1]

    LEFT[2][2] = LEFT[0][2]
    LEFT[2][1] = LEFT[1][2]

    LEFT[0][2] = temp1
    LEFT[1][2] = temp2


    tmp1 = TOP[0][0]
    tmp2 = TOP[1][0]
    tmp3 = TOP[2][0]

    TOP[0][0] = BACK[2][2]
    TOP[1][0] = BACK[1][2]
    TOP[2][0] = BACK[0][2]

    BACK[2][2] = BOTTOM[0][0]
    BACK[1][2] = BOTTOM[1][0]
    BACK[0][2] = BOTTOM[2][0]

    BOTTOM[0][0] = FRONT[0][0]
    BOTTOM[1][0] = FRONT[1][0]
    BOTTOM[2][0] = FRONT[2][0]

    FRONT[0][0] = tmp1
    FRONT[1][0] = tmp2
    FRONT[2][0] = tmp3

def right():
    temp1 = RIGHT[0][0]
    temp2 = RIGHT[0][1]

    RIGHT[0][0] = RIGHT[2][0]
    RIGHT[0][1] = RIGHT[1][0]

    RIGHT[2][0] = RIGHT[2][2]
    RIGHT[1][0] = RIGHT[2][1]

    RIGHT[2][2] = RIGHT[0][2]
    RIGHT[2][1] = RIGHT[1][2]

    RIGHT[0][2] = temp1
    RIGHT[1][2] = temp2


    tmp1 = TOP[0][2]
    tmp2 = TOP[1][2]
    tmp3 = TOP[2][2]

    TOP[0][2] = FRONT[0][2]
    TOP[1][2] = FRONT[1][2]
    TOP[2][2] = FRONT[2][2]

    FRONT[0][2] = BOTTOM[0][2]
    FRONT[1][2] = BOTTOM[1][2]
    FRONT[2][2] = BOTTOM[2][2]

    BOTTOM[0][2] = BACK[2][0]
    BOTTOM[1][2] = BACK[1][0]
    BOTTOM[2][2] = BACK[0][0]

    BACK[2][0] = tmp1
    BACK[1][0] = tmp2
    BACK[0][0] = tmp3

