import pygame

pygame.font.init()
size = 500
Window = pygame.display.set_mode((size, size))
surface = pygame.Surface((size, size), pygame.SRCALPHA)
pygame.display.set_caption("Sudoku")

x = 0
z = 0
diff = size/9
value = 0

defaultgrid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
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

#determining the font
font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)

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
                Window.blit(text1, (i * diff + 20, j * diff + 20))

def notemid():
    for i in range (9):
        for j in range (9):
            if midnotes[i][j]:
                text1 = font1.render(''.join(str(x) for x in midnotes[i][j]), 1, (45, 46, 48))
                Window.blit(text1, (i * diff + 20, j * diff + 20))

def highlightbox():
    for i in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x*diff+1, (z+i)*diff-1), (x*diff+diff+1, (z+i)*diff-1), 5)
        pygame.draw.line(Window, (0, 0, 0), ((x+i)*diff+1, (z)*diff-1), ((x+i)*diff+1, (z*diff+diff-1)), 5)
        pygame.draw.rect(surface, (109, 147, 201, 75), [x*diff, z*diff, diff, diff])

def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 20, z * diff + 20))

'''def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it] == value:
            return False
        if m[it][l] == value:
            return False
    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if m[k][l]== value:
                return False
    return True '''

def placenotemid(b,c,value1):
    if value1 not in midnotes[b][c]:
        midnotes[b][c].append(value1)
    else:
        midnotes[b][c].remove(value1)


flag=True  
flag1 = 0
rs = 0
error = 0
value1 = 0

while flag:
    Window.fill((255,255,255))
    Window.blit(surface, (0, 0))
    surface.fill((255, 255, 255))
    addnums()
    drawlines()
    notemid()
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
            if event.key == pygame.K_1:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 1
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 1
            if event.key == pygame.K_2:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 2
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 2
            if event.key == pygame.K_3:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 3
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 3
            if event.key == pygame.K_4:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 4
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 4
            if event.key == pygame.K_5:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 5
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 5
            if event.key == pygame.K_6:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 6
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 6
            if event.key == pygame.K_7:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 7
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 7
            if event.key == pygame.K_8:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 8
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 8
            if event.key == pygame.K_9:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    value1 = 9
                    placenotemid(int(x), int(z), value1)
                else:
                    value = 9
            if event.key == pygame.K_r:
                defaultgrid=[
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
            if event.key == pygame.K_d:
                defaultgrid = defaultgridcopy

    if value != 0:           
        fillvalue(value)
        defaultgrid[int(x)][int(z)] = value
        value = 0    
 
    if flag1 == 1:
        highlightbox()    
    pygame.display.update() 
   
pygame.quit()   