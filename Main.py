import pygame as pg
import numpy as np
from math import*
from Maps import Maps
from Raycasting import Raycasting
pg.init()
screen_Size = (500,400)
screen = pg.display.set_mode(screen_Size)

pg.display.set_caption("FranEngine2")

player_Pos = [7,7]
move_Vel = 5
rot_Speed = 2
fov = 60

ray_Step = fov/screen_Size[0]

direction = [-1.0,0.0]
plane = [0.0,0.66]


run = True

fps=60
startFrameTime=0
Map = Maps.load(1)

while run:
    startFrameTime = pg.time.get_ticks()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    # Moving to the sides in dev
    # if keys[pg.K_LEFT] and player_Pos[0]>move_Vel:
    #     player_Pos[0]-=move_Vel
    # if keys[pg.K_RIGHT] and player_Pos[0]<screen_Size[0]-player_Size[0]:
    #     player_Pos[0]+=move_Vel

    # And here we have some movement(conventional)
    # if keys[pg.K_UP]:
    #     if Map[player_Pos[0]//64][player_Pos[1]]:
    #         player_Pos[0] += direction[0] * move_Vel
    #     if Map[player_Pos[0]][player_Pos[1]//64]:
    #         player_Pos[1] += direction[1] * move_Vel
    # if keys[pg.K_DOWN]:   
    #     if Map[player_Pos[0]//64][player_Pos[1]]:
    #         player_Pos[0] -= direction[0] * move_Vel
    #     if Map[player_Pos[0]][player_Pos[1]//64]:
    #         player_Pos[1] += direction[1] * move_Vel

    # To rotate the view we have to rotate the camera plane
    if keys[pg.K_a]:
        old_direction = direction[0]
        direction[0] = direction[0] * cos(radians(rot_Speed)) - direction[1] * sin((radians(rot_Speed)))
        direction[1] = old_direction * sin(radians(rot_Speed)) + direction[1] * cos((radians(rot_Speed))) 
        old_Plane = plane[0]
        plane[0]= plane[0] * cos(radians(rot_Speed)) - plane[1] * sin((radians(rot_Speed)))
        plane[1]= old_Plane * cos((radians(rot_Speed))) + plane[1] * cos((radians(rot_Speed)))
    if keys[pg.K_d]:
        old_direction = direction[0]
        direction[0] = direction[0] * cos(radians(rot_Speed)) - direction[1] * sin(radians(rot_Speed))
        direction[1] = old_direction * sin(radians(rot_Speed)) + direction[1] * cos(radians(rot_Speed)) 
        old_Plane = plane[0]
        plane[0]= plane[0] * cos(radians(rot_Speed)) - plane[1] * sin(radians(rot_Speed))
        plane[1]= old_Plane * cos(radians(rot_Speed)) + plane[1] * cos(radians(rot_Speed))
    
    
    
    # Drawing celling and floor
    screen.fill((145,145,145)) #floor
    pg.draw.rect(screen,(60,255,220),(0,0,screen_Size[0],screen_Size[1]//2)) #celling  

    Raycasting.casting3D(screen,screen_Size,player_Pos,direction,plane,fov,Map,ray_Step)

    pg.display.update() 

    #fps counter
    # fpscounter = str(round(1000/(pg.time.get_ticks()-startFrameTime)))

    

    pg.time.delay((int(1000/fps))-(pg.time.get_ticks()-startFrameTime))