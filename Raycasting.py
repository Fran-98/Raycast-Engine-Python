import pygame as pg
from math import*

class Raycasting:

    def casting3D(screen,screen_Size,player_Pos,direction,plane,fov,Map,ray_Step):
        hit_X = 0
        hit_Y = 0
        dist_X = 0
        dist_Y = 0
        near_hit = 0
        column = 0        
        Y = 0
        X = 0
        hit = False
        map_now = 0
        #We have to do the process for every column/pixel
        while column < screen_Size[0]-1:
            hit = False
            if direction[1]>0: #ray is facing up
                Y = floor(player_Pos[1]/64) * 64 - 1
            if direction[1]<0: #ray is facing down
                Y = floor(player_Pos[1]/64) * 64 + 64
            
            X = player_Pos[0] + abs(player_Pos[1]-Y)/tan(atan(direction[1]/direction[0]+radians(column * ray_Step - fov/2)))
            
            grid_X = int (X // 64) 

            grid_Y = int(Y // 64)
            # Finding dY
            if direction[1]>0: #ray is facing up
                dY = -64
            if direction[1]<0: #ray is facing down
                dY = 64

            dX = int(64//tan((atan(direction[1]/direction[0])+radians(column * ray_Step - fov / 2))))
            print("dX",dX)
            while hit is not True:
            #Check if there is a wall in [grid_X][grid_Y]
                print("Grid X", grid_X,"Grid_Y",grid_Y,"Map",Map[grid_X][grid_Y])
                if grid_X < 0 or grid_X > len(Map)-1:
                    hit = True
                    hit_Y = "False"
                if grid_Y < 0 or grid_Y > len(Map[0])-1:
                    hit = True
                    hit_Y = "False"
                if Map[grid_X][grid_Y] != 1:
                    hit = True
                    hit_Y = [grid_X,grid_Y]
                    
                # If there is no hit We should add dX and dY
                if hit is not True:
                    Y += dY
                    X += dX
                
                    grid_Y = int(Y // 64)
                    grid_X = int(X // 64)

            # The same from above but for intersections with vertical lines
            hit = False

            if direction[0]>0: #ray is facing right
                X = floor(player_Pos[0]/64) * 64 + 64
            if direction[0]<0: #ray is facing left
                X = floor(player_Pos[0]/64) * 64 - 1

            Y = player_Pos[1] + abs(player_Pos[0]-X)* tan(atan(direction[1]/direction[0])+radians(column * ray_Step - fov / 2))

            grid_X = floor (X / 64) 

            grid_Y = floor(Y / 64)

            # Finding dX
            if direction[0]>0: #ray is facing right
                dX = 64
            if direction[0]<0: #ray is facing left
                dX = -64

            dY = int(64*tan((atan(direction[1]/direction[0])+radians(column * ray_Step - fov / 2))))

            
            while hit is not True:
            #Check if there is a wall in [grid_X][grid_Y]
                if grid_Y < 0 or grid_Y > len(Map[0])-1:
                    hit = True
                    hit_X = "False"
                if grid_X < 0 or grid_X > len(Map)-1:
                    hit = True
                    hit_X = "False"
                
                if Map[grid_X][grid_Y] != 1:

                    hit = True
                    hit_X = [grid_X,grid_Y]
                    
                    
                # If there is no hit We should add dX and dY
                if hit is not True:
                    Y += dY
                    X += dX

                    grid_Y = int(Y // 64)
                    grid_X = int(X // 64)


            # Now we have to find wich hit is the nearest
            dist_Y = abs(player_Pos[0]-grid_X)/cos((atan(direction[1]/direction[0])+radians(column * ray_Step - fov / 2)))
            dist_X = abs(player_Pos[0]-grid_Y)/cos((atan(direction[1]/direction[0])+radians(column * ray_Step - fov / 2)))
        
            

            column += 1

            