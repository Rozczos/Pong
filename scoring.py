
import pygame


class Scoring(object):
    def __init__(self, screen, screen_width, screen_height, ball, points_opponent, points_player):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball = ball
        self.points_opponent = points_opponent
        self.points_player = points_player

        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.score1 = self.font.render(f'Opponent: {self.points_opponent}', True, (255,255,255))
        self.textRect1 = self.score1.get_rect()

        self.score2 = self.font.render(f'Player: {self.points_player}', True, (255,255,255))
        self.textRect2 = self.score2.get_rect()

    def print_score(self):
        self.textRect1.center = (200, 40) 
        self.screen.blit(self.score1, self.textRect1)

        self.textRect2.center = (600, 40) 
        self.screen.blit(self.score2, self.textRect2)