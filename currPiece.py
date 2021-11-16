#this is the current piece
import pygame
import string
import sys
import random
import time

from pieces import Piece

pygame.init()

class currentPiece(pygame.sprite.Sprite):
    '''
    This is the piece of the tetris block
    '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.x = x
        #self.y = y
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.x4 = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.y4 = 0
        self.width = 40
        self.height = 40
        self.pieces = pygame.sprite.Group()
        self.orientation = 2
        self.rotate = False

    def updatePiece(self, type, x, y):
        if type == "I":
            self.x1 = x
            self.y1 = y
            if (self.orientation % 2 == 0):
                self.x2 = self.x1 + 40
                self.x3 = self.x2 + 40
                self.x4 = self.x3 + 40
                self.y2 = self.y1
                self.y3 = self.y1
                self.y4 = self.y1
            if (self.orientation % 2 != 0):
                self.x2 = self.x1
                self.x3 = self.x1
                self.x4 = self.x1
                self.y2 = self.y1 + 40
                self.y3 = self.y2 + 40
                self.y4 = self.y3 + 40
        if type == "J":
            if (self.orientation == 1):
                self.x1 = x
                self.y1 = y
                self.x2 = self.x1
                self.x3 = self.x2 + 40
                self.x4 = self.x3 + 40
                self.y2 = self.y1 + 40
                self.y3 = self.y1 + 40
                self.y4 = self.y1 + 40
            if (self.orientation == 2):
                self.x1 = x
                self.y1 = y
                self.x2 = self.x1 + 40
                self.x3 = self.x1
                self.x4 = self.x1
                self.y2 = self.y1
                self.y3 = self.y2 + 40
                self.y4 = self.y3 + 40
            #WORK ON THIS
            if (self.orientation == 3):
                self.x1 = x
                self.y1 = y
                self.x2 = self.x1
                self.x3 = self.x2 + 40
                self.x4 = self.x3 + 40
                self.y2 = self.y1 + 40
                self.y3 = self.y1 + 40
                self.y4 = self.y1 + 40
            #WORK ON THIS
            if (self.orientation == 4):
                self.x1 = x
                self.y1 = y
                self.x2 = self.x1 + 40
                self.x3 = self.x1
                self.x4 = self.x1
                self.y2 = self.y1
                self.y3 = self.y2 + 40
                self.y4 = self.y3 + 40

    
    def renderPiece(self, screen, type, x, y):
        if pygame.key.get_pressed()[pygame.K_r] and self.rotate == False:
            self.rotate = True
            self.orientation += 1
        else:
            self.rotate  = False

        self.updatePiece(type, x, y)
        if type == "I":
            blue = pygame.transform.scale(pygame.image.load('blueBlock.png'), (40,40))
            screen.blit(blue, (self.x1,self.y1))
            screen.blit(blue, (self.x2,self.y2))
            screen.blit(blue, (self.x3,self.y3))
            screen.blit(blue, (self.x4,self.y4))
        if type == "J":
            blue = pygame.transform.scale(pygame.image.load('blueBlock.png'), (40,40))
            screen.blit(blue, (self.x1,self.y1))
            screen.blit(blue, (self.x2,self.y2))
            screen.blit(blue, (self.x3,self.y3))
            screen.blit(blue, (self.x4,self.y4))



    

    
        