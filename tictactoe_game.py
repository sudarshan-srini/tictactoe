import pygame, sys
import numpy as np

pygame.init()
sh = 600
sw = 600
row_Num = 3
col_Num = 3
screen = pygame.display.set_mode((sh,sw))
pygame.display.set_caption('TIC TAC TOE')

BG_lineClr = (0, 118, 118)
BG_clr = (20, 170, 156)
screen.fill(BG_clr)

gameMap = np.zeros((row_Num, col_Num))
#print(gameMap)

def draw_line():
    pygame.draw.line(screen, BG_lineClr, (1 / 3 * sw, 0), (1 / 3 * sw, sh), 15)
    pygame.draw.line(screen, BG_lineClr, (2 / 3 * sw, 0), (2 / 3 * sw, sh), 15)
    pygame.draw.line(screen, BG_lineClr, (0, 1 / 3 * sh), (sw, 1 / 3 * sh), 15)
    pygame.draw.line(screen, BG_lineClr, (0, 2 / 3 * sh), (sw, 2 / 3 * sh), 15)

def mark_square(row, col, player):
    gameMap[row][col] = player

def available_square(row, col):
    if gameMap[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for i in range(row_Num):
        for j in range(col_Num):
            if gameMap[i][j] == 0:
                return False
            else:
                return True

mark_square(1,2,1)
print(available_square(1,1))
print(is_board_full())

draw_line()

#mainloop -> same code for every pygame app
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()