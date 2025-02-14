import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((460, 750))
clock = pygame.time.Clock()
running = True
MENU_MOUSE_POS_X = 0
MENU_MOUSE_POS_Y = 0
CLICK = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    bg=pygame.image.load("Wordie Logo.png").convert()
    largebg=pygame.transform.scale(bg,(460,75))
    screen.blit(largebg,(0,50))
    
    ENGLISH_BUTTON =pygame.image.load("English Button.png").convert()
    ENGLISH_BUTTON_LARGE =pygame.transform.scale(ENGLISH_BUTTON,(420,69))
    screen.blit(ENGLISH_BUTTON_LARGE,(20,280))
    
    MATHS_BUTTON =pygame.image.load("Maths Button.png").convert()
    MATHS_BUTTON_LARGE =pygame.transform.scale(MATHS_BUTTON,(420,69))
    screen.blit(MATHS_BUTTON_LARGE,(20,200))
    
    COMPSCI_BUTTON =pygame.image.load("CompSci Button.png").convert()
    COMPSCI_BUTTON_LARGE =pygame.transform.scale(COMPSCI_BUTTON,(420,69))
    screen.blit(COMPSCI_BUTTON_LARGE,(20,360))
    
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    for event in pygame.event.get():    
        if event.type == pygame.MOUSEBUTTONDOWN :
            x = MENU_MOUSE_POS_X
            y = MENU_MOUSE_POS_Y
            CLICK = True
            if ((CLICK == True) and (27 <= MENU_MOUSE_POS_X <= 434) and (207 <= MENU_MOUSE_POS_Y <= 265)):
                print("Maths")
        #print(pygame.mouse.get_pos())
        
        #27,207 / 434, 265
    
    
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()






