import pygame
from pygame.locals import *
import numpy as np
from math import sin, cos
import random

pygame.init()
WIDTH = 1920
HEIGHT = 1080
SCALE = 75


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


cube_points = [
    [i, j, k] for i in range(-6, 8, 2) for j in range(-6, 8, 2) for k in range(-6, 8, 2)
]

# rm = [[i,j,k] for i in range(-1,3,2) for j in range(-1,3,2) for k in range(-1,3,2)]

# cube_points = [point for point in cube_points if point not in rm]


m_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])


angle_x = angle_y = angle_z = 0


# Connecting lines
connections = []
for i in range(len(cube_points)):
    for j in range(i + 1, len(cube_points)):
        distance = sum(abs(a - b) for a, b in zip(cube_points[i], cube_points[j]))
        if distance == 2:
            connections.append((i, j))


move = False
disco = False

C = 0
C1 = C2 = 0
C3 = 255

# main loop
while True:
    COLOR = (C1,C2,C3)
    COLOR2 = (C2,C3,C1)
    COLOR3 = (C3,C1,C2)
    
    OFF_X = random.randint(-100,100)
    OFF_Y = random.randint(-100,100)

    


    clock.tick(60)
    window.fill(COLOR3)

    # Rotation Matrix
    roation_x = np.array(
        [[1, 0, 0], [0, cos(angle_x), -sin(angle_x)], [0, sin(angle_x), cos(angle_x)]]
    )

    roation_y = np.array(
        [[cos(angle_y), 0, sin(angle_y)], [0, 1, 0], [-sin(angle_y), 0, cos(angle_y)]]
    )

    roation_z = np.array(
        [[cos(angle_z), -sin(angle_z), 0], [sin(angle_z), cos(angle_z), 0], [0, 0, 1]]
    )

    points = []
    i = 0
    for point in cube_points:
        rotated_2d = np.matmul(roation_x, point)
        rotated_2d = np.matmul(roation_y, rotated_2d)
        rotated_2d = np.matmul(roation_z, rotated_2d)
        points_2d = np.matmul(m_matrix, rotated_2d)

        x = points_2d[0] * SCALE + WIDTH / 2 
        y = points_2d[1] * SCALE + HEIGHT / 2 

        points.append([x, y])
        # print(points)
        i += 1
        pygame.draw.circle(window, COLOR2, (x, y), 1)
    
    for connection in connections:
        p1, p2 = connection
        pygame.draw.line(window, COLOR, points[p1], points[p2],3)

    
 
    
    C += 1
    if C > 765:
        C = 0
    elif C > 510:
        C2 -= 1
        C3 += 1
    elif C > 255:
        C1 -= 1
        C2 += 1
    else:
        C3 -= 1
        C1 += 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            move = True

        if event.type == pygame.MOUSEBUTTONUP:
            move = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if disco:
                    disco = False
                else:
                    disco = True

    if disco:
        angle_x += 0.005
        angle_y += 0.005
        angle_z += 0.005




    if move:
        mouse_delta = pygame.mouse.get_rel()
        angle_x += mouse_delta[1] * -0.01
        angle_y += mouse_delta[0] * 0.01

    pygame.display.update()
