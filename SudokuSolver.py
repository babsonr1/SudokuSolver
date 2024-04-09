import pygame
import pygame.font

pygame.font.init()
size = 500
Window = pygame.display.set_mode((size, size))
surface = pygame.Surface((size, size), pygame.SRCALPHA)
surfacecomplete = pygame.Surface((size, size), pygame.SRCALPHA)
pygame.display.set_caption("Sudoku")

x = 0
z = 0
diff = size/9
value = 0
nums = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

defaultgrid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
#option to reset to default (if default is different than all zeros)
defaultgridcopy = defaultgrid.copy()

midnotes = [[[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]]]

edgenotes = [[[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]],
            [[],[],[],[],[],[],[],[],[]]]

#determining the font
font = pygame.font.SysFont("microsoftsansserif", 35)
font1 = pygame.font.SysFont("microsoftsansserif", 15)

#uses x and z to find top left of the box mouse is in
def cord(pos):
    global x
    x = pos[0]//diff
    global z
    z = pos[1]//diff

def drawlines():
    for l in range(10):
        if l % 3 == 0 :
            thick = 3
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (size, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, size), thick)

def addnums():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j] != 0:
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * diff + 20, j * diff + 10))

def notemid():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j] != 0:
                midnotes[i][j] = []
            if midnotes[i][j]:
                text1 = font1.render(''.join(str(x) for x in midnotes[i][j]), 1, (45, 46, 48))
                Window.blit(text1, (i * diff + 20, j * diff + 20))

def noteedge():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j] != 0:
                edgenotes[i][j] = []
            if edgenotes[i][j]:
                text1 = font1.render(''.join(str(x) for x in edgenotes[i][j]), 1, (45, 46, 48))
                Window.blit(text1, (i * diff + 5, j * diff + 5))

def highlightbox():
    for i in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x*diff+1, (z+i)*diff-1), (x*diff+diff+1, (z+i)*diff-1), 5)
        pygame.draw.line(Window, (0, 0, 0), ((x+i)*diff+1, (z)*diff-1), ((x+i)*diff+1, (z*diff+diff-1)), 5)
        pygame.draw.rect(surface, (109, 147, 201, 75), [x*diff, z*diff, diff, diff])

def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 20, z * diff + 20))


def validboard():
    for row in range(1):
        if sorted(defaultgrid[row]) != list(range(1,10)):
            return False

    check = [] 
    for col in range(2):
        for row in range(9):
            check += [defaultgrid[row][col]]
        if sorted(check) != list(range(1,10)):
            return False
        check = []

    box = []
    for row in range(0, 3, 3):
        for col in range (0, 3, 3):
            box = defaultgrid[row][col:col+3] + defaultgrid[row+1][col:col+3] + defaultgrid[row+2][col:col+3]
            for i in range(1,10):
                if i not in box:
                    return False
        box = []
    return True

def endmessage():
    fin = 0
    for i in range(9):
        if 0 not in defaultgrid[i]:
            fin += 1
    if fin == 9 and validboard():
        text1 = font.render("Great job!", 1, (0, 0, 0))
    else:
        text1 = font.render("Try again!", 1, (0, 0, 0))
    textbox = text1.get_rect(center=(size/2, size/2))
    pygame.draw.rect(surfacecomplete, (255, 255, 255, 225), [0, 0, size, size])
    Window.blit(surfacecomplete, (0, 0))
    Window.blit(text1,textbox)

def placenotemid(a,b,value1):
    if value1 not in midnotes[a][b]:
        midnotes[a][b].append(value1)
        midnotes[a][b].sort()
    else:
        midnotes[a][b].remove(value1)
        midnotes[a][b].sort()

def placenoteedge(a,b,value1):
    if value1 not in edgenotes[a][b]:
        edgenotes[a][b].append(value1)
        midnotes[a][b].sort()
    else:
        edgenotes[a][b].remove(value1)
        edgenotes[a][b].sort()

flag=True  
flag1 = 0
checkgrid = 0
value1 = 0

while flag:
    Window.fill((255,255,255))
    Window.blit(surface, (0, 0))
    surface.fill((255, 255, 255))
    addnums()
    drawlines()
    notemid()
    noteedge()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                value = 0
                defaultgrid[int(x)][int(z)] = value
                midnotes[int(x)][int(z)] = []
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                z -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                z += 1
                flag1 = 1
            if event.key in nums:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = int(chr(event.key))
                    placenotemid(int(x), int(z), value1)
                elif pygame.key.get_mods() & pygame.KMOD_CTRL:
                    value1 = int(chr(event.key))
                    placenoteedge(int(x), int(z), value1)
                else:
                    value = int(chr(event.key))
            if event.key == pygame.K_r:
                defaultgrid=[[0, 2, 7, 1, 5, 4, 3, 9, 6],
                            [9, 6, 5, 3, 2, 7, 1, 4, 8],
                            [3, 4, 1, 6, 8, 9, 7, 5, 2],
                            [5, 9, 3, 4, 6, 8, 2, 7, 1],
                            [4, 7, 2, 5, 1, 3, 6, 8, 9],
                            [6, 1, 8, 9, 7, 2, 4, 3, 5],
                            [7, 8, 6, 2, 3, 5, 9, 1, 4],
                            [1, 5, 4, 7, 9, 6, 8, 2, 3],
                            [2, 3, 9, 8, 4, 1, 5, 6, 7]]
            if event.key == pygame.K_c:
                if checkgrid == 1:
                    checkgrid = 0
                else:
                    checkgrid = 1
            if event.key == pygame.K_d:
                defaultgrid = defaultgridcopy

    if value != 0:           
        fillvalue(value)
        defaultgrid[int(x)][int(z)] = value
        value = 0    
 
    if flag1 == 1:
        highlightbox()
    
    if checkgrid == 1:
        endmessage()
    
    
        
        
        
    pygame.display.update() 

pygame.font.quit()      
pygame.quit()
