#Import modules we require
import pygame
import random

# Initialize the game engine
pygame.init()

# Define all of our colors
BLACK = (38, 49,57)
BLACK3 = (10,10,10)
PlanetBlackShade = (36,36,36)
theLight = (60,72,82)
lightBlack=(6,20,29)
lightBlackPurple=(29,6,28)
brownGrey=(132,123,124)
darkBrown2=(100,93,92)
anotherGrey2=(42,53,53)
darkGrey=(5,24,32)
shadeGreen=(161,212,144)
darkGreen=(110,166,91)
darkBlue=(8,36,48)
REDBLACK =(57,38,38)
BLACK2 = (23,29,33)
PUREBLACK = (0,0,0,)
PUREWHITE= (255,255,255)
PUREWHITE2 = (223,223,223)
BRIGHTRED=(250,81,85)
RED= (189, 61, 64)
RED2 = (155, 53, 54)
RED3 = (134,45,48)
GREY1 = (87,86,86)
GREY2 = (73,74,74)
GREY3 = (62,62,62)
GREY4 = (107,107,107)
GREY5 = (94,94,94)
GREY6 = (76,76,76)
GREY7 = (40,40,40)
GREY8= (50,50,50)
WHITE = (158,158,156)
WHITE2 = (133,133,135)
WHITE3 = (105,106,106)
WHITE4= (109,108,106)
GREEN = (90,252,113)
GREEN2 = (73,183,83)
BLUE = (169,229,248)
BLUE2 = (61,61,190)
BLUE3=(53,60,155)
BLUE4 = (47,49,133)
BLUE5 = (32,34,94)
ORANGE = (253,189,99)
FIREB1 = (210,210,210)
FIREB2 = (220,220,220)
FIREB3 = (240, 240,240)
FIRER1 = (210,210,210)
FIRER2 = (220,220,220)
FIRER3 = (240, 240,240)
tintBlue=(211,218,220)
greyBlue=(135,153,163)
darkGrey=(90,94,103)
shadeGrey=(65,61,66)
tintBlack=(27,20,12)
tintGrey=(29,23,18)
anotherGrey=(20,14,8)
BLACKx = (14,7,1)
grey1=(230,230,230)
blue1=(11,38,58)
blue2=(7,28,42)
darkBlue=(5,24,38)
BEIGE=(252,255,222)
BROWN=(144,5,0)
BROWN2= (96,38,14)
lightYellow=(253,190,116)
lightBeige = (255, 205, 146)
YELLOW=(249,255,186)
fillYellow=(255,240,171)
shadeYellow=(255,164,57)
lightBrown=(253,152,33)
chocoBrown=(122,67,1)
brown1=(76,41,0)
brown2=(97,54,3)
brown3=(255,138,0)
brown4= (160,94,16)
YELLOW2=(255,176,82)
darkYellow=(241,252,114)
shadeBrown=(238,255,51)
neutralBrown=(234,255,0)
darkBrown=(255,238,0)
shadeRed=(158,8,0)
darkRed=(109,1,0)
shadePurple=(96,16,111)
darkPurple=(62,14,61)
shadeGrey2=(82,54,78)
darkerPurple=(34,4,16)
PURPLE=(157,32,174)

#Play background music + loud sound effects"
"This is our background music that plays throughout the whole animation"
music=pygame.mixer.Sound('sounds/BGMusic.wav')
music.play()
"""These sound effects only need to be loaded as they will be selectivley played
later"""
beep=pygame.mixer.Sound('sounds/Beep.wav')
qbeep=pygame.mixer.Sound('sounds/qBeep.wav')
detach=pygame.mixer.Sound('sounds/Detach.wav')
thrust=pygame.mixer.Sound('sounds/ThrustSound.wav')
elevate = pygame.mixer.Sound('sounds/Elevate.wav')
click = pygame.mixer.Sound('sounds/Click.wav')
heal = pygame.mixer.Sound('sounds/Heal.wav')
healed =pygame.mixer.Sound('sounds/Healed.wav')
fire =pygame.mixer.Sound('sounds/Fire Start.wav')
fire2 =pygame.mixer.Sound('sounds/Fire Out.wav')
door =pygame.mixer.Sound('sounds/Finish.wav')
finish = pygame.mixer.Sound ('sounds/Credits.wav')

#Set the width and height of the screen [width, height] and name of the animation
#window.
size = (701, 501)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Zenith")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Our main functions for our rockets and shuttles
"This is our right facing red shuttle (rocketship)"
def spaceShuttle (x,y):
        pygame.draw.polygon(screen, RED3, [[x-39, y-16],[x-37, y-9], [x-22, y-9], [x-27, y-16]])
        pygame.draw.polygon(screen, RED3, [[x-37, y+9],[x-39, y+16], [x-27, y+16], [x-22, y+9]])
        pygame.draw.rect(screen, RED, [x-40, y-9, 40, 9])
        pygame.draw.rect(screen, RED2, [x-40, y, 40, 9])
        pygame.draw.rect(screen, RED3, [x-15, y-9, 7, 9])
        pygame.draw.rect(screen, RED3, [x-15, y, 7, 9])
        pygame.draw.polygon(screen, GREY1, [[x-41, y+6],[x-43, y+8], [x-43, y], [x-41, y]])
        pygame.draw.polygon(screen, GREY2, [[x-43, y+8],[x-45, y+10], [x-45, y], [x-43, y]])
        pygame.draw.polygon(screen, GREY3, [[x-45, y+10],[x-47, y+12], [x-47, y], [x-45, y]])
        pygame.draw.polygon(screen, GREY4, [[x-41, y-6], [x-43, y-8],[x-43, y],[x-41, y]])
        pygame.draw.polygon(screen, GREY5, [[x-43, y-8], [x-45, y-10],[x-45, y],[x-43, y]])
        pygame.draw.polygon(screen, GREY6, [[x-45, y-10], [x-47, y-12],[x-47, y],[x-45, y]])
        pygame.draw.polygon(screen, RED, [[x, y-1],[x+11, y-1],[x, y-9]])
        pygame.draw.polygon(screen, RED2, [[x, y],[x+11, y],[x, y+8]])
"This is our right facing white fire used for both shuttles"
def spaceShuttleFire (f,a):
        pygame.draw.ellipse(screen, FIREB1, [f+30,a-3.5,27 ,9])
        pygame.draw.polygon(screen, FIREB1,  [[f+36, a-3.5], [f+30, a+3.5], [f+10, a]])
        pygame.draw.ellipse(screen, FIREB2, [f+39,a-2.5,16 ,6])
        pygame.draw.polygon(screen, FIREB2,  [[f+47, a-2.5], [f+40, a+2.5], [f+24, a]])
        pygame.draw.ellipse(screen, FIREB3, [f+47,a-1.0,8 ,3])
        pygame.draw.polygon(screen, FIREB3,  [[f+50, a-2], [f+44, a+1], [f+35, a]])
"This is our propelling rocket that soon detaches from the shuttle, rocket boosters not included"
def Rocket (v,b):
        pygame.draw.rect(screen, WHITE, [v+30,b+6, 87, 22])
        pygame.draw.rect(screen, WHITE2, [v+99,b+6, 12, 22])
        pygame.draw.polygon(screen, WHITE2, [[v+117,b+6],[v+117,b+27],[v+123,b+23],[v+123,b+10]])
        pygame.draw.rect(screen, WHITE, [v+124,b+11, 9, 13])
        pygame.draw.circle(screen, WHITE, [v+137,b+18],6)
        pygame.draw.rect(screen, WHITE2, [v+133,b+11, 4, 13])
        pygame.draw.polygon(screen, WHITE, [[v+29,b+6],[v+29,b+27],[v+15,b+22],[v+15,b+11]])
        pygame.draw.polygon(screen, WHITE3, [[v+15,b+23],[v+15,b+11],[v+3,b+6],[v+3,b+28]])
        pygame.draw.rect(screen, GREY6, [v-6,b+6, 9, 23])
"This the top booster, it is seperate becauses it detaches sepeartly"
def rocketBoosterTop (j,g):
        pygame.draw.circle(screen, WHITE4, [j+74,g+3],3)
        pygame.draw.rect(screen, GREY6, [j-6,g, 7, 6])
        pygame.draw.rect(screen, WHITE4, [j,g, 75, 6])
"This the bottom booster, it is seperate becauses it detaches sepeartly"
def rocketBoosterBottom (i,u):
        pygame.draw.circle(screen, WHITE4, [i+74,u+3],3)
        pygame.draw.rect(screen, GREY6, [i-6,u, 7, 6])
        pygame.draw.rect(screen, WHITE4, [i,u, 75, 6])
"This the blue left facing shuttle(rocketship)"
def leftBlueSpaceShuttle (p,d):
        pygame.draw.polygon (screen,BLUE2, [[p+9,d-9],[p-8,d],[p+10,d]])
        pygame.draw.polygon (screen,BLUE3, [[p+9,d+8],[p-8,d],[p+10,d]])
        pygame.draw.polygon(screen, BLUE4, [[p+38, d-24],[p+15, d-7], [p+45, d-7], [p+49, d-21]])
        pygame.draw.polygon(screen, BLUE4, [[p+15, d+7],[p+38, d+24], [p+49, d+21], [p+45, d+7]])
        pygame.draw.rect(screen, BLUE2, [p+10, d-9, 40, 9])
        pygame.draw.rect(screen, BLUE3, [p+10, d, 40, 9])
        pygame.draw.rect(screen, BLUE4, [p+13,d-9,4,18])
        pygame.draw.rect(screen, BLUE4, [p+20,d-9,4,18])
        pygame.draw.polygon(screen, GREY1, [[p+50, d+6],[p+52, d+8], [p+52, d], [p+50, d]])
        pygame.draw.polygon(screen, GREY2, [[p+52, d+8],[p+54, d+10], [p+54, d], [p+52, d]])
        pygame.draw.polygon(screen, GREY3, [[p+54, d+10],[p+56, d+12], [p+56, d], [p+54, d]])
        pygame.draw.rect(screen,GREY3,[p+54,d,3,14])
        pygame.draw.polygon(screen, GREY4, [[p+50, d-6], [p+52, d-8],[p+52, d],[p+50, d]])
        pygame.draw.polygon(screen, GREY5, [[p+52, d-8], [p+54, d-10],[p+54, d],[p+52, d]])
        pygame.draw.polygon(screen, GREY6, [[p+54, d-10], [p+56, d-12],[p+56, d],[p+54, d]])
        pygame.draw.rect(screen,GREY6,[p+54,d-13,3,13])
"This the blue right facing shuttle(rocketship)"
def blueSpaceShuttle (x,y):
        pygame.draw.polygon (screen,BLUE3, [[x,y+8],[x,y],[x+15,y]])
        pygame.draw.polygon (screen,BLUE2, [[x,y-9],[x,y-1],[x+15,y]])
        pygame.draw.polygon(screen, BLUE4, [[x-28,y-23],[x-39,y-21], [x-35,y-9], [x-5,y-9]])
        pygame.draw.polygon(screen, BLUE4, [[x-39, y+21],[x-28, y+23], [x-5, y+9], [x-35, y+9]])
        pygame.draw.rect(screen, BLUE2, [x-40, y-9, 40, 9])
        pygame.draw.rect(screen, BLUE3, [x-40, y, 40, 9])
        pygame.draw.rect(screen, BLUE4, [x-7,y-9,4,18])
        pygame.draw.rect(screen, BLUE4, [x-14,y-9,4,18])
        pygame.draw.polygon(screen, GREY1, [[x-41, y+6],[x-43, y+8], [x-43, y], [x-41, y]])
        pygame.draw.polygon(screen, GREY2, [[x-43, y+8],[x-45, y+10], [x-45, y], [x-43, y]])
        pygame.draw.polygon(screen, GREY3, [[x-45, y+10],[x-47, y+12], [x-47, y], [x-45, y]])
        pygame.draw.rect(screen,GREY3,[x-47,y,3,14])
        pygame.draw.polygon(screen, GREY4, [[x-41, y-6], [x-43, y-8],[x-43, y],[x-41, y]])
        pygame.draw.polygon(screen, GREY5, [[x-43, y-8], [x-45, y-10],[x-45, y],[x-43, y]])
        pygame.draw.polygon(screen, GREY6, [[x-45, y-10], [x-47, y-12],[x-47, y],[x-45, y]])
        pygame.draw.rect(screen,GREY6,[x-47,y-13,3,13])
# Load the many images we need
# All of these images are infact screenshots of pygame drawings
# This was done to save time and not force ourselves to recreate drawings facing
# different ways.
launchRocket = pygame.image.load("images/Launch.bmp").convert()
launchRocket = pygame.transform.rotate(launchRocket,90)
launchRocket.set_colorkey(PUREWHITE)
leftBlueSpaceShuttleFire = pygame.image.load("images/leftBlueSpaceShuttleFire.bmp").convert()
leftBlueSpaceShuttleFire.set_colorkey(PUREWHITE)
landingShuttle = pygame.image.load("images/Shuttle.bmp").convert()
landingShuttle = pygame.transform.rotate(landingShuttle,90)
landingShuttle.set_colorkey(PUREWHITE)
landingBlueShuttle = pygame.image.load("images/blueShuttle.bmp").convert()
landingBlueShuttle = pygame.transform.rotate(landingBlueShuttle,90)
landingBlueShuttle.set_colorkey(PUREWHITE)
"=============================================================================="
"=====================SCENE 1==================="
#VARIABLES
f = 0
t = 0
#The The vairables f and t are used for the transition scene(Black rectangles)
u=0
#The variable u will decrease the y coordinate of the rocket and the elevator to make it look
#like its rising
n=0
#The variable n increase the y coordinate of the elevator to make it look like its
#going down
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(PUREWHITE)
        #The entire screen is filled with PUREWHITE
        font = pygame.font.SysFont('Century Gothic', 20, False,False)
        #We set the font style/size here
        if f==0:
                elevate.play()
        #The first sound effect plays here and is timed just as the scene starts
        if 155-u>0:
        #This if statement allows the following to loop until the black transition
        #rectangles leave the screen
                pygame.draw.rect (screen, BLUE, [0,0,702 , 500])
                pygame.draw.rect (screen, GREEN, [0,388,702, 200])
                screen.blit(launchRocket, [337,235+155-u])
                pygame.draw.rect (screen, GREY7, [337,384+155-u,35, 4])
                pygame.draw.rect (screen, GREY7, [352,384+155-u,5, 10])
                pygame.draw.rect (screen, GREY6, [377,343,50, 7])
                pygame.draw.rect (screen, GREY6, [372,283,56, 7])
                pygame.draw.rect (screen, GREY6, [367,243,60, 7])
                pygame.draw.rect (screen, GREEN, [0,400,702, 200])
                pygame.draw.ellipse(screen, GREEN2, [325, 390, 150, 15])
                pygame.draw.rect (screen, GREY7, [417,215, 50, 170])
                pygame.draw.rect (screen, GREY7, [335,390,132, 7])
                pygame.draw.rect (screen, GREY7, [380,383,87, 7])
                pygame.draw.ellipse(screen, GREEN2, [195, 389, 130, 15])
                pygame.draw.rect (screen, GREY7, [215,265, 90, 130])
                pygame.draw.rect (screen, GREY8, [260,265,45,130])
                pygame.draw.rect (screen, GREY8, [260,265,45,130])
                pygame.draw.rect (screen, GREY8, [442,215,25,180])
                pygame.draw.rect (screen, WHITE, [436,210,10, 5])
                #These pygame drawings create the green and blue scenery, shading
                #along with the launch pad and also the the actual launch
                #rocket is printed
                u+=1
                #The u+=1 loops allowing the rectangles to move horizontally
        else:
                pygame.draw.rect (screen, BLUE, [0,0,702 , 500])
                pygame.draw.rect (screen, GREEN, [0,388,702, 200])
                screen.blit(launchRocket, [337,235])
                pygame.draw.rect (screen, GREY7, [337,384+n,35, 4])
                pygame.draw.rect (screen, GREY7, [352,384+n,5, 10])
                pygame.draw.rect (screen, GREY6, [377,343,50, 7])
                pygame.draw.rect (screen, GREY6, [372,283,56, 7])
                pygame.draw.rect (screen, GREY6, [367,243,60, 7])
                pygame.draw.rect (screen, GREEN, [0,400,702, 200])
                pygame.draw.ellipse(screen, GREEN2, [325, 390, 150, 15])
                pygame.draw.rect (screen, GREY7, [417,215, 50, 170])
                pygame.draw.rect (screen, GREY7, [335,390,132, 7])
                pygame.draw.rect (screen, GREY7, [380,383,87, 7])
                pygame.draw.ellipse(screen, GREEN2, [195, 389, 130, 15])
                pygame.draw.rect (screen, GREY7, [215,265, 90, 130])
                pygame.draw.rect (screen, GREY8, [260,265,45,130])
                pygame.draw.rect (screen, GREY8, [442,215,25,180])
                pygame.draw.rect (screen, WHITE, [436,210,10, 5])
                #The same scene as before is recreated here
                n+=0.5
                #This n value is the elevators y value decreasing and making
                #it seems it rises
        pygame.draw.rect (screen, PUREBLACK, [0+f,0,350,501])
        pygame.draw.rect (screen, PUREBLACK, [350+t,0,350,501])
        #These two rectangles are our transition shades
        f -= 1
        t += 1
        #The f and t variables as stated before move the transition
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        #Limit frame rate to 60 fps
        if 350+t==752:
                done = True
        #A timed if statement to allow the scene to end exactly when the black
        #transition rectangles leave the screen
"==========================SCENE 2======================="
done = False
#VARIABLES
e=0
q=0
h=0
#The variables e,q,h are three different variables that at 3 different speeds decrease
#the horizontal size and increase the x coordinate to make it seem that the 3 arms
#are detaching from the rocket and fold into the building.
count = 22
#The count variable is how the count down works but it starts at a much higher
#number of 22 for timings sake (explained below)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #Fill the screen with the color Black
        font = pygame.font.SysFont('Century Gothic', 20, False,False)
        #Set the fontstyle and size here
        pygame.draw.rect (screen, BLUE, [0,0,702, 500])
        pygame.draw.rect (screen, GREEN, [0,388,702, 200])
        pygame.draw.ellipse(screen, GREEN2, [325, 390, 150, 15])
        screen.blit(launchRocket, [337,235])
        pygame.draw.rect (screen, GREY6, [377+e,343,50-e, 7])
        #The variable e increases the x coordinate and decreases the x value
        #making it seems it slides into the rest of the launch pad
        pygame.draw.rect (screen, GREY6, [372+q,283,56-q, 7])
        #The variable q increases the x coordinate and decreases the x value
        #making it seems it slides into the rest of the launch pad
        pygame.draw.rect (screen, GREY6, [367+h,243,60-h, 7])
        #The variable h increases the x coordinate and decreases the x value
        #making it seems it slides into the rest of the launch pad
        pygame.draw.rect (screen, GREY7, [417,215, 50, 170])
        pygame.draw.rect (screen, GREY7, [335,390,132, 7])
        pygame.draw.rect (screen, GREY7, [380,383,87, 7])
        pygame.draw.ellipse(screen, GREEN2, [195, 389, 130, 15])
        pygame.draw.rect (screen, GREY7, [215,265, 90, 130])
        pygame.draw.rect (screen, GREY7, [215,265, 90, 130])
        pygame.draw.rect (screen, GREY8, [260,265,45,130])
        pygame.draw.rect (screen, GREY8, [442,215,25,180])
        pygame.draw.rect (screen, WHITE, [436,210,10, 5])
        #Repition of the same scene recreated earlier
        e+= 6
        q+= 5
        h+= 8
        #The variables go at different speeds to make it more realistic and cool
        if count<5:
                done=True
        #This is an if statement that is timed and once reached the scene ends
        elif  count == 22:
                click.play()
                detach.play()
                count = count-1
        #A double sound effect has been timed and fitted here
        elif count == 21:
                count = count-1
        #Nothing is fitted in this interval, it is here for a break in timing
        elif  count == 20 or count == 19 or count ==18 or count ==17 or count == 16 or count == 15 or count == 14 or count==13:
                text1 = font.render("T MINUS 15 SECONDS GUIDANCE IS INTERNAL" ,True,PUREWHITE)
                count = count-1
                screen.blit(text1, [135, 420])
        #We began our count variable so high because our countdown was not simply
        #numbers. We needed to put words in it as well. Thus we decided to fit the
        #words in timed as we knew each count lasted for 1 second (1fps). This
        #word lasts for 7 counts aka 7 seconds
        elif count ==12 or count ==11 or count ==10:
                text2 = font.render(str(count),True,PUREWHITE)
                screen.blit(text2, [342, 420])
        #This time instead of fitting words, the actual count digits are printed
        #by converting them into strings
        elif count ==9:
                text3 = font.render("9",True,PUREWHITE)
                screen.blit(text3, [349, 420])
        #We needed a sperate piece for the number 9 because its position needs
        #to change as it is 1 digit.
        elif count == 8 or count == 7 or count ==6:
                text4 = font.render( "IGNITION SEQUENCE START" ,True,PUREWHITE)
        #For 3 counts/3 seconds this word is printed
                if count ==8 or count ==6:
                        pygame.draw.rect (screen, RED, [436,210,10, 5])
                        beep.play()
                        #Timed sound effect
                count = count-1
                screen.blit(text4, [225, 420])
        count=count-1
        #Although in every loop, we stated again to assure the count is constantly
        #decreasing
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(1)
        #Limit frame rate to 60 fps
        if count==5:
                done=True
        #A timed if statement to assure that when reach the scene ends
"==========================SCENE 3======================="
done=False
#VARIABLES
count = 6
#The remainging countdown is from 6-0 and thus we start at 6 instead of a higher
#value
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #Fill the screen with Black
        font = pygame.font.SysFont('Century Gothic', 20, False, False)
        #Once again set font style and size
        pygame.draw.rect (screen, BLUE, [0,0,702, 500])
        pygame.draw.rect (screen, GREEN, [0,388,702, 200])
        pygame.draw.ellipse(screen, GREEN2, [325, 390, 150, 15])
        screen.blit(launchRocket, [337,235])
        pygame.draw.rect (screen, GREY7, [417,215, 50, 170])
        pygame.draw.rect (screen, GREY7, [335,390,132, 7])
        pygame.draw.rect (screen, GREY7, [380,383,87, 7])
        pygame.draw.ellipse(screen, GREEN2, [195, 389, 130, 15])
        pygame.draw.rect (screen, GREY7, [215,265, 90, 130])
        pygame.draw.rect (screen, GREY8, [260,265,45,130])
        pygame.draw.rect (screen, GREY8, [442,215,25,180])
        pygame.draw.rect (screen, RED, [436,210,10, 5])
        #We recreate the launch scene once again
        if count<-1:
                done=True
        #A timed if statement that when reached the scene ends
        else:
                text = font.render(str(count),True,PUREWHITE)
                #Converts the count values into strings and prints them
                if count%2==0:
                        beep.play()
                        pygame.draw.rect (screen, RED, [436,210,10, 5])
                if count%2==1:
                        beep.play()
                        pygame.draw.rect (screen, WHITE, [436,210,10, 5])
                #A timed sound effect here
        screen.blit(text, [349, 420])
        #The position where the text is outputted
        count=count-1
        #Although in every loop, we stated again to assure the count is constantly
        #decreasing
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(1)
        #Limit frame rate to 1 fps
        if count==-1:
                done=True
        #A timed if statement that when reached the scene ends
"==========================SCENE 4======================="
done=False
#VARIABLES
k=0
#The variable k increases the vertical size and decreases the y coordinate to make it seem like
#the fire is coming out from the back of the rocket.
o=0
#The variable o makes the rocket move up but infact everything else is just going
#up
n = 650
#The variable n is a set timer
p=0
#The p variable does what k does but is needed for the next statements positioning
w=0
#The w variable will allow us to wiggle/shake the entire scene
v=0
#The v variable will also us to wiggle/shake the rocket and fire at a slower
#speed
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLUE)
        #Fill the screen with Blue
        qbeep.play()
        #This beep is quieter and is played constantly throught the scene
        font = pygame.font.SysFont('Century Gothic', 20, False, False)
        #Set the font style and size here
        if 235-k!=234:
        #This if statement is for until the rocket exactly launches
                pygame.draw.rect (screen, BLUE, [0+w,0,702, 500])
                pygame.draw.rect (screen, GREEN, [0+w,388,702, 200])
                pygame.draw.ellipse(screen, GREEN2, [325+w, 390, 150, 15])
                pygame.draw.rect (screen, ORANGE, [345+v,383-k,18, 0+k])
                pygame.draw.rect (screen, ORANGE, [337+v,383-k,6, 0+k])
                pygame.draw.rect (screen, ORANGE, [365+v,383-k,6, 0+k])
                screen.blit(launchRocket, [337+v,235-k])
                pygame.draw.rect (screen, GREY7, [417+w,215, 50, 170])
                pygame.draw.rect (screen, GREY7, [335+w,390,132, 7])
                pygame.draw.rect (screen, GREY7, [380+w,383,87, 7])
                pygame.draw.ellipse(screen, GREEN2, [195+w, 389, 130, 15])
                pygame.draw.rect (screen, GREY7, [215+w,265, 90, 130])
                pygame.draw.rect (screen, GREY7, [215+w,265, 90, 130])
                pygame.draw.rect (screen, GREY8, [260+w,265,45,130])
                pygame.draw.rect (screen, GREY8, [442+w,215,25,180])
                pygame.draw.rect (screen, BRIGHTRED, [436+w,210,10, 5])
                #The launch scene is recreated but with fire from the rocket and
                #a bright red light
                n=n-1
                word = "ALL ENGINES RUNNING"
                text = font.render(word,True,PUREWHITE)
                screen.blit(text, [250+w, 420])
                #Position where text is printed
                k +=1
                p +=1
                #k and p increase making the fire look like its coming out
        elif 235-k==234:
                pygame.draw.rect (screen, BLUE, [0+w,0+o,70, 500])
                pygame.draw.rect (screen, GREEN, [0+w,388+o,702, 200])
                pygame.draw.ellipse(screen, GREEN2, [325+w, 390+o, 150, 15])
                pygame.draw.rect (screen, ORANGE, [345+v,383-p+o,18, 10+p])
                pygame.draw.rect (screen, ORANGE, [337+v,383-p+o,6, 10+p])
                pygame.draw.rect (screen, ORANGE, [365+v,383-p+o,6, 10+p])
                screen.blit(launchRocket, [337+v,235-p+o])
                pygame.draw.rect (screen, GREY7, [417+w,215+o, 50, 170])
                pygame.draw.rect (screen, GREY7, [335+w,390+o,132, 7])
                pygame.draw.rect (screen, GREY7, [380+w,383+o,87, 7])
                pygame.draw.ellipse(screen, GREEN2, [195+w, 389+o, 130, 15])
                pygame.draw.rect (screen, GREY7, [215+w,265+o, 90, 130])
                pygame.draw.rect (screen, GREY7, [215+w,265+o, 90, 130])
                pygame.draw.rect (screen, GREY8, [260+w,265+o,45,130])
                pygame.draw.rect (screen, GREY8, [442+w,215+o,25,180])
                pygame.draw.rect (screen, BRIGHTRED, [436+w,210+o,10, 5])
                #Previous scene is recreated
                word = "ALL ENGINES RUNNING"
                n=n-1
                text = font.render(word,True,PUREWHITE)
                screen.blit(text, [250+w, 420+o])
                #Position of text
                p+=1
                o+=1.5
        if n%2 == 0:
                w=w-2
                v=v-1
        if n%2 == 1:
                w=w+2
                v=v+1
        #At every odd frame it wiggles to the left and every even frame to the
        #right, at 60 fps this works quickly and causes the shake
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        #Limit frame rate to 60 fps
        if n==0:
                done=True
        #A timed statement that when reached the scene ends
"==========================SCENE 5======================="
done=False
#VARIABLES
m=0
#This variable allows the blackish rectangles to come from the tops
#and bottoms of the screen making another transition
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLUE)
        #Fill the screen with Blue
        if n<0:
                done=True
        #A timed if statement that when reached the scene ends
        elif -340+m!=401:
                pygame.draw.rect (screen,BLACK, [0,-1000+m,701,1000])
                pygame.draw.rect (screen,BLACK, [0,501-m,701,1000])
                m+=1
        #The two transition rectangles at work
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        #Limit frame rate to 60 fps
        if -340+m>0:
                done=True
        #An if statement that when the black rectangles fully cover the screen
        #the scene ends
"==========================SCENE 6======================="
done=False
#VARIABLES
timer = 0
#A timer
m=0
#Another timer
x=-170
#The starting x position of the red rocket ship and title cover
y=250
#The starting y position of the red rocket ship
f = -279
#The starting x position of the rocket ship fire
a = 250
#The starting y position of the rocket ship fire
v= -257
#The starting x position of the rocket
b = 233
#The starting xyposition of the rocket
j = -257
#The starting x position of the top booster
g = 233
#The starting y position of the top booster
k =-257
#The starting x position of the bottom booster
u = 260
#The starting y position of the bottom booster
o = -257
#The starting x postion of the rocket fire
d =-200
#The starting x postion of the title cover
#---
p=0
yy=0
xx=0
oo=0
vv = 0
jj = 0
gg = 0
kk = 0
uu = 0
jjj = 0
kkk=0
vvv=0
vvvv=0
xxx=0
xxxx=0
dd =0
ddd=0
dddd=0
c=0
#---All these are position/value changers
starfield = []
#A list where position of stars are put
#Loop 15 times and add a star in a random t,w position
for i in range(15):
        t = random.randrange(700, 1400)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#A random x and y value for 15 stars are generated randomly
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #Fill the screen with Black
        if x+xxxx>1500:
                done=True
        if timer > -1:
                timer +=1
                if timer == 185 or timer ==227:
                        detach.play()
                #A timed sound effect, twice
        if timer ==213:
                thrust.play()
        #A timed sound effect
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                #Stars are printed and once they leave the screen, regenerated
                #randomly somewhere else
        font = pygame.font.SysFont('Century Gothic', 22, False, False)
        #Font style and size
        text = font.render("Z  E  N  I  T  H" ,True,WHITE)
        #Title
        screen.blit(text, [290, 236])
        #Position of text
        if x+xx<285:
                pygame.draw.rect(screen, BLACK, [d+dd, y-9, 1000, 18])
                dd += 2
                ddd+=2
                dddd+=2
        elif 315<x+xx<505:
                pygame.draw.rect(screen, BLACK, [d+ddd, y-9, 1000, 18])
                ddd+=1
                dddd+=1
        else:
                pygame.draw.rect(screen, BLACK, [d+dddd, y-9, 1000, 18])
                dddd+=2
        if j+jj<=105:
                pygame.draw.rect(screen, ORANGE, [o+oo-150, 233, 150, 6])
                pygame.draw.rect(screen, ORANGE, [o+oo-150, 260, 150, 6])
                pygame.draw.rect(screen, ORANGE, [o+oo-150, 241, 150, 17])
                oo+=2
        else:
                if 150-p>0:
                        pygame.draw.rect(screen, ORANGE, [o+oo-150+c, 233, 150-p, 6])
                        pygame.draw.rect(screen, ORANGE, [o+oo-150+c, 260, 150-p, 6])
                        pygame.draw.rect(screen, ORANGE, [o+oo-150+c, 241, 150-p, 17])
                        c +=20
                        p +=20
                        oo+=2
        if j+jj<=145:
                rocketBoosterTop (j+jj,g)
                rocketBoosterBottom (k+kk,u)
                jj+=2
                jjj+=2
                kk+=2
                kkk+=2
        else:
                rocketBoosterTop (j+jjj,g+gg)
                rocketBoosterBottom(k+kkk,u+uu)
                jjj -=2
                gg -= 1
                kkk -= 2
                uu += 1
        if j+jj<=145:
                Rocket (v+vv,b)
                vv += 2
                vvv+=2
                vvvv+=2
        elif j+jjj>95:
                Rocket (v+vvv,b)
                vvv+=1
                vvvv+=1
        else:
                Rocket (v+vvvv,b)
                vvvv -=1
        if x+xx<285:
                spaceShuttle(x+xx,y)
                xx += 2
                xxx+=2
                xxxx+=2
        elif 315<x+xx<505:
                spaceShuttle(x+xxx,y)
                xxx+=1
                xxxx+=1
        else:
                spaceShuttle(x+xxxx,y)
                spaceShuttleFire(f+xxxx,a)
                xxxx+=2
        #All this is timed and seperatly changes the x value and coordinate
        #of drawings to make them dissapear such as the rocket fire and more
        #Likewise stuff appear timed such as the rocketship fire
        #Also the titles is appeared through the title cover
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        #Limit the frame rate to 60 fps
        if x+xxxx>1500:
                done=True
        #An if statement that when the rocket reaches a certain point, the
        #scene ends
"--------------------------------------------------------"
def  BlueSun(j,k):
        pygame.draw.circle(screen,shadeGrey,(j,k),150)
        pygame.draw.circle(screen,darkGrey,(j,k),140)
        pygame.draw.circle(screen,greyBlue,(j,k),120)
        pygame.draw.circle(screen,tintBlue,(j,k),110)
        pygame.draw.circle(screen,PUREWHITE,(j,k),95)
def Eclipse(x,u):
        pygame.draw.circle(screen,tintBlack,(x,u),130)
def WhitePlanet (x,y):
        pygame.draw.circle(screen,blue2,(x,y),350)
        pygame.draw.circle(screen,blue1,(x,y),250)
        pygame.draw.circle(screen,WHITE,(x,y),200)
        pygame.draw.circle(screen,grey1,(x,y),170)
def YellowSun (f,g):
        pygame.draw.circle(screen,darkBrown,(f,g),380)
        pygame.draw.circle(screen,neutralBrown,(f,g),350)
        pygame.draw.circle(screen,shadeBrown,(f,g),335)
        pygame.draw.circle(screen,darkYellow,(f,g),325)
        pygame.draw.circle(screen,YELLOW,(f,g),310)
        pygame.draw.circle(screen,BEIGE,(f,g),300)
def RedSunPlanet(h,i):
        pygame.draw.circle(screen,PUREBLACK,(h,i),83)
        pygame.draw.circle(screen,PUREBLACK,(h+150,i+5),20)
        pygame.draw.circle(screen,PUREBLACK,(h+200,i-20),4)
        pygame.draw.circle(screen,PUREBLACK,(h+180,i-25),3)
def BrownMoon (a,b):
        pygame.draw.circle(screen,darkBrown2,(a,b),17)
        pygame.draw.circle(screen,brownGrey,(a,b),15)
def GreenPlanet (c,e):
        pygame.draw.circle(screen,darkGreen,(c,e),55)
        pygame.draw.circle(screen,shadeGreen,(c,e),53)
def Sun(v,b):
        pygame.draw.circle(screen,shadeYellow,(v,b),125)
        pygame.draw.circle(screen,YELLOW2,(v,b),120)
        pygame.draw.circle(screen,lightYellow,(v,b),112)
        pygame.draw.circle(screen,lightBeige,(v,b),105)
def chocoBrownPlanet(x,y):
        pygame.draw.circle(screen,BLACK3,(x,y),140)
def brownPlanetOne(x,y):
        pygame.draw.circle(screen,BLACK3,(x,y),40)
def brownPlanetTwo(x,y):
        pygame.draw.circle(screen,BLACK3,(x,y),50)
def brownPlanetThree(x,y):
        pygame.draw.circle(screen,BLACK3,(x,y),20)
def brownPlanetFour(x,y):
        pygame.draw.circle(screen,BLACK3,(x,y),60)
def purplePlanet (x,y):
        pygame.draw.circle(screen,shadePurple,(x,y),58)
        pygame.draw.circle(screen,PURPLE,(x,y),55)
def bluePlanet (x,y):
        pygame.draw.circle(screen,BLUE3,(x,y),105)
def redPlanet (x,y):
        pygame.draw.circle(screen,RED3,(x,y),100)
#Most celestial objects/planets are made and defined here (NOT ALL)
"==========================SCENE 6======================="
done=False
#VARIABLES
timer = 0
#A timer
starfield = []
#The stars are back in the scene and so is the list
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Same procedure as before, randomly generated x and y coordinates
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #The screen is filled in black
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                #Like before, once stars go over the scene, they are randomly
                #regenerated
        if timer == 275:
                done= True
        #A timed if statement that when reached the scene ends
        else:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
        pygame.display.flip()
        #Go ahead and update the screen with what we've drawn.
        clock.tick(60)
        #Limit frame rate to 60 fps
        if timer == 275:
                done = True
        #A timed if statement that when reached the scene ends
"==========================SCENE 7======================="
done=False
#VARIABLE
timer = 0
#A timer
l=0
ll=0
lll=0
#Different changers of x coordinates at different rates for different
#celestial objects
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#The stars are generated here
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #The screen is filled in Blackish
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                #Stars printed and randomly regenerated here
        if timer == 285:
                done= True
        #A timed scene ender
        else:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                pygame.draw.circle (screen, WHITE, [580-ll,470], 3)
                pygame.draw.circle (screen, WHITE, [209-lll,320], 3)
                pygame.draw.circle (screen, WHITE, [400-ll,700], 2)
                pygame.draw.circle (screen, WHITE, [600-l,600], 3)
                pygame.draw.circle (screen, WHITE, [333-ll,46], 3)
                pygame.draw.circle (screen, WHITE, [680-ll,87], 2)
                pygame.draw.circle (screen, WHITE, [90-ll,155], 5)
                pygame.draw.circle (screen, WHITE, [876-l,424], 3)
                pygame.draw.circle (screen, WHITE, [665-l,115], 6)
                pygame.draw.circle (screen, WHITE, [345-l,222], 3)
                pygame.draw.circle (screen, WHITE, [213-lll,20], 2)
                pygame.draw.circle (screen, WHITE, [600-lll,248], 3)
                pygame.draw.circle (screen, WHITE, [499-lll,9], 2)
                l+=1
                ll+=2
                lll+=3
                timer +=1
                #The drawn circles are larger random stars that move at different
                #rates
        pygame.display.flip()
        #Update scene
        clock.tick(60)
         #Limit frame rate to 60 fps
        if timer == 285:
                done = True
        #Timed scene ender
"==========================SCENE 7======================="
done=False
timer = 0
#A timer
lex = 0
x = 0
#Both variables to make celestial objects move the the left
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars made here
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(tintBlack)
        #Screen colored Blackish
        if timer == 285:
                done =True
        #Timed scene ender
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
        #Stars printed
        else:
                BlueSun(350-x,200)
                Eclipse (460-lex,320)
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
                lex += 2
                x += 1
        #The celestial object is moved the  left

        pygame.display.flip()
        #Update scene
        clock.tick(60)
        #Limit frames to 60 fps
        if timer == 285:
                done = True
        #Timed scene ender
"==========================SCENE 8======================="
done=False
#VARIABLES
timer = 0
#A timer
starfield = []
for i in range(4):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars generated here
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK3)
        #Screen filled with shade of black
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                #Stars printed
        if timer == 280:
                done= True
        #Timed scene ender
        else:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
        #A stationed space shuttle
        pygame.display.flip()
        #Update scene
        clock.tick(60)
        #Lim. frame rate to 60 fps
        if timer == 280:
                done = True
        #Timed scene ender
"==========================SCENE 9======================="
done=False
#VARIABLES
timer = 0
#A timer
x=0
#Moves celestial object to the left
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars made here
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(fillYellow)
        #Screen filled yellow here
        for i in range(len(starfield)):
                pygame.draw.circle(screen, fillYellow, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                        #Stars printed here
        if timer == 290:
                done= True
        #Timed scene ender
        else:
                YellowSun (400-x,0)
                RedSunPlanet (550-x*2,200)
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
                x+=1
        #Stationed space shuttle, while celestial objects move at different
        #speeds to the left
        pygame.display.flip()
        #Update scene
        clock.tick(60)
        #Lim frame rate to 60 fps
        if timer == 290:
                done = True
        #Timed scene ender
"==========================SCENE 10======================="
done=False
timer = 0
#A timer
x=0
#Moves stuff to the left
starfield = []
for i in range(10):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars made
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(darkBlue)
        #Screen filled DARKblue
        if timer == 280:
                done= True
                #Timed scene ender
        else:
                WhitePlanet (600-x,600)
                for i in range(len(starfield)):
                        pygame.draw.circle(screen, grey1, starfield[i],2)
                        starfield[i][0] += -1
                        if starfield[i][0] < 0:
                                w = random.randrange(0, 501)
                                starfield[i][1] = w
                                t = random.randrange(710, 750)
                                starfield[i][0] = t
                pygame.draw.circle(screen,blue1,(600-x,600),250)
                pygame.draw.circle(screen,WHITE,(600-x,600),200)
                pygame.draw.circle(screen,grey1,(300-x,300),15)
                pygame.draw.circle(screen,grey1,(600-x,600),170)
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
                x+=1
        #Celestial body moves to the left and stars printed
        pygame.display.flip()
        #Update scene
        clock.tick(60)
        #Lim. frame rate to 60 fps
        if timer == 280:
                done = True
        #Timed scene ender
"==========================SCENE 11======================="
done=False
timer = 0
#A timer
x=0
#Moves stuff to the left
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars generated
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #Fill screen black
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                starfield[i][0] += -1
                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w
                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                        #Print stars
        if timer == 285:
                done= True
                #Timed scene ender
        else:
                BrownMoon (655-x*2,350)
                redPlanet (100-x,400)
                bluePlanet (600-x,100)
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                x +=1
                timer +=1
                #Celestial objects moved as shuttle is stationed
        pygame.display.flip()
        #Update SCENE
        clock.tick(60)
        #Lim. Frame rate to 60 fps
        if timer == 285:
                done = True
        #Timed scene ender
"==========================SCENE 12======================="
done=False
timer = 0
#Timer
x=0
o=0
#Moves stuff to the left
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
#Stars made
while not done:
                # --- Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(BLACK)
        #Screen painted Black
        for i in range(len(starfield)):
                pygame.draw.circle(screen, WHITE, starfield[i], 2)
                if 705-x>500:
                        starfield[i][0] += -1
                else:
                        starfield[i][0] += 0

                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w

                        t = random.randrange(710, 750)
                        starfield[i][0] = t
                #Stars printed
        if timer == 1260:
                done= True
                #Timed scene ender
        if 705-x>450:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                pygame.draw.rect(screen, GREEN, [725+13-x,250-9,4,18])
                pygame.draw.rect(screen, GREEN, [725+20-x,250-9,4,18])
                leftBlueSpaceShuttle (725-x,250)
                x +=1
                timer +=1
        else :
                pygame.draw.rect(screen, GREEN, [370-15, 250-9, 7, 9])
                pygame.draw.rect(screen, GREEN, [370-15, 250, 7, 9])
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                pygame.draw.rect(screen, GREEN, [725+13-x,250-9,4,18])
                pygame.draw.rect(screen, GREEN, [725+20-x,250-9,4,18])
                leftBlueSpaceShuttle (725-x,250)
                timer +=1
        if timer ==350 or timer ==470 or timer ==590:
                heal.play()
        if timer ==710:
                healed.play()
        if timer == 902:
                fire.play()
        if 350 <=timer<= 450 or 470<=timer<=570 or 590<=timer<=690:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                pygame.draw.rect(screen, GREEN, [370-15, 250-9, 7, 9])
                pygame.draw.rect(screen, GREEN, [370-15, 250, 7, 9])
                leftBlueSpaceShuttle (725-x,250)
                timer +=1
        if 710 <= timer <= 900 :
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                leftBlueSpaceShuttle (725-x,250)
                timer +=1
                pygame.draw.rect(screen, GREEN, [725+13-x,250-9,4,18])
                pygame.draw.rect(screen, GREEN, [725+20-x,250-9,4,18])
        if timer >=901:
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                leftBlueSpaceShuttle (725-x,250)
                timer +=1
                screen.blit(leftBlueSpaceShuttleFire, [784-x,247])
                pygame.draw.rect(screen, BLACK, [784-x+o,246,46,12])
                o = o+1
        #In this scene the second blue ship arrives and is healed by
        #the red ship with many sound effects
        pygame.display.flip()
        #Update scenes
        clock.tick(60)
        #Lim frame rate to 60  fps
        if timer == 1260:
                done = True
        #Timed scene ender
"==========================SCENE 13======================="
done=False
timer = 0
x=0
starfield = []
for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
while not done:
                # --- Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(BLACK)

        for i in range(len(starfield)):

                pygame.draw.circle(screen, WHITE, starfield[i], 2)


                starfield[i][0] += -1

                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w

                        t = random.randrange(710, 750)
                        starfield[i][0] = t
        if timer == 580:
                done= True
        else:
                blueSpaceShuttle (400,200)
                spaceShuttleFire (291,200)
                spaceShuttle (370,250)
                spaceShuttleFire (261,250)
                timer +=1
        pygame.display.flip()
        clock.tick(60)
        if timer == 580:
                done = True
"==========================SCENE 14======================="
done=False
timer = 0
x=0
starfield = []

for i in range(20):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
while not done:
                # --- Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(brown3)
        pygame.draw.circle(screen,lightBrown,(480-x/2,80),170)

        if timer == 565:
                done= True
        else:
                Sun (480-x/2,80)
                brownPlanetOne (700-x*2,250)
                brownPlanetTwo (170-x*2,100)
                brownPlanetThree (390-x*2,405)
                brownPlanetFour (200-x,90)
                chocoBrownPlanet (520-x,330)
                blueSpaceShuttle (300,320)
                spaceShuttleFire (190,320)
                spaceShuttle (400,250)
                spaceShuttleFire (290,250)
                x+=1
                timer +=1
        for i in range(len(starfield)):

                pygame.draw.circle(screen, lightBeige, starfield[i], 1)


                starfield[i][0] += -4

                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w

                        t = random.randrange(710, 750)
                        starfield[i][0] = t
        pygame.display.flip()
        clock.tick(60)
        if timer == 565   :
                done = True
"==========================SCENE 15======================="
done=False
timer = 0
x=0
y=0
starfield = []

for i in range(15):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(BLACK)

        for i in range(len(starfield)):

                pygame.draw.circle(screen, WHITE, starfield[i], 2)


                starfield[i][0] += -1

                if starfield[i][0] < 0:
                        w = random.randrange(0, 501)
                        starfield[i][1] = w

                        t = random.randrange(710, 750)
                        starfield[i][0] = t


        if timer == 570:
                done= True
        else:

                blueSpaceShuttle (350,275)
                spaceShuttleFire (240,275)
                spaceShuttle (530,270)
                spaceShuttleFire (422,270)
                timer +=1

        pygame.display.flip()
        clock.tick(60)
        if timer == 570 :
                done = True
"==========================SCENE 16======================="
landingFire = pygame.transform.rotate(leftBlueSpaceShuttleFire,-90)
"--------------------------------------------------------"
done = False
timer = 0
while not done:
                # --- Main event loop
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(BLACK)

        if timer == 360:
                done= True
        if 210+x==260:
                fire2.play()
        if 210+x<280:
                pygame.draw.rect (screen, GREEN, [0,350,702, 200])
                pygame.draw.ellipse (screen, GREEN2, [298,394,40,10])
                pygame.draw.ellipse (screen, GREEN2, [403,408,40,10])
                screen.blit(landingShuttle, [300,200+x])
                screen.blit(landingBlueShuttle, [400,210+x])
                screen.blit (landingFire, [300+12,262+x])
                screen.blit (landingFire, [400+19,276+x])
                x+=1
                timer +=1
        elif 210+x<350:
                pygame.draw.rect (screen, GREEN, [0,350,702, 200])
                pygame.draw.ellipse (screen, GREEN2, [298,394,40,10])
                pygame.draw.ellipse (screen, GREEN2, [403,408,40,10])
                screen.blit(landingShuttle, [300,200+x])
                screen.blit(landingBlueShuttle, [400,210+x])
                x+=0.5
                timer +=1
        else :
                pygame.draw.rect (screen, GREEN, [0,350,702, 200])
                pygame.draw.ellipse (screen, GREEN2, [298,394,40,10])
                pygame.draw.ellipse (screen, GREEN2, [403,408,40,10])
                screen.blit(landingShuttle, [300,200+x])
                screen.blit(landingBlueShuttle, [400,210+x])
                timer +=1

        pygame.display.flip()
        clock.tick(60)
        if timer == 360   :
                done = True
"==========================SCENE 17======================="
done=False
timer = 0
x=0
d=0
for i in range(30):
        t = random.randrange(0, 701)
        w = random.randrange(0, 501)
        starfield.append([t, w])
while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(BLACK)

        if timer == 15:
                done= True
        if timer==0:
                door.play()

        if 20-d>0:
                pygame.draw.rect (screen, GREEN, [0,350,702, 200])
                pygame.draw.ellipse (screen, GREEN2, [298,394,40,10])
                pygame.draw.ellipse (screen, GREEN2, [403,408,40,10])
                screen.blit(landingShuttle, [300,340])
                screen.blit(landingBlueShuttle, [400,350])
                pygame.draw.rect (screen, PUREBLACK, [311,375,10, 17])
                pygame.draw.rect (screen, RED, [311,375,5, 17-d])
                pygame.draw.rect (screen, RED2, [316,375,5, 17-d])
                pygame.draw.rect (screen, PUREBLACK, [418,389,10, 17])
                pygame.draw.rect (screen, BLUE2, [418,389,5, 17-d])
                pygame.draw.rect (screen, BLUE3, [423,389,5, 17-d])
                d+=0.25
                timer +=1
        elif 20-d==0:
                pygame.draw.rect (screen, GREEN, [0,350,702, 200])
                pygame.draw.ellipse (screen, GREEN2, [298,394,40,10])
                pygame.draw.ellipse (screen, GREEN2, [403,408,40,10])
                screen.blit(landingShuttle, [300,340])
                screen.blit(landingBlueShuttle, [400,350])
                pygame.draw.rect (screen, PUREBLACK, [311,375,10, 17])
                pygame.draw.rect (screen, PUREBLACK, [418,389,10, 17])

                timer +=1

        pygame.display.flip()
        clock.tick(60)
        if timer == 20   :
                done = True
"==========================SCENE 18======================="
done=False
starfield = []

for i in range(12):
        t = random.randrange(702, 1400)
        w = random.randrange(0, 501)
        starfield.append([t, w])
while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(BLACK)
        font = pygame.font.SysFont('Century Gothic', 22, False, False)
        font2 = pygame.font.SysFont('Century Gothic', 20, False, False)
        finish.play()
        text = font.render("Z  E  N  I  T  H" ,True,WHITE)
        text2 = font2.render("Z E E L  M A N S U R  &  R A F I T  J A M I L" ,True,WHITE)

        screen.blit(text, [290, 226])
        screen.blit(text2, [185,250])
        for i in range(len(starfield)):

                        pygame.draw.circle(screen, WHITE, starfield[i], 2)


                        starfield[i][0] += -1

                        if starfield[i][0] < 0:
                                w = random.randrange(0, 501)
                                starfield[i][1] = w

                                t = random.randrange(710, 750)
                                starfield[i][0] = t
        pygame.display.flip()
        clock.tick(60)
"==========================END ANIMATION======================="
# Close the window and quit.
pygame.quit()
