
# coding: utf-8

# In[1]:


### Size of chess board
global N
N=8
import numpy as np
import pygame, sys
from pygame.locals import *


# In[2]:


def IsSafe(x,y,sol):
    return (x>=0 and x<N and y>=0 and y<N and sol[x][y]==-1)
    


# In[3]:


def graphicTour(N,L_coor):
        horse = pygame.image.load("knight.png")

        # Initialize window size and title:
        pygame.init()
        window = pygame.display.set_mode((32*N,32*N))
        pygame.display.set_caption("Knight's Tour")
        background = pygame.image.load("chess.png")
        index = 0

        # Text:
        font = pygame.font.SysFont("Ubuntu",16)
        text = []
        surface = []

        while True:
            # Fill background:
            window.blit(background,(0,0))
            if index < N*N:
                #print(index)
                window.blit(horse,(L_coor[index][0]*32,L_coor[index][1]*32))
                text.append(font.render(str(index+1),True,(255,255,255)))
                surface.append(text[index].get_rect())
                surface[index].center = (L_coor[index][0]*32+16,L_coor[index][1]*32+16)
                index += 1
            else:
                window.blit(horse,(L_coor[index-1][0]*32,L_coor[index-1][1]*32))
            for x in range(10000000):
                pass
            # Check events on window:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pygame.quit()
                        sys.exit()

            for i in range(index):
                window.blit(text[i],surface[i])

            # Update window:
            pygame.display.update()


# In[10]:


def solveKT():
    ### Initialize matrix
    sol=np.zeros((N,N), dtype=np.int)
    for x in range(0,N):
        for y in range(0,N):
            sol[x][y] = -1;
    xMove = [2,1,-1,-2,-2,-1, 1, 2]
    yMove = [1,2,2,1,-1,-2,-2, -1]
    sol[0][0]=0
    if (solveKTUtil(0, 0, 1, sol, xMove, yMove) == False):
    
        print("Solution does not exist")
        return False
    
    else:
        print(sol)
        k = 0
        L = []
        while k <= (N*N)-1:
            for i in range(N):
                for j in range(N):
                    #print(k)
                    if sol[i][j] == k:
                        L.append([i,j])
                        k += 1
                        #print("k: "+str(k))
        #print(sol)
        if len(L) == 0:
            print("Didn't find a solution.")
        print("Knights' positions: ", L)

        if N <= 32:
            graphicTour(N,L)
 
    return True


# In[11]:


def solveKTUtil(x,y,movei,sol,xMove,yMove):
    if (movei == N*N):
        return True
 
    ##Try all next moves from the current coordinate x, y */
    for k in range(0,8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if (IsSafe(next_x, next_y, sol)):
            sol[next_x][next_y] = movei
            if (solveKTUtil(next_x, next_y, movei+1, sol,
                         xMove, yMove) == True):
                 return True
            else:
                sol[next_x][next_y] = -1
    
   
 
    return False


# In[12]:


if __name__ == '__main__':
    solveKT()

