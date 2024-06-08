import pygame
import sys    
from init import *
from constans import *
from objects import *
from functions import *
Turn = True
show()
while True :                                     # a game is a forever loop and only events can logically break it .  
    for event in pygame.event.get():             # there are two type of events : 1. closeing window    2.clicking (by mouse)
        if event.type == pygame.QUIT:
            pygame.quit()                        #this line deletes all datas from RAM
            sys.exit()                           #closes window
        elif event.type == pygame.MOUSEBUTTONUP :
            mouse_pos = pygame.mouse.get_pos()
            for sq in range(len(sq_list)) :
                if sq_list[sq].collidepoint(mouse_pos):
                    row , col = sq//3 , sq%3
                    if game_board[row][col] == 0 :
                        if Turn == 0 :             # loved this syntx , it means : " if Turn is True : "
                            Circle(sq)
                            Turn = not Turn
                            game_board[row][col] = 1
                        else:
                            cross(sq)
                            Turn = not Turn
                            game_board[row][col] = 2
            state =  check_state(game_board)
            if state != "continue" :
                if state != "Tie" :
                    print(f'player {state} won!')
                else:
                    print("Tie!")
    pygame.display.update()
    