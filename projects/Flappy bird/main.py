import pygame 
import sys
from files import *   
import random
import time


pygame.init()
win_sound = pygame.mixer.Sound('projects/Flappy bird/assets/sound/smb_stomp.wav')
game_over_sound = pygame.mixer.Sound('projects/Flappy bird/assets/sound/smb_mariodie.wav')
display_width = 576                    
display_height = 1024    
# Game display
main_screen = pygame.display.set_mode((display_width, display_height))               
clock = pygame.time.Clock()
floor_x = 0
gravity = 0.25
bird_movement = 0
pipe_list = []
game_status = True 
bird_list_index = 0
game_font = pygame.font.Font('Flappy.TTF', 40)
score = 0
high_score = 0
active_score = True
#--------------------------------------------------------------------------------

create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_pipe, 1200)
pygame.time.set_timer(create_flap, 100)
#--------------------------------------------------------------------------------

bird_list = [bird_image_down, bird_image_mid, bird_image_up]
bird_image = bird_list[bird_list_index]

def generate_pipe_rect():
    random_pipe = random.randrange(400, 800)
    pipe_rect_top = pipe_image.get_rect(midbottom=(700, random_pipe - 300))  # it's bottom pipe -------> explain why 700 & keywords
    pipe_rect_bottom = pipe_image.get_rect(midtop=(700, random_pipe))        # it's top pipe
    return pipe_rect_top, pipe_rect_bottom


def move_pipe_rect(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipes


def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            main_screen.blit(pipe_image, pipe)      # not out of display
        else:
            reversed_pipes = pygame.transform.flip(pipe_image, False, True)    # out of display , so flip it ------> explain why True
            main_screen.blit(reversed_pipes, pipe)


def check_collision(pipes):
    global active_score
    for pipe in pipes:
        if bird_image_rect.colliderect(pipe):
            game_over_sound.play()
            time.sleep(3)
            active_score = True
            return False
        if bird_image_rect.top <= -50 or bird_image_rect.bottom >= 900:
            game_over_sound.play()
            time.sleep(3)
            active_score = True
            return False
    return True


def bird_animation():
    new_bird = bird_list[bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_image_rect.centery))
    return new_bird, new_bird_rect


def display_score(status):
    if status == 'active':
        text1 = game_font.render(str(score), False, (255, 255, 255))    # make what we want to display
        text1_rect = text1.get_rect(center=(288, 100))                  # then we put it at rectangle
        main_screen.blit(text1, text1_rect)                             # then blit it
    if status == 'game_over':
        # score
        text1 = game_font.render(f'Score : {score}', False, (255, 255, 255))
        text1_rect = text1.get_rect(center=(288, 100))
        main_screen.blit(text1, text1_rect)
        # high score
        text2 = game_font.render(
            f'HighScore : {high_score}', False, (255, 255, 255))
        text2_rect = text2.get_rect(center=(288, 850))
        main_screen.blit(text2, text2_rect)


def update_score():
    global score, high_score, active_score
    if pipe_list:
        for pipe in pipe_list:
            if 95 < pipe.centerx < 105 and active_score:   # bird is stb and x = 100
                win_sound.play()
                score += 1
                active_score = False
            if pipe.centerx < 0:
                active_score = True
    if score > high_score:
        high_score = score
    return high_score


bird_image_rect = bird_image.get_rect(center=(100, 520))


#----------------------------------------------------------------------
# main codes: 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 7
            if event.key == pygame.K_r and game_status == False:
                game_status = True
                pipe_list.clear()
                bird_image_rect.center = (100, 512)
                bird_movement = 0
                score = 0
        if event.type == create_pipe:
            pipe_list.extend(generate_pipe_rect())
        if event.type == create_flap:
            if bird_list_index < 2:
                bird_list_index += 1
            else:
                bird_list_index = 0    # reset for a loop 
            bird_image, bird_image_rect = bird_animation()
    main_screen.blit(background_image, (0, 0))
    if game_status:
        main_screen.blit(bird_image, bird_image_rect)
        # checks for collision
        game_status = check_collision(pipe_list)
        # pipe move
        pipe_list = move_pipe_rect(pipe_list)
        display_pipes(pipe_list)
        # gravityand mivement
        bird_movement += gravity
        bird_image_rect.centery += bird_movement
        # showing score
        update_score()
        display_score('active')
    else:
        main_screen.blit(game_over_image, game_over_image_rect)
        display_score('game_over')
    #floor
    floor_x -= 1
    main_screen.blit(floor_image, (floor_x, 900))
    main_screen.blit(floor_image, (floor_x + 576, 900))
    if floor_x <= -576:
        floor_x = 0
    #----------------------------------------------------
    #updating
    pygame.display.update()
    clock.tick(90)












