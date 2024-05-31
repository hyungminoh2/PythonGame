import pygame
#want to import exit function only (to close the while loop, aka the game)
from sys import exit
pygame.init()
# width,height (0,0) is on the top left of screen
screen = pygame.display.set_mode((800,400))
# changes the title of the game
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #adding the test surface onto main screen        
    screen.blit(test_surface,(200,100))
    pygame.display.update()
    clock.tick(60)

    