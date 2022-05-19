from pygame.locals import *
import pygame

WIDTH = 700 # YOU CAN CHANGE THIS
HEIGHT = 700 # YOU CAN CHANGE THIS
WHITE = (255,255,255)
BLACK = (21,21,21)
FPS = 120

class Cross:
    def __init__(self, posX, posY, display):
        self.posX = posX
        self.posY = posY
        self.display = display
        self.height = 2000
        self.width = 1
    
    def create(self):
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.posX, self.posY, self.height, self.width))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.posX, self.posY, self.width, self.height))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.posX - self.height, self.posY, self.height, self.width))
        pygame.draw.rect(self.display, WHITE, pygame.Rect(self.posX, self.posY - self.height, self.width, self.height))

pygame.init()
pygame.font.init()
#CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Mouse | Cords")
font = pygame.font.SysFont("Comic Sans MS", 15)
run = True

cross = Cross(WIDTH / 2, HEIGHT / 2, SCREEN)

while run:
    #CLOCK.tick(FPS)
    MOUSE = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   
    SCREEN.fill(BLACK)
    text = font.render(f"X:{MOUSE[0]} Y:{MOUSE[1]}", False, WHITE)
    SCREEN.blit(text, (0,0))
    cross = Cross(MOUSE[0],MOUSE[1], SCREEN)
    cross.create()
    pygame.display.flip()

pygame.quit()
