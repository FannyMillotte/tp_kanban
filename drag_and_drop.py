import pygame
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def drawGrid(screen: pygame.Surface):
    font : pygame.font.Font = pygame.font.SysFont("Arial", 24)
    txt_1 : pygame.Surface = font.render("TO DO", True, (0, 0, 0))
    txt_2 : pygame.Surface = font.render("In progress", True, (0, 0, 0))
    txt_3 : pygame.Surface = font.render("DONE", True, (0, 0, 0))
    txtsurf = [txt_1, txt_2, txt_3]
    i = 0
    w, h = pygame.display.get_surface().get_size()
    x_blockSize = int(w / 3)
    for x in range(0, w, x_blockSize):
        rect = pygame.Rect(x, 0 + 40 , x_blockSize, h)
        pygame.draw.rect(screen, WHITE, rect, 1)
        if (i < 3):
            screen.blit(txtsurf[i],(x +40, 0+10))
            i+=1
        # for y in range(0, h, blockSize):
        #     rect = pygame.Rect(x, y, x_blockSize, blockSize)
        #     pygame.draw.rect(screen, WHITE, rect, 1)

pygame.init()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen : pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Drag And Drop')


active_box = None
items : list[pygame.Rect] = []
for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)

    w = random.randint(35, 65)
    h = random.randint(35, 65)

    # box = pygame.Rect(x, y, w, h)
    box = pygame.Rect(x, y, 50, 60)

    items.append(box)

# fonts = pygame.font.get_fonts()
# for f in fonts:
#    print(f)

font : pygame.font.Font = pygame.font.SysFont("Arial", 36)
txtsurf : pygame.Surface = font.render("Hello, World", True, (0, 0, 0))

run = True
while run :
    screen.fill((255, 248, 231))
    # screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
    drawGrid(screen=screen)

    for box in items:
        pygame.draw.rect(screen, (160,154,209), box, 2)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, box in enumerate(items):
                    if box.collidepoint(event.pos):
                        active_box = num
                    pass
                pass
            pass
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None


        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                items[active_box].move_ip(event.rel)
            pass

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    pass