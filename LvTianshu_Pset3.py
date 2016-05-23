import pygame
from pygame.locals import *
import random
import copy
import pickle
copy=copy.deepcopy

pygame.init()

SCREEN_HEIGHT=600
SCREEN_WIDTH=800
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
myfont=pygame.font.SysFont("arial", 20)

pygame.display.set_caption('Life Game')
screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))
clock=pygame.time.Clock()

died=(245,245,245)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,0)
pink=(255,192,203)
orange=(255,97,0)
purple=(160,32,240)
brown=(128,42,42)

colors=[died,red,blue,green,yellow,pink,orange,purple,brown]



def main():
    global screen,clock, colors,SCREEN_WIDTH,SCREEN_SIZE
    running=True
    pause=False
    fullScreen=False
    c=80
    r=80
    cellLife=[[False for i in range(c)] for i in range(r)]
    myCells=[]
    save=[]
    x=0
    y=0
    length=SCREEN_WIDTH//c
    blank=1
    delay=1
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(Cell(screen,False,(x+j*length,y+i*length,length-1,length-1),(122,122,122)))
        myCells.append(row)
    for i in range (int(c*r/10)):
        cellLife[random.randint(1,r-1)][random.randint(1,c-1)]=True
    while running:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==KEYDOWN:
                if event.key==K_p:
                    pause=not pause
                elif event.key==K_MINUS:
                    delay+=10
                elif event.key==K_EQUALS:
                    delay-=10
                elif event.key==K_r:
                    for i in range(len(cellLife)):
                        for j in range (len(cellLife[i])):
                            oldCells[i][j]=False
                            cellLife[i][j]=False
                elif event.key==K_f:
                    fullScreen=not fullScreen
                    if fullScreen:
                        screen=pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN,32)
                    else:
                        screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
                elif event.key==K_0:
                    for i in range (int(c*r/10)):
                        cellLife[random.randint(1,r-1)][random.randint(1,c-1)]=True
                    oldCells=copy(cellLife)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                (posx,posy)=pygame.mouse.get_pos()
                cellX=posx//length
                cellY=posy//length
                if pause==True:
                    if cellLife[cellY][cellX]==True:
                        cellLife[cellY][cellX]=False
                        myCells[cellY][cellX].setColor(colors[0])
                    else:
                        cellLife[cellY][cellX]=True
                        myCells[cellY][cellX].setColor(colors[2])
            if event.type==KEYDOWN:
                if event.key==K_s:
                    f=open('save.dat','wb')
                    pickle.dump(cellLife,f)
                if event.key==K_l:
                    if pause==True:
                        f=open('save.dat','rb')
                        cellLife=pickle.load(f)
                        pause=False

            #if event.type==KEYDOWN:
                if event.key==K_z:
                    screen.fill((255,255,255))
                    c-=7
                    r-=7
                    length=SCREEN_WIDTH//c
                    cellLife=[[False for i in range(c)] for i in range(r)]
                    myCells=[]
                    x=0
                    y=0
                    for i in range(r):
                        row=[]
                        for j in range(c):
                            row.append(Cell(screen,False,(x+j*length,y+i*length,length-1,length-1),(122,122,122)))
                        myCells.append(row)
                    for i in range (int(c*r/10)):
                        cellLife[random.randint(1,r-1)][random.randint(1,c-1)]=True
                elif event.key==K_x:
                    screen.fill((255,255,255))
                    c+=7
                    r+=7
                    length=SCREEN_WIDTH//c
                    cellLife=[[False for i in range(c)] for i in range(r)]
                    myCells=[]
                    x=0
                    y=0
                    for i in range(r):
                        row=[]
                        for j in range(c):
                            row.append(Cell(screen,False,(x+j*length,y+i*length,length-1,length-1), (122,122,122)))
                        myCells.append(row)
                    for i in range (int(c*r/10)):
                        cellLife[random.randint(1,r-1)][random.randint(1,c-1)]=True
                    
        oldCells=copy(cellLife)
        if pause==False:
            setColorCells(oldCells,cellLife,myCells,colors)
        drawCells(myCells)
        pygame.display.flip()
        clock.tick(100)
        pygame.time.delay(delay)

def setColorCells(oldCells,cellLife,myCells,colors):
    for i in range(len(cellLife)):
        for j in range(len(cellLife[i])):
            count=isAlive(oldCells, cellLife,(j,i))
            if oldCells[i][j]==False:
                myCells[i][j].setColor(colors[0])
            else:
                myCells[i][j].setColor(colors[count])
            
            
def isAlive(oldCells,cellLife,location):
    count=0
    x=location[0]
    y=location[1]
    try:
        if oldCells[y-1][x-1]==True:
            count+=1
    except:
        pass
    try:
        if oldCells[y-1][x]:
            count+=1
    except:
        pass
    try:
        if oldCells[y-1][x+1]:
            count+=1
    except:
        pass
    try:
        if oldCells[y][x-1]:
            count+=1
    except:
        pass
    try:
        if oldCells[y][x+1]:
            count+=1
    except:
        pass
    try:
        if oldCells[y+1][x-1]:
            count+=1
    except:
        pass
    try:
        if oldCells[y+1][x]:
            count+=1
    except:
        pass
    try:
        if oldCells[y+1][x+1]:
            count+=1
    except:
        pass
    if cellLife[y][x]==True:
        if count<2 or count>3:
            cellLife[y][x]=False
    else:
        if count==3:
            cellLife[y][x]=True
    return count

def drawCells(myCells):
    for row in myCells:
        for cell in row:
            cell.drawCell()
        


class Cell:
    def __init__(self,surface,life,rect,color):
        self.life=life
        self.surface=surface
        self.color=color
        self.rect=rect
    def setColor(self,color):
        self.color=color
    def drawCell(self):
        pygame.draw.rect(self.surface,self.color,self.rect)
main()
