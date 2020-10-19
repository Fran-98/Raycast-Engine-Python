import pygame as pg
from math import*

class Raycasting:

    def casting3D(screen,screen_Size,ray_Pos,direction,plane,fov,Map,ray_Step,dist_to_plane):
        
        column = 0        
    
        wall_Height = 0
        ray_Map_Pos = [0,0]
        hit = False
        color = [255,0,0]
        ray_Direction = [0,0]
        
        #We have to do the process for every column/pixel
        # Checking col with horizontal lines

        while column < screen_Size[0]-1:
            
            cameraX = 2 * column / screen_Size[0] - 1.0
            ray_Direction[0] = direction[0] + plane[0] * cameraX
            ray_Direction[1] = direction[1] + plane[1] * cameraX
 
            ray_Map_Pos[0] = int(ray_Pos[0]) 
            ray_Map_Pos[1] = int(ray_Pos[1])
            
            
            if ray_Direction[1] == 0:
                deltaDistX = 0
                deltaDistY = 1
            if ray_Direction[0] == 0:
                deltaDistX = 1
                deltaDistY = 0
            if ray_Direction[0] != 0 and ray_Direction[1] != 0:
                deltaDistX = abs(1/ray_Direction[0]) 
                deltaDistY = abs(1/ray_Direction[1])
            
            if ray_Direction[0] < 0:
                stepX = -1 
                sideDistX = (ray_Pos[0] - ray_Map_Pos[0]) * deltaDistX
            else:
                stepX = 1  
                sideDistX = (ray_Map_Pos[1] + 1.0 - ray_Pos[0]) * deltaDistX

            if ray_Direction[1] < 0:
                stepX = -1 
                sideDistY = (ray_Pos[1] - ray_Map_Pos[1]) * deltaDistY
            else:
                stepX = 1 
                sideDistY = (ray_Map_Pos[1] + 1.0 -ray_Pos[1]) * deltaDistY

            hit = False
            side = 0

            while hit:

                if sideDistX < sideDistY:
                    sideDistX += deltaDistX
                    ray_Map_Pos[0] = stepX
                    side = 0
                else:
                    sideDistY += deltaDistY
                    ray_Map_Pos[1] += stepY
                    side = 1
                if Map[ray_Map_Pos[0]][ray_Map_Pos[1]]:
                    hit = True
                    

            column += 1

            