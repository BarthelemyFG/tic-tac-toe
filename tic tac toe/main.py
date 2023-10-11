import pygame
import pygame.time
import random

pygame.init()

sizeScreen = (630, 800)
screen = pygame.display.set_mode(sizeScreen)

template = pygame.image.load('Assets/_template tic tac toe.png').convert_alpha()
cross = pygame.transform.scale(pygame.image.load('Assets/cross.png'), (200, 200)).convert_alpha()
circle = pygame.transform.scale(pygame.image.load('Assets/circle.png'), (200, 200)).convert_alpha()
XTurn = pygame.transform.scale(pygame.image.load("Assets/X's turn !.png"), (630, 140)).convert_alpha()
OTurn = pygame.transform.scale(pygame.image.load("Assets/O's turn !.png"), (630, 140)).convert_alpha()
XWin = pygame.transform.scale(pygame.image.load("Assets/X WIN !.png"), (630, 140)).convert_alpha()
OWin = pygame.transform.scale(pygame.image.load("Assets/O WIN !.png"), (630, 140)).convert_alpha()
Draw = pygame.transform.scale(pygame.image.load("Assets/DRAW !.png"), (630, 140)).convert_alpha()
resetText = pygame.transform.scale(pygame.image.load("Assets/reset text.png"), (630, 140)).convert_alpha()

pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(cross)

colorBlack = (0, 0, 0)

Rect1 = pygame.draw.rect(screen, colorBlack, (0, 0, 200, 200))
Rect2 = pygame.draw.rect(screen, colorBlack, (212, 0, 200, 200))
Rect3 = pygame.draw.rect(screen, colorBlack, (425, 0, 200, 200))
Rect4 = pygame.draw.rect(screen, colorBlack, (0, 220, 200, 200))
Rect5 = pygame.draw.rect(screen, colorBlack, (212, 220, 200, 200))
Rect6 = pygame.draw.rect(screen, colorBlack, (425, 220, 200, 200))
Rect7 = pygame.draw.rect(screen, colorBlack, (0, 440, 200, 200))
Rect8 = pygame.draw.rect(screen, colorBlack, (212, 440, 200, 200))
Rect9 = pygame.draw.rect(screen, colorBlack, (425, 440, 200, 200))
RectText = pygame.draw.rect(screen, colorBlack, (0, 660, 630, 140))

actualPlayer = random.randint(1, 2)   # 1= X player to play / 2= O player to play

Board = []
for x in range(3):
    ligne = []
    for y in range(3):
        ligne.append(0)
    Board.append(ligne)


def screen_update():
    pygame.display.update()


def check_winner_cross(board):
    for row in board:
        if all(cell == 1 for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == 1 for row in range(3)):
            return True

    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return True
    return False


def check_winner_circle(board):
    for row in board:
        if all(cell == -1 for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == -1 for row in range(3)):
            return True

    if all(board[i][i] == -1 for i in range(3)) or all(board[i][2 - i] == -1 for i in range(3)):
        return True
    return False


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True


def handle_x_turn(mouseCoord):
    global actualPlayer

    if Rect1.collidepoint(mouseCoord) and Board[0][0] == 0:
        screen.blit(cross, Rect1)
        Board[0][0] = 1
        actualPlayer += 1
    if Rect2.collidepoint(mouseCoord) and Board[0][1] == 0:
        screen.blit(cross, Rect2)
        Board[0][1] = 1
        actualPlayer += 1
    if Rect3.collidepoint(mouseCoord) and Board[0][2] == 0:
        screen.blit(cross, Rect3)
        Board[0][2] = 1
        actualPlayer += 1
    if Rect4.collidepoint(mouseCoord) and Board[1][0] == 0:
        screen.blit(cross, Rect4)
        Board[1][0] = 1
        actualPlayer += 1
    if Rect5.collidepoint(mouseCoord) and Board[1][1] == 0:
        screen.blit(cross, Rect5)
        Board[1][1] = 1
        actualPlayer += 1
    if Rect6.collidepoint(mouseCoord) and Board[1][2] == 0:
        screen.blit(cross, Rect6)
        Board[1][2] = 1
        actualPlayer += 1
    if Rect7.collidepoint(mouseCoord) and Board[2][0] == 0:
        screen.blit(cross, Rect7)
        Board[2][0] = 1
        actualPlayer += 1
    if Rect8.collidepoint(mouseCoord) and Board[2][1] == 0:
        screen.blit(cross, Rect8)
        Board[2][1] = 1
        actualPlayer += 1
    if Rect9.collidepoint(mouseCoord) and Board[2][2] == 0:
        screen.blit(cross, Rect9)
        Board[2][2] = 1
        actualPlayer += 1
    pass


def handle_o_turn(mouseCoord):
    global actualPlayer

    if Rect1.collidepoint(mouseCoord) and Board[0][0] == 0:
        screen.blit(circle, Rect1)
        Board[0][0] = -1
        actualPlayer -= 1
    if Rect2.collidepoint(mouseCoord) and Board[0][1] == 0:
        screen.blit(circle, Rect2)
        Board[0][1] = -1
        actualPlayer -= 1
    if Rect3.collidepoint(mouseCoord) and Board[0][2] == 0:
        screen.blit(circle, Rect3)
        Board[0][2] = -1
        actualPlayer -= 1
    if Rect4.collidepoint(mouseCoord) and Board[1][0] == 0:
        screen.blit(circle, Rect4)
        Board[1][0] = -1
        actualPlayer -= 1
    if Rect5.collidepoint(mouseCoord) and Board[1][1] == 0:
        screen.blit(circle, Rect5)
        Board[1][1] = -1
        actualPlayer -= 1
    if Rect6.collidepoint(mouseCoord) and Board[1][2] == 0:
        screen.blit(circle, Rect6)
        Board[1][2] = -1
        actualPlayer -= 1
    if Rect7.collidepoint(mouseCoord) and Board[2][0] == 0:
        screen.blit(circle, Rect7)
        Board[2][0] = -1
        actualPlayer -= 1
    if Rect8.collidepoint(mouseCoord) and Board[2][1] == 0:
        screen.blit(circle, Rect8)
        Board[2][1] = -1
        actualPlayer -= 1
    if Rect9.collidepoint(mouseCoord) and Board[2][2] == 0:
        screen.blit(circle, Rect9)
        Board[2][2] = -1
        actualPlayer -= 1
    pass


def main():
    run = True

    while run:
        screen.blit(template, (0, 0))
        screen_update()
        is_board_full(Board)
        check_winner_cross(Board)
        check_winner_circle(Board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if actualPlayer == 1:
                screen.blit(resetText, RectText)
                screen.blit(XTurn, RectText)
            if actualPlayer == 2:
                screen.blit(resetText, RectText)
                screen.blit(OTurn, RectText)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if actualPlayer == 1:
                    mouseCoord = pygame.mouse.get_pos()
                    handle_x_turn(mouseCoord)
                elif actualPlayer == 2:
                    mouseCoord = pygame.mouse.get_pos()
                    handle_o_turn(mouseCoord)

            if is_board_full(Board):
                screen.blit(resetText, RectText)
                print("Match nul !")
                screen.blit(Draw, RectText)
                run = False

            if check_winner_cross(Board):
                screen.blit(resetText, RectText)
                print("Les X ont gagné !")
                screen.blit(XWin, RectText)
                run = False

            if check_winner_circle(Board):
                screen.blit(resetText, RectText)
                print("Les O ont gagné !")
                screen.blit(OWin, RectText)
                run = False

    screen_update()
    pygame.time.delay(5000)
    pygame.quit()


main()
