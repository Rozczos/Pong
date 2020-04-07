
import pygame, sys
from objects import *
from movement import *

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Drawing objects
player = Player(screen, screen_width, screen_height).draw()
opponent = Opponent(screen, screen_width, screen_height).draw()
ball = Ball(screen, screen_width, screen_height).draw()

move_ball = Ball_move(screen, screen_width, screen_height, ball, player, opponent)
move_player = Player_move(screen, screen_width, screen_height, player)
move_opponent = Opponent_move(screen, screen_width, screen_height, opponent, ball)

while True:
    #Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Moving objects
    move_ball.move()
    move_player.move()
    move_opponent.move()

    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

	# Updating the window 
    pygame.display.flip()
    clock.tick(60)
