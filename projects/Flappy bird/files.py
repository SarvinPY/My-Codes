import pygame
background_image = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/bg2.png'))
floor_image = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/floor.png'))
bird_image_down = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/red_bird_down_flap.png'))
bird_image_mid = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/red_bird_mid_flap.png'))
bird_image_up = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/red_bird_up_flap.png'))
pipe_image = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/pipe_red.png'))
game_over_image = pygame.transform.scale2x(
    pygame.image.load('projects/Flappy bird/assets/img/message.png'))
game_over_image_rect = game_over_image.get_rect(center=(288, 512))

