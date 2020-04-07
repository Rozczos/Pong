
import pygame


class Object(object):
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height


class Ball(Object):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.ball_width = 20
        self.ball_height = 20

    def draw(self):
        # Drawing ball (starting x, starting y, width, height) - Ball is centered on the screen
        ball = pygame.Rect(self.screen_width/2 - self.ball_width/2, self.screen_height/2 - self.ball_height/2, self.ball_width, self.ball_height)
        return ball


class Paddle(Object):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.paddle_width = 8
        self.paddle_height = 140


class Player(Paddle):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)

    def draw(self):
        player = pygame.Rect(self.screen_width - (self.paddle_width + 2), self.screen_height/2 - self.paddle_height/2, self.paddle_width, self.paddle_height)
        return player


class Opponent(Paddle):
    def __init__(self, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)

    def draw(self):
        opponent = pygame.Rect(2, self.screen_height/2 - self.paddle_height/2, self.paddle_width, self.paddle_height)
        return opponent