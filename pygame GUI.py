#Module imports
import pygame

#Functions & procedures
def background(x,y):
    bg = pygame.image.load("images/bg.png")
    gameDisplay.blit(bg, (0,0))

#Colours
black = ('#00000000')
white = ('#ffffffff')

#Main game
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Project')

clock = pygame.time.Clock()

crashed = False 
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(black)
    background(0,0)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
