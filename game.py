import pygame
from pygame.locals import *
from initial import *
from moves import *
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
ORANGE = (255, 165, 0)

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
         
        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))
         
        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
        self.border = pygame.draw.rect(self.surf, (0, 0, 0), self.rect, 1)

screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption("Rubics Cube Solver")

CUBE = [TOP,BOTTOM,LEFT,RIGHT,FRONT,BACK]

def color(CUBE,i,j,k):
    if "W" in CUBE[i][j][k]:
        return WHITE
    elif "Y" in CUBE[i][j][k]:
        return YELLOW
    elif "B" in CUBE[i][j][k]:
        return BLUE
    elif "G" in CUBE[i][j][k]:
        return GREEN
    elif "R" in CUBE[i][j][k]:
        return RED
    elif "O" in CUBE[i][j][k]:
        return ORANGE


for i in range(0,6):
    for j in range(0,3):
        for k in range(0,3):
            c = color(CUBE,i,j,k)
            number = CUBE[i][j][k][1]
            CUBE[i][j][k] = Square()
            CUBE[i][j][k].surf.fill(c)
            CUBE[i][j][k].border = pygame.draw.rect(CUBE[i][j][k].surf, (0, 0, 0), CUBE[i][j][k].rect, 1)
            
            



gameOn = True
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():
         
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
             
            # If the Backspace key has been pressed set
            # running to false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False
            if event.key == K_f:
                front()
            if event.key == K_b:
                back()
            if event.key == K_l:
                left()
            if event.key == K_r:
                right()
            if event.key == K_t:
                top()
            if event.key == K_o:
                bottom()
                 
        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False
        
    for i in range(0,6):
        for j in range(0,3):
            for k in range(0,3):
                #TOP
                if i == 0:
                    screen.blit(CUBE[i][j][k].surf, (225+25*k, 150+25*j))
                #BOTTOM
                elif i == 1:
                    screen.blit(CUBE[i][j][k].surf, (225+25*k, 300+25*j))
                #LEFT
                elif i == 2:
                    screen.blit(CUBE[i][j][k].surf, (150+25*k, 225+25*j))
                #RIGHT
                elif i == 3:
                    screen.blit(CUBE[i][j][k].surf, (300+25*k, 225+25*j))
                #FRONT
                elif i == 4:
                    screen.blit(CUBE[i][j][k].surf, (225+25*k, 225+25*j))
                #BACK
                elif i == 5:
                    screen.blit(CUBE[i][j][k].surf, (375+25*k, 225+25*j))
    

    pygame.display.flip()

