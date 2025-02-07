def game():
    import pygame
    import sys
    import random

    pygame.init()
    clock = pygame.time.Clock()


    Width=460
    Height=750
    whitecol=(255,255,255)
    blackcol=(0,0,0)
    redcol=(255,0,0)
    greencol=(0,255,0)
    
    wordlist=["HOUSE","HORSE"]
    chosenword=random.choice(wordlist)
    print(chosenword)

    screen = pygame.display.set_mode((Width, Height))
    screen.fill(whitecol)
    bg = pygame.image.load("C:\\Users\\samre\\OneDrive - University of Hertfordshire\\University\\TSP\\Test\\Wordie Logo.png").convert()
    largebg=pygame.transform.scale(bg,(460,75))
    screen.blit(largebg, (100,100))


    Lines=[30,105,180,255,330,405]

    def drawboxes(Lines):
        for i in Lines:
            pygame.draw.rect(screen, blackcol, pygame.Rect(30, i, 60, 60),  2)
            #pygame.draw.rect(screen, redcol, pygame.Rect(32, 32, 56, 56))
            pygame.draw.rect(screen, blackcol, pygame.Rect(110, i, 60, 60),  2)
            pygame.draw.rect(screen, blackcol, pygame.Rect(190, i, 60, 60),  2)
            pygame.draw.rect(screen, blackcol, pygame.Rect(270, i, 60, 60),  2)
            pygame.draw.rect(screen, blackcol, pygame.Rect(350, i, 60, 60),  2)
        

    base_font = pygame.font.Font("CourierPrime-Bold.ttf", 47) 
    user_text = ''

    x=35
    y=35
    value=75

    # text position
    input_rect = pygame.Rect(x, y, 360, 60)

    #images
    imp = pygame.image.load("C:\\Users\\samre\\OneDrive - University of Hertfordshire\\University\\TSP\\Test\\Babycat.jpg").convert()
    smallimp=pygame.transform.scale(imp,(300,100))
    
    imp2 = pygame.image.load("C:\\Users\\samre\\OneDrive - University of Hertfordshire\\University\\TSP\\Test\\Bigcat.jpg").convert()
    smallimp2=pygame.transform.scale(imp2,(525,100))
    

    #leave words
    def leave_word1(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,35))

    def leave_word2(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,110))

    def leave_word3(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,185))
        
    def leave_word4(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,260))
        
    def leave_word5(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,335))

    def leave_word6(user_text,x,y):
        guess = base_font.render(user_text, True, blackcol)
        screen.blit(guess, (x,410))
        
    def retrytext(base_font):
        text=base_font.render('*Game Over*',True,redcol)
        text2=base_font.render('-Click Any Key-',True,redcol)
        text3=base_font.render('-To Retry-',True,redcol)
        textRect = text.get_rect()
        screen.blit(text, (x+35,500))
        screen.blit(text2, (x-13,550))
        screen.blit(text3, (x+50,600))
        screen.blit(smallimp, (x+75, 650))

    def wintext(base_font):
        text=base_font.render('*You Win*',True,greencol)
        text2=base_font.render('-Click Any Key-',True,greencol)
        text3=base_font.render('-To Retry-',True,greencol)
        screen.blit(text, (x+60,500))
        screen.blit(text2, (x-13,550))
        screen.blit(text3, (x+50,600))
        screen.blit(smallimp2, (x-30, 650))


        
        
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

    
    win="false"  
      
    while True:
        screen.fill(whitecol)
        screen.blit(largebg, (0,0))
        drawboxes(Lines)
        text_surface = base_font.render(user_text, True, (blackcol))
        
        nowhitetext="".join(user_text.split())
        if win=="true":
            wintext(base_font)

                
        #print(nowhitetext)
        
        if active1=="true":
            leave_word1(word1,x,y1)
            #retrytext(base_font)
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
            retrytext(base_font)
        
        
        for event in pygame.event.get(): 

            if event.type == pygame.KEYDOWN: 
      
                # Check for backspace 
                if event.key == pygame.K_BACKSPACE:

      
                    # get text input from 0 to -1 i.e. end. 
                    user_text = user_text[:-3]

                    
                elif event.key == pygame.K_RETURN and len(user_text)>=15 or active6=="true" or win=="true":
                    
                    if win=="true":
                        pygame.quit()
                        game()
                    elif active1=="false":
                        active1="true"
                        word1=user_text
                    elif active2=="false":
                        active2="true"
                        word2=user_text
                    elif active3=="false":
                        active3="true"
                        word3=user_text
                    elif active4=="false":
                        active4="true"
                        word4=user_text
                    elif active5=="false":
                        active5="true"
                        word5=user_text                    
                    elif active6=="false":
                        active6="true"
                        retrytext(base_font)
                        word6=user_text
                    elif active6=="true":
                        print("the game should end hereeee")
                        pygame.quit()
                        game()
                        
                        
                        
                    #if y1=="":
                        #y1=y

                    user_text=''
                    y+=value
                    
                    
                    



                # Unicode standard is used for string 
                # formation
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
              
              

            
        # render at position stated in arguments
        
        if active6=="false" and win=="false":
            screen.blit(text_surface, (input_rect.x, y))

        
          
        
          
        # display.flip() will update only a portion of the 
        # screen to updated, not full area 
        pygame.display.flip() 
          
        # clock.tick(60) means that for every second at most 
        # 60 frames should be passed. 
        clock.tick(60) 

game()