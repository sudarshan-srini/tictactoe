'''import turtle

def drawBoard():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200*i)
        drawer.pendown()
        drawer.forward(600)

    drawer.right(90)

    for j in range(2):
        drawer.penup()
        drawer.goto(-100 + 200*j, 300)
        drawer.pendown()
        drawer.forward(600)

        screen.update()

drawer = turtle.Turtle()
drawer.pensize(10)
drawer.ht()

screen = turtle.Screen()
screen.tracer(0)

drawBoard()
turtle.mainloop()
'''

import pygame, sys
import numpy as np

pygame.init()
sh = 600
sw = 600
row_Num = 3
col_Num = 3
screen = pygame.display.set_mode((sh,sw))
pygame.display.set_caption('TIC TAC TOE')

circle_clr = (245,245,245)
cross_clr = (35,35,35)
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

def draw_figures():
    for row in range(row_Num):
        for col in range(col_Num):
            if gameMap[row][col] == 1:
                pygame.draw.circle(screen, circle_clr, (int(col*200 + 100), int(row*200 + 100)), 60, 15)
            elif gameMap[row][col] == 2:
                pygame.draw.line(screen, cross_clr, (col*200 + 200/4, row*200 +200 - 200/4), (col*200 + 200 - 50, row*200 + 50), 25)
                pygame.draw.line(screen, cross_clr, (col*200 + 200/4, row*200 + 50), (col*200 + 150, row*200 + 150), 25)
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

def game_end():
    for i in range(row_Num):
        for j in range(row_Num):
            if gameMap[i][j] == 1:
                gameWinner = 1
            elif gameMap[i][j] == 2:
                gameWinner = 2
            else:
                gameWinner = "Tie"

def check_win(player):
    for col in range(col_Num):
        if gameMap[0][col] == player and gameMap[1][col] == player and gameMap[2][col] == player:
            draw_vert_win_line(col, player)
            return True

    for row in range(row_Num):
        if gameMap[row][0] == player and gameMap[row][1] == player and gameMap[row][2] == player:
            draw_hor_win_line(row, player)
            return True

    if gameMap[2][0] == player and gameMap[1][1] == player and gameMap[0][2] == player:
        draw_asc_diag_win_line(player)
        return True

    if gameMap[0][0] == player and gameMap[1][1] == player and gameMap[2][2] == player:
        draw_desc_diag_win_line(player)
        return True

def draw_vert_win_line(col, player):
    posX = col*200 + 100

    if player == 1:
        color = circle_clr
    elif player == 2:
        color = cross_clr

    pygame.draw.line(screen, color, (posX,15), (posX,sh - 15), 15)

def draw_hor_win_line(row, player):
    posY = row*200 + 100

    if player == 1:
        color = circle_clr
    elif player == 2:
        color = cross_clr

    pygame.draw.line(screen, colour, (15,posY), (sw-15,posY), 15)

def draw_asc_diag_win_line(player):
    if player == 1:
        color = circle_clr
    elif player == 2:
        color = cross_clr

    pygame.draw.line(screen, color, (15, sh - 15), (sw - 15, 15), 15)

def draw_desc_diag_win_line(player):
    if player == 1:
        color = circle_clr
    elif player == 2:
        color = cross_clr

    pygame.draw.line(screen, color, (15,15), (sw-15, sh-15), 15)

def restart():
    pass

"""mark_square(0,0,2)
mark_square(1,1,2)
mark_square(2,2,2)
"""

print(gameMap)
print(game_end())

draw_line()

game_over = False

player = 1

#mainloop -> same code for every pygame app
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  #x
            mouseY = event.pos[1]  #y

            clicked_Col = int(mouseX/200)
            clicked_Row = int(mouseY/200)

            if available_square(clicked_Row, clicked_Col):
                if player == 1:
                    mark_square(clicked_Row,clicked_Col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_Row,clicked_Col,2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()


    pygame.display.update()