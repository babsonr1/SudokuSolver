import pygame

pygame.font.init()
clock = pygame.time.Clock()
size = 500
Window = pygame.display.set_mode((size, size))
surface = pygame.Surface((size, size), pygame.SRCALPHA)
surfacecomplete = pygame.Surface((size, size), pygame.SRCALPHA)
pygame.display.set_caption("Sudoku")

x = 0
y = 0
diff = size/9
value = 0
nums = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

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

highlighter = [[False for i in range(9)] for j in range(9)]
selected = [[False for i in range(9)] for j in range(9)]

#determining the font
font = pygame.font.SysFont("microsoftsansserif", 35)
font1 = pygame.font.SysFont("microsoftsansserif", 15)

#uses x and y to find top left of the box mouse is in
def cord(pos):
    global x
    x = pos[0]//diff
    global y
    y = pos[1]//diff

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

def selcells(x, y):
    if selected[int(x)][int(y)]:
        selected[int(x)][int(y)] = False
    elif not selected[int(x)][int(y)]:
        selected[int(x)][int(y)] = True

def blackout(j, k):
    for i in range(2):
        pygame.draw.rect(surface, (54, 57, 61, 210), [j*diff, k*diff, diff, diff])

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

def highlightbox1(j, k):
    for i in range(2):
        pygame.draw.line(Window, (0, 0, 0), (j*diff+1, (k+i)*diff-1), (j*diff+diff+1, (k+i)*diff-1), 3)
        pygame.draw.line(Window, (0, 0, 0), ((j+i)*diff+1, (k)*diff-1), ((j+i)*diff+1, (k*diff+diff-1)), 3)
        pygame.draw.rect(surface, (109, 147, 201, 40), [j*diff, k*diff, diff, diff])

def highlightbox():
    for i in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x*diff+1, (y+i)*diff-1), (x*diff+diff+1, (y+i)*diff-1), 5)
        pygame.draw.line(Window, (0, 0, 0), ((x+i)*diff+1, (y)*diff-1), ((x+i)*diff+1, (y*diff+diff-1)), 5)
        pygame.draw.rect(surface, (109, 147, 201, 75), [x*diff, y*diff, diff, diff])

def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 20, y * diff + 20))


def validboard():
    for row in range(9):
        if sorted(defaultgrid[row]) != list(range(1,10)):
            return False

    check = [] 
    for col in range(9):
        for row in range(9):
            check += [defaultgrid[row][col]]
        if sorted(check) != list(range(1,10)):
            return False
        check = []

    box = []
    for row in range(0, 9, 3):
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
    else:
        midnotes[a][b].remove(value1)
    midnotes[a][b].sort()

def placenoteedge(a,b,value1):
    if value1 not in edgenotes[a][b]:
        edgenotes[a][b].append(value1)
    else:
        edgenotes[a][b].remove(value1)
    edgenotes[a][b].sort()

flag = True  
flag1 = 0
flag2 = 0
checkgrid = 0
value1 = 0
tempx = 0
tempy = 0

while flag:
    Window.fill((252,249,225))
    Window.blit(surface, (0, 0))
    surface.fill((252, 249, 225))
    addnums()
    drawlines()
    notemid()
    noteedge()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                tempx = pos[0]//diff
                tempy = pos[1]//diff
                if tempx != x or tempy != y:
                    x = tempx
                    y = tempy
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        selcells(int(x), int(y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cord(pos)
            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                selcells(int(x), int(y))
            if (pygame.key.get_mods() & pygame.KMOD_SHIFT) == False:
                selected = [[False for i in range(9)] for j in range(9)]
            flag1 = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if highlighter[int(x)][int(y)]:
                    highlighter[int(x)][int(y)] = False
                elif not highlighter[int(x)][int(y)]:
                    highlighter[int(x)][int(y)] = True
                    flag2 = 1
            if event.key == pygame.K_BACKSPACE:
                defaultgrid[int(x)][int(y)] = 0
                midnotes[int(x)][int(y)] = []
                edgenotes[int(x)][int(y)] = []
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    for j in range(9):
                        for k in range(9):
                            if selected[j][k]:
                                midnotes[j][k] = []
                                edgenotes[j][k] = []
                            else:
                                continue
            if event.key == pygame.K_LEFT:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    selcells(int(x), int(y))
                if (pygame.key.get_mods() & pygame.KMOD_SHIFT) == False:
                    selected = [[False for i in range(9)] for j in range(9)]
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    selcells(int(x), int(y))
                if (pygame.key.get_mods() & pygame.KMOD_SHIFT) == False:
                    selected = [[False for i in range(9)] for j in range(9)]
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    selcells(int(x), int(y))
                if (pygame.key.get_mods() & pygame.KMOD_SHIFT) == False:
                    selected = [[False for i in range(9)] for j in range(9)]
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    selcells(int(x), int(y))
                if (pygame.key.get_mods() & pygame.KMOD_SHIFT) == False:
                    selected = [[False for i in range(9)] for j in range(9)]
                y += 1
                flag1 = 1
            if event.key in nums:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = int(chr(event.key))
                    for j in range(9):
                        for k in range(9):
                            if selected[j][k]:
                                placenotemid(j, k, value1)
                            else:
                                continue
                    placenotemid(int(x), int(y), value1)
                elif pygame.key.get_mods() & pygame.KMOD_CTRL:
                    value1 = int(chr(event.key))
                    for j in range(9):
                        for k in range(9):
                            if selected[j][k]:
                                placenoteedge(j, k, value1)
                            else:
                                continue
                    placenoteedge(int(x), int(y), value1)
                else:
                    value = int(chr(event.key))
            if event.key == pygame.K_r:
                defaultgrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
            if event.key == pygame.K_c:
                if checkgrid == 1:
                    checkgrid = 0
                else:
                    checkgrid = 1

    if value != 0:           
        fillvalue(value)
        defaultgrid[int(x)][int(y)] = value
        selected = [[False for i in range(9)] for j in range(9)]
        value = 0    
    
    if flag2 == 1:
        for j in range(9):
            for k in range(9):
                if highlighter[j][k]:
                    blackout(j,k)
            else:
                continue
    
    if flag1 == 1:
        highlightbox()

    for j in range(9):
        for k in range(9):
            if selected[j][k]:
                highlightbox1(j, k)
            else:
                continue
    
    if checkgrid == 1:
        endmessage()
        
    pygame.display.update() 

pygame.font.quit()      
pygame.quit()
