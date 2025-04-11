def menu():
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((460, 750))
    clock = pygame.time.Clock()

    bg = pygame.image.load("Wordie Logo.png").convert()
    largebg = pygame.transform.scale(bg, (460, 75))

    ENGLISH_BUTTON = pygame.image.load("English Button.png").convert()
    ENGLISH_BUTTON_LARGE = pygame.transform.scale(ENGLISH_BUTTON, (420, 69))

    MATHS_BUTTON = pygame.image.load("Maths Button.png").convert()
    MATHS_BUTTON_LARGE = pygame.transform.scale(MATHS_BUTTON, (420, 69))

    COMPSCI_BUTTON = pygame.image.load("CompSci Button.png").convert()
    COMPSCI_BUTTON_LARGE = pygame.transform.scale(COMPSCI_BUTTON, (420, 69))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                MENU_MOUSE_POS_X, MENU_MOUSE_POS_Y = MENU_MOUSE_POS

                if 24 <= MENU_MOUSE_POS_X <= 438 and 207 <= MENU_MOUSE_POS_Y <= 265:
                    print("Maths")
                    game("Maths")
                elif 24 <= MENU_MOUSE_POS_X <= 438 and 283 <= MENU_MOUSE_POS_Y <= 346:
                    print("English")
                    game("English")
                elif 24 <= MENU_MOUSE_POS_X <= 438 and 367 <= MENU_MOUSE_POS_Y <= 424:
                    print("Computer Science")
                    game("Computer Science")

        screen.fill("white")
        screen.blit(largebg, (0, 50))
        screen.blit(MATHS_BUTTON_LARGE, (20, 200))
        screen.blit(ENGLISH_BUTTON_LARGE, (20, 280))
        screen.blit(COMPSCI_BUTTON_LARGE, (20, 360))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def game(subjectchoice):
    import pygame
    import sys
    import random

    pygame.init()
    clock = pygame.time.Clock()
    
    index=0
    Width=500
    Height=750
    
    x=35
    y=85
    value=75
    
    Lines=[80,155,230,305,380,455]
    
    whitecol=(255,255,255)
    blackcol=(0,0,0)
    redcol=(255,0,0)
    greencol=(112,206,113)
    orangecol=(237,212,28)
    greycol=(190,190,190)
    
    print(subjectchoice)
    if subjectchoice=="Maths":
    
        with open("MathsWords.txt", "r") as file: 
            allText = file.read() 
            words = list(map(str, allText.split()))
        
    elif subjectchoice=="English":
        with open("EnglishWords.txt", "r") as file: 
            allText = file.read() 
            words = list(map(str, allText.split()))
    
    elif subjectchoice=="Computer Science":
        with open("Computer ScienceWords.txt", "r") as file: 
            allText = file.read() 
            words = list(map(str, allText.split())) 
   
    chosenword = random.choice(words)
    

    print(chosenword)

    screen = pygame.display.set_mode((Width, Height))
    screen.fill(whitecol)
    bg = pygame.image.load("Wordie Logo.png").convert()
    largebg=pygame.transform.scale(bg,(460,75))
    screen.blit(largebg, (100,100))


    


    boxcolors=[whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol,whitecol]
    xpositions=[32,112,192,272,352]
    ypositions=[82,157,232,307,382,457]


    def drawcolorboxes(screen, boxcolors):
        for i, color in enumerate(boxcolors):
            x = 32 + (i % 5) * 80
            y = 82 + (i // 5) * 75
            pygame.draw.rect(screen, color, pygame.Rect(x, y, 56, 56))

    def drawboxes(screen, lines, blackcol):
        for y in lines:
            for x in range(30, 391, 80):
                pygame.draw.rect(screen, blackcol, pygame.Rect(x, y, 60, 60), 2)
        
    base_font = pygame.font.Font("CourierPrime-Bold.ttf", 47)
    winlose_font = pygame.font.Font("CourierPrime-Bold.ttf", 30) 
    user_text = ''
    
    


    input_rect = pygame.Rect(x, y, 360, 60)

    imp = pygame.image.load("Babycat.jpg").convert()
    smallimp=pygame.transform.scale(imp,(200,100))
    
    imp2 = pygame.image.load("Bigcat.jpg").convert()
    smallimp2=pygame.transform.scale(imp2,(400,100))
    

    def leave_word1(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,85))
        if int(score1int)<3:
            scorecol=redcol
        elif int(score1int)>2 and int(score1int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score1=base_font.render(score1int,True,scorecol)
        screen.blit(score1, (x+380,85))
        score1=base_font.render("/5",True,scorecol)
        screen.blit(score1, (x+400,85))        
        

    def leave_word2(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,160))
        if int(score2int)<3:
            scorecol=redcol
        elif int(score2int)>2 and int(score2int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score2=base_font.render(score2int,True,scorecol)
        screen.blit(score2, (x+380,160))
        score2=base_font.render("/5",True,scorecol)
        screen.blit(score2, (x+400,160))         

    def leave_word3(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,235))
        if int(score3int)<3:
            scorecol=redcol
        elif int(score3int)>2 and int(score3int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score3=base_font.render(score3int,True,scorecol)
        screen.blit(score3, (x+380,235))
        score3=base_font.render("/5",True,scorecol)
        screen.blit(score3, (x+400,235)) 
        
    def leave_word4(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,310))
        if int(score4int)<3:
            scorecol=redcol
        elif int(score4int)>2 and int(score4int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score4=base_font.render(score4int,True,scorecol)
        screen.blit(score4, (x+380,310))
        score4=base_font.render("/5",True,scorecol)
        screen.blit(score4, (x+400,310)) 
        
    def leave_word5(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,385))
        if int(score5int)<3:
            scorecol=redcol
        elif int(score5int)>2 and int(score5int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score5=base_font.render(score5int,True,scorecol)
        screen.blit(score5, (x+380,385))
        score5=base_font.render("/5",True,scorecol)
        screen.blit(score5, (x+400,385)) 

    def leave_word6(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,460))
        if int(score6int)<3:
            scorecol=redcol
        elif int(score6int)>2 and int(score6int)<5:
            scorecol=orangecol
        else:
            scorecol=greencol
        score6=base_font.render(score6int,True,scorecol)
        screen.blit(score6, (x+380,460))
        score6=base_font.render("/5",True,scorecol)
        screen.blit(score6, (x+400,460)) 
        
    def retrytext(base_font):
        text=winlose_font.render('*Game Over*',True,redcol)
        text2=winlose_font.render('-Click Any Key-',True,redcol)
        text3=winlose_font.render('-To Retry-',True,redcol)
        text4=winlose_font.render('The Word Was:',True,blackcol)
        text5=winlose_font.render(chosenword,True,blackcol)
        
        textRect = text.get_rect()
        screen.blit(text, (x+90,525))
        screen.blit(text2, (x+55,560))
        screen.blit(text3, (x+100,595))
        screen.blit(text4, (x+75,630))
        screen.blit(text5, (x+140,665))
        screen.blit(smallimp, (x+80, 695))

    def wintext(base_font):
        text=winlose_font.render('*You Win*',True,greencol)
        text2=winlose_font.render('-Click Any Key-',True,greencol)
        text3=winlose_font.render('-To Retry-',True,greencol)
        screen.blit(text, (x+110,525))
        screen.blit(text2, (x+55,560))
        screen.blit(text3, (x+100,595))
        screen.blit(smallimp2, (x, 635))


    active1="false"
    active2="false"
    active3="false"
    active4="false"
    active5="false"
    active6="false"
    y1=""
    y2=""
    y3=""
    y4=""
    y5=""
    y6=""
    word1=""
    word2=""
    word3=""
    word4=""
    word5=""
    word6=""
    score1int=""
    score2int=""
    score3int=""
    score4int=""
    score5int=""
    score6int=""

    
    win="false"  
      
    while True:
        screen.fill(whitecol)
        screen.blit(largebg, (0,0))
        drawboxes(screen, Lines, blackcol)
        drawcolorboxes(screen, boxcolors)
        text_surface = base_font.render(user_text, True, (blackcol))
        
        nowhitetext="".join(user_text.split())
        if win=="true":
            wintext(base_font)


        if active1=="true":
            leave_word1(word1,x,y1)
        if active2=="true":
            leave_word2(word2,x,y2)
        if active3=="true":
            leave_word3(word3,x,y3)
        if active4=="true":
            leave_word4(word4,x,y4)        
        if active5=="true":
            leave_word5(word5,x,y5)
        if active6=="true":
            leave_word6(word6,x,y6)
            if win!="true":
                retrytext(base_font)
        
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
      
                
                if event.key == pygame.K_BACKSPACE:

      
                    user_text = user_text[:-3]
 
                elif event.key == pygame.K_RETURN and len(user_text) >= 15 or active6 == "true" or win == "true":
                    if win == "true":
                        pygame.quit()
                        game(subjectchoice)
                    elif active6 == "true":
                        print("The game should end here.")
                        pygame.quit()
                        game(subjectchoice)

                    i = 0
                    scoring = 0
                    
                    for i in range(min(len(chosenword), len(nowhitetext))):
                        if nowhitetext[i] in chosenword:
                            boxcolors[index] = orangecol
                            if chosenword[i] == nowhitetext[i]:
                                boxcolors[index] = greencol
                                scoring += 1
                        else:
                            boxcolors[index] = greycol
                        index += 1

                    if active1=="false":
                        active1="true"
                        word1=user_text
                        score1int=str(scoring)
                    elif active2=="false":
                        active2="true"
                        word2=user_text
                        score2int=str(scoring)
                    elif active3=="false":
                        active3="true"
                        word3=user_text
                        score3int=str(scoring)
                    elif active4=="false":
                        active4="true"
                        word4=user_text
                        score4int=str(scoring)
                    elif active5=="false":
                        active5="true"
                        word5=user_text
                        score5int=str(scoring)
                    elif active6=="false":
                        active6="true"
                        if nowhitetext!=chosenword:
                            retrytext(base_font)
                        word6=user_text
                        score6int=str(scoring)

                    user_text=''
                    y+=value
                                            
                
                elif event.key == pygame.K_ESCAPE:
                    menu()
                    
                
                alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                
            
                if nowhitetext==chosenword:
                    win="true"
                    print("win is true")
                    wintext(base_font)
                print(nowhitetext)
                    
                if active6 != "true":
                    if len(nowhitetext)<5:
                        letter=event.unicode
                        if letter in alphabet:
                            user_text += event.unicode
                            user_text=user_text + "  "
                            
                            user_text=user_text.upper()
                    else:
                        user_text=user_text
              
              

            

        
        if active6=="false" and win=="false":
            screen.blit(text_surface, (input_rect.x, y))

        
          
        
          

        pygame.display.flip() 
          

        clock.tick(60) 

menu()