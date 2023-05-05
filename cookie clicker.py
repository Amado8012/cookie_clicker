#gopher mash
#written by Dr. Mo, 11/10/2020
import pygame
import math #needed for square root function



pygame.init()#initializes Pygame
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((800,800))#creates game screen

#print(pygame.font.get_fonts())
#player variables
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('score:', False, (0, 200, 200))
text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 400
circY = 400
radius = 100

CookiePic = pygame.image.load("cookie_clicker/cookie.png") #remove the file path when running this in it's own directory
CookieRect = CookiePic.get_rect(topleft=(308,315.5))
CookieBigPic = pygame.image.load("cookie_clicker/cookiebig.png")
CookieBigRect = CookiePic.get_rect(topleft=(289.5,298.5))
big = False
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
      if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2) < radius:
       # print(math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2), radius)
        numClicks+=1
        #print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        if math.sqrt((mousePos[0]-circX)**2 + (mousePos[1]-circY)**2) < radius:
            big = True
        else:
           big = False
        mousePos = event.pos #refreshes mouse position
       #print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    
    ##pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    #print("clicks:", numClicks) #uncomment this once collision is set up
    text2 = font.render(str(int(numClicks)), 1, (0, 200, 200))
    screen.blit(text, (10, 10))
    screen.blit(text2, (110, 10))

    screen.blit(CookiePic, CookieRect)
    if big:
       screen.blit(CookieBigPic, CookieBigRect)
    pygame.display.flip()
    


#end game loop##############################################

pygame.quit()

