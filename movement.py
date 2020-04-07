
import pygame
import random

class Move(object):
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

class Ball_move(Move):
    def __init__(self, screen, screen_width, screen_height, ball, player, opponent):
        super().__init__(screen, screen_width, screen_height)
        self.ball = ball
        self.ball_xspeed = 5
        self.ball_yspeed = 5
        self.player = player
        self.opponent = opponent
        self.points_player = 0
        self.points_opponent = 0
        
    def move(self):
        # Starting velocity
        self.ball.x += self.ball_xspeed
        self.ball.y += self.ball_yspeed
        
        # Border collision rules
        if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
            self.ball_yspeed *= -1

        if self.ball.left <= 0:
            self.points_player += 1
            self.ball_restart()
            return self.points_player

        if self.ball.right >= self.screen_width:
            self.points_opponent += 1
            self.ball_restart()
            return self.points_opponent

        # Paddle collision rules
        if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
            self.ball_xspeed *= -1

    def ball_restart(self):
        self.ball.center = (self.screen_width/2, self.screen_height/2)
        self.ball_xspeed *= random.choice((-1, 1))
        self.ball_yspeed *= random.choice((-1, 1))

class Player_move(Move):
    def __init__(self, screen, screen_width, screen_height, player):
        super().__init__(screen, screen_width, screen_height)
        self.player = player
        self.player_speed = 5

    def move(self):
        k = pygame.key.get_pressed()

        # Player movement keybinds
        if k[pygame.K_UP]:
            self.player.y -= self.player_speed
        if k[pygame.K_DOWN]:
            self.player.y += self.player_speed

        # Player border rules
        if self.player.top <= 0:
            self.player.top = 0
        if self.player.bottom >= self.screen_height:
            self.player.bottom = self.screen_height

class Opponent_move(Move):
    def __init__(self, screen, screen_width, screen_height, opponent, ball):
        super().__init__(screen, screen_width, screen_height)
        self.opponent = opponent
        self.opponent_speed = 5
        self.ball = ball

    def move(self):
        # Simple opponent AI
        if self.opponent.top < self.ball.y:
            self.opponent.y += self.opponent_speed
        if self.opponent.bottom > self.ball.y:
            self.opponent.y -= self.opponent_speed
        
        # Opponent border rules
        if self.opponent.top <= 0:
            self.opponent.top = 0
        if self.opponent.bottom >= self.screen_height:
            self.opponent.bottom = self.screen_height