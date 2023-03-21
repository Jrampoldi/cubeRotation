# include libraries
import pygame, sys
import numpy as np
from math import *
# define constants
SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 60
# create window and clock 
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# declare projection matrix list
projection_matrix = [[1, 0, 0],
                    [0, 1, 0]]
# define angle for adjustment
angle = 0

# declare points for adjustment
new_points = []
# declare start points
cube_points = []
# append points of cube
cube_points.append(np.matrix([[-0.5], [-0.5], [0.5]]))
cube_points.append(np.matrix([[0.5], [-0.5], [0.5]]))
cube_points.append(np.matrix([[0.5], [0.5], [0.5]]))
cube_points.append(np.matrix([[-0.5], [0.5], [0.5]]))
cube_points.append(np.matrix([[-0.5], [-0.5], [-0.5]]))
cube_points.append(np.matrix([[0.5], [-0.5], [-0.5]]))
cube_points.append(np.matrix([[0.5], [0.5], [-0.5]]))
cube_points.append(np.matrix([[-0.5], [0.5], [-0.5]]))
# start infinite game loop
while True:
    # if user quits, close window/stop program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # control
    if len(new_points) > 2500:
        for points in range(len(new_points) - 1):
            new_points.pop()
    # clear window
    window.fill(BLACK)
    # rotation matracies that will be used for perspective change
    rotate_z = np.matrix([[cos(angle), -sin(angle), 0],
                        [sin(angle), cos(angle), 0],
                        [0, 0, 1]])
    rotate_y = np.matrix([[cos(angle), 0, sin(angle)],
                        [0, 1, 0],
                        [-sin(angle), 0, cos(angle)]])
    rotate_x = np.matrix([[1, 0, 0],
                        [0, cos(angle / 2 ), -sin(angle / 2)],
                        [0, sin(angle / 2), cos(angle / 2)]])



    
    # rotate and project to view   
    for points in cube_points:
        # rotate_Z = np.dot(rotate_z, points)
        rotate_Y = np.dot(rotate_y, points)
        rotate_X = np.dot(rotate_x, rotate_Y)
        rotate_Z = np.dot(rotate_z, rotate_X)
        rotate_Z = np.dot(rotate_z, rotate_Z)
        point_2d = np.dot(projection_matrix, rotate_Z)

        point_x = int(point_2d[0][0] * 150) + 400
        point_y = int(point_2d[1][0] * 150) + 400

        new_points.insert(0, [point_x, point_y])


        pygame.draw.circle(window, (70, 100, 130), (point_x, point_y), 5)
    # connect points via lines
    pygame.draw.line(window, (235, 235, 235), (new_points[0][0], new_points[0][1]), (new_points[4][0], new_points[4][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[1][0], new_points[1][1]), (new_points[5][0], new_points[5][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[2][0], new_points[2][1]), (new_points[6][0], new_points[6][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[3][0], new_points[3][1]), (new_points[7][0], new_points[7][1]), 3)

    pygame.draw.line(window, (235, 235, 235), (new_points[0][0], new_points[0][1]), (new_points[1][0], new_points[1][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[1][0], new_points[1][1]), (new_points[2][0], new_points[2][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[2][0], new_points[2][1]), (new_points[3][0], new_points[3][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[0][0], new_points[0][1]), (new_points[3][0], new_points[3][1]), 3)

    pygame.draw.line(window, (235, 235, 235), (new_points[4][0], new_points[4][1]), (new_points[5][0], new_points[5][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[5][0], new_points[5][1]), (new_points[6][0], new_points[6][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[6][0], new_points[6][1]), (new_points[7][0], new_points[7][1]), 3)
    pygame.draw.line(window, (235, 235, 235), (new_points[7][0], new_points[7][1]), (new_points[4][0], new_points[4][1]), 3)

    #pygame.draw.line(window, (235, 235, 235), (new_points[7][0], new_points[7][1]), (new_points[1][0], new_points[1][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[6][0], new_points[6][1]), (new_points[0][0], new_points[0][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[5][0], new_points[5][1]), (new_points[3][0], new_points[3][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[4][0], new_points[4][1]), (new_points[2][0], new_points[2][1]), 3)

    #pygame.draw.line(window, (235, 235, 235), (new_points[8][0], new_points[8][1]), (new_points[12][0], new_points[12][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[9][0], new_points[9][1]), (new_points[13][0], new_points[13][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[10][0], new_points[10][1]), (new_points[14][0], new_points[14][1]), 3)
    #pygame.draw.line(window, (235, 235, 235), (new_points[11][0], new_points[11][1]), (new_points[15][0], new_points[15][1]), 3)


            



 

    angle += 0.005
    # update changes
    pygame.display.update()
    # manage framerate
    clock.tick(FRAMES_PER_SECOND)




