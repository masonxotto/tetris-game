#this is the pieces of the game
import pygame

pygame.init()

class Piece(pygame.sprite.Sprite):

    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
