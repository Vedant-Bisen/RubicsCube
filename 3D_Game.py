import pygame
from pygame.locals import *
import numpy as np
from math import sin, cos
import random
pygame.init()
WIDTH = 800
SCALE = 50

window = pygame.display.set_mode((WIDTH, WIDTH))
clock = pygame.time.Clock()


cube_points = [[i,j,k] for i in range(-3,5,2) for j in range(-3,5,2) for k in range(-3,5,2)]

rm = [[i,j,k] for i in range(-1,3,2) for j in range(-1,3,2) for k in range(-1,3,2)]

cube_points = [point for point in cube_points if point not in rm]


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

# main loop
while True:
    
    clock.tick(60)
    window.fill((0, 0, 0))

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
        y = points_2d[1] * SCALE + WIDTH / 2

        points.append([x, y])
        # print(points)
        i += 1
        pygame.draw.circle(window, (255, 255, 0), (x, y), 5)
   
    for connection in connections:
        p1, p2 = connection
        pygame.draw.line(window, (255, 255, 255), points[p1], points[p2])
    
 
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            move = True

        if event.type == pygame.MOUSEBUTTONUP:
            move = False

    if move:
        mouse_delta = pygame.mouse.get_rel()
        angle_x += mouse_delta[1] * -0.01
        angle_y += mouse_delta[0] * 0.01

    pygame.display.update()
