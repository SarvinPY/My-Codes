import pygame
from constans import *
from init import *
from objects import *
import numpy as np

def show() :
    for item in sq_list :
        pygame.draw.rect(game_display , White ,  item)

def Circle(sq) :              # args that we need for draw a circle are : surface , color , center coordinate  and width
    row , col = sq//3 , sq%3 
    pygame.draw.circle(game_display , 
                    (255 , 0 , 0) , 
                    (CORDS[col] + Half_Tile , CORDS[row] + Half_Tile) , 
                    50 , 7)


def cross(sq) :               # args that we need for draw a cross are : surface , color , star_po , end_pos , width
    row , col = sq//3 , sq%3 
    pygame.draw.line(game_display , Black ,
                    (CORDS[col] + 20 , CORDS[row] + 20) , 
                    (CORDS[col] + Tile_Size - 20 , CORDS[row] + Tile_Size - 20) , 7)
    pygame.draw.line(game_display , Black , 
                    (CORDS[col] + 20 , CORDS[row] + Tile_Size - 20) , 
                    (CORDS[col] + Tile_Size - 20 , CORDS[row] + 20), 7)

def check_state(gb) :
    for i in range(3) :
        row = np.unique(gb[:][i])     # checks all rows
        col = np.unique(gb[i][:])     # checks all columns
        #---------------------------------------------------
        if len(row) == 1 and row != 0 :
            return row
        elif len(col) == 1 and col != 0 :
            return col
        #----------------------------------------------------
        if game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[0][0] != 0 :
            return game_board[1][1]
        elif game_board[0][2] == game_board[2][0] and game_board[2][0] == game_board[1][1] and game_board[0][2] != 0 :
            return game_board[1][1]
        #-----------------------------------------------------
        if 0 not in np.unique(game_board) :
            return("Tie")
    return "continue"