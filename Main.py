import pygame as pg
import numpy as np
from math import*
from Maps import Maps
from Raycasting import Raycasting

pg.init()
screen_Size = (500,400)
screen = pg.display.set_mode(screen_Size)

pg.display.set_caption("FranEngine2")

player_Pos = [2,2]
move_Speed = 4
rot_Speed = 2
col_Radius = 0.1
fov = 60

ray_Step = fov/screen_Size[0]

direction = np.array([-1.0,0.0])
plane = [0.0,0.66]

#Rotation matrix

run = True

startFrameTime=0
Map = Maps.load(1)

while run:
    startFrameTime = pg.time.get_ticks()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

     # To rotate the view we have to rotate the camera plane
    if keys[pg.K_a]:
        old_direction = direction[0]

        direction[0] = direction[0] * cos(rot_Vel) - direction[1] * sin((rot_Vel))
        direction[1] = old_direction * sin(rot_Vel) + direction[1] * cos((rot_Vel)) 
        print(direction)
        old_Plane = plane[0]
        plane[0]= plane[0] * cos(rot_Vel) - plane[1] * sin(rot_Vel)
        plane[1]= old_Plane * sin(rot_Vel) + plane[1] * cos(rot_Vel)
        
        print(direction)
    if keys[pg.K_d]:
        old_direction = direction[0]
        direction[0] = direction[0] * cos(-rot_Vel) - direction[1] * sin(-rot_Vel)
        direction[1] = old_direction * sin(-rot_Vel) + direction[1] * cos(-rot_Vel) 
        old_Plane = plane[0]
        plane[0]= plane[0] * cos(-rot_Vel) - plane[1] * sin(-rot_Vel)
        plane[1]= old_Plane * sin(-rot_Vel) + plane[1] * cos(-rot_Vel)

    col_RadiusX = col_Radius * (direction[0]/abs(direction[0]))
    if direction[0]/abs(direction[0]) < 0:
        col_RadiusX -= 1

    if direction[1] == 0:
        col_RadiusY = col_Radius
    else:
        col_RadiusY = col_Radius * (direction[1]/abs(direction[1]))

    if (direction[1]/abs(direction[1])) < 0:
        col_RadiusY -= 1

    # No colisions
    if keys[pg.K_LEFT]:
        if Map[int(col_Radius * direction[0] + player_Pos[0] + move_Vel * (direction[0] * cos(radians(90)) - direction[1] * sin(radians(90))))][int(player_Pos[1])] == 0:
            player_Pos[0] += move_Vel * (direction[0] * cos(radians(90)) - direction[1] * sin(radians(90)))
        if Map[int(player_Pos[0])][int(col_Radius * direction[1] + player_Pos[1] + move_Vel * (direction[0] * sin(radians(90)) + direction[1] * cos(radians(90))))] == 0:
            player_Pos[1] += move_Vel * (direction[0] * sin(radians(90)) + direction[1] * cos(radians(90)))
    if keys[pg.K_RIGHT]:
        if Map[int(col_Radius * direction[0] + player_Pos[0] - move_Vel * (direction[0] * cos(radians(90)) - direction[1] * sin(radians(90))))][int(player_Pos[1])] == 0:
            player_Pos[0] -= move_Vel * (direction[0] * cos(radians(90)) - direction[1] * sin(radians(90)))
        if Map[int(player_Pos[0])][int(col_Radius * direction[1] + player_Pos[1] - move_Vel * (direction[0] * sin(radians(90)) + direction[1] * cos(radians(90))))] == 0:
            player_Pos[1] -= move_Vel * (direction[0] * sin(radians(90)) + direction[1] * cos(radians(90)))


    # And here we have some movement(conventional)
    # Colisions working
    if keys[pg.K_UP]:
    
        if Map[round(col_RadiusX + player_Pos[0] + direction[0] * move_Vel)][int(player_Pos[1])] == 0:
            player_Pos[0] += direction[0] * move_Vel
        if Map[int(player_Pos[0])][round(col_RadiusY + player_Pos[1] + direction[1]* move_Vel)] == 0:
            player_Pos[1] += direction[1] * move_Vel
    # Colisions not working
    if keys[pg.K_DOWN]: 
        if Map[int((-col_RadiusX) + player_Pos[0] - direction[0] * move_Vel)][int(player_Pos[1])] == 0:
            player_Pos[0] -= direction[0] * move_Vel
        if Map[int(player_Pos[0])][int(-col_RadiusY + player_Pos[1] - direction[1] * move_Vel)] == 0:
            player_Pos[1] -= direction[1] * move_Vel
    
    # Drawing celling and floor
    screen.fill((145,145,145)) #floor
    pg.draw.rect(screen,(60,255,220),(0,0,screen_Size[0],screen_Size[1]//2)) #ceilling  

    Raycasting.casting3D(screen,screen_Size,player_Pos,direction,plane,fov,Map,ray_Step)

    pg.display.update() 

    frame_time = (pg.time.get_ticks() - startFrameTime)/ 1000

    move_Vel = frame_time * move_Speed
    rot_Vel = frame_time * rot_Speed
    #fps counter
    fpscounter = str(round(1000/(pg.time.get_ticks()-startFrameTime + 0.0000000001)))
    
