
# coding: utf-8

# In[8]:


import sys
import numpy as np
import pygame, sys
from pygame.locals import *
class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()
    def graphicTour(self,N,L_coor):
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

    def generate_board(self):
        """
        Creates a nested list to represent the game board
        """
        for i in range(self.h):
            self.board.append([0]*self.w)

    def visualize_board(self):
        print("  ")
        print("------")
        Board = np.zeros((self.h,self.w),dtype=np.int)
        i=0
        for elem in self.board:
            Board[i,]=elem
            i+=1
        k = 1
        L = []
        while k <= self.h*self.w:
            for i in range(self.w):
                for j in range(self.h):
                    if Board[i][j] == k:
                        L.append([i,j])
                        k += 1
        print(Board)
        if len(L) == 0:
            print("Didn't find a solution.")
        print("Knights' positions: ", L)

        if self.h <= 32:
            self.graphicTour(self.h,L)
        print("------")
        print("  ")
    def generate_legal_moves(self, cur_pos):
        """
        Generates a list of legal moves for the knight to take next
        """
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

    def sort_lonely_neighbors(self, to_visit):
        """
        It is more efficient to visit the lonely neighbors first, 
        since these are at the edges of the chessboard and cannot 
        be reached easily if done later in the traversal
        """
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def tour(self, n, path, to_visit):
        """
        Recursive definition of knights tour. Inputs are as follows:
        n = current depth of search tree
        path = current path taken
        to_visit = node to visit
        """
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit) #append the newest vertex to the current point
        #print("Visiting: ",to_visit)

        if n == self.w * self.h: #if every grid is filled
            self.visualize_board()
            #print(path)
            print("Done!")
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            #If we exit this loop, all neighbours failed so we reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                #print("Going back to: ", path[-1])
            except IndexError:
                print("No path found")
                sys.exit(1)



# In[10]:


#Define the size of grid. We are currently solving for an 8x8 grid
kt = KnightsTour(8,8)
kt.tour(1, [], (0,0))

