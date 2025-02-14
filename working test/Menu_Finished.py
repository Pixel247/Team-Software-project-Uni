import pygame

pygame.init()
screen = pygame.display.set_mode((460, 750))
clock = pygame.time.Clock()

running = True
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
    



    for event in pygame.event.get():    
        if event.type == pygame.MOUSEBUTTONDOWN :
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_MOUSE_POS_X, MENU_MOUSE_POS_Y = MENU_MOUSE_POS
            CLICK = True
            if (CLICK == True) and (24 <= MENU_MOUSE_POS_X <= 438) and (207 <= MENU_MOUSE_POS_Y <= 265):
                print("Maths")
#Dequote stuff  #wordList = maths
                #pygame.quit()
                #game("maths")
            elif (CLICK == True) and (24 <= MENU_MOUSE_POS_X <= 438) and (283 <= MENU_MOUSE_POS_Y <= 346):
                print("English")
                #wordList = english
                #pygame.quit()
                #game("english")
            elif (CLICK == True) and (24 <= MENU_MOUSE_POS_X <= 438) and (367 <= MENU_MOUSE_POS_Y <= 424):
                print("Computer Science")
                #wordList = computerscience
                #pygame.quit()
                #game("computer science")

    
    CLICK = False
    pygame.display.flip()

    clock.tick(60)  

pygame.quit()





