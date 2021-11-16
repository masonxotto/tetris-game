#Tetris
import pygame
import string
import sys
import random
import time

pygame.init()

display_width = 800
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
pace = 60
score = 0

def gameBorder(left, right, top, bottom):
    borderLeft = pygame.Rect(0, 0, 200, 800)
    pygame.draw.rect(screen, left, borderLeft, 0)
    borderRight = pygame.Rect(600, 0, 200, 800)
    pygame.draw.rect(screen, right, borderRight, 0)
    borderTop = pygame.Rect(200, 0, 400, 100)
    pygame.draw.rect(screen, top, borderTop, 0)
    borderBottom = pygame.Rect(200, 740, 400, 100)
    pygame.draw.rect(screen, bottom, borderBottom, 0)

def playfieldGrid(gridColor):
    for x in range(200, 600, 40):
        for y in range(100, 720, 40):
            grid = pygame.Rect(x, y, 40, 40)
            pygame.draw.rect(screen, gridColor, grid, 1)

def game():
    #game
    exitGame = False

    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame = True
        
        screen.fill((64,64,64)) #grey
        gameBorder((32,32,32), (32,32,32), (32,32,32), (32,32,32)) #dark grey
        playfieldGrid((102,102,255)) #blue

        pygame.display.update()
        clock.tick(pace)

def main():

    #this runs the game
    game()
    
    pygame.quit()
    sys.exit()

req_version = (3,10)
curr_version = sys.version_info
if curr_version >= req_version:
    if __name__ == '__main__':
        main()
else:
    # prompt user to update python
    print("Please update your python version to 3.10 or greater")