import pygame as pg, sys
from pygame.locals import *
import time

# Initialize global variables
XO = "x"
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# TictacToe 3x3 broad
TTT = [[None] * 3, [None] * 3, [None] * 3]

# Initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Loading the images
openning = pg.image.load("opening.png")
x_img = pg.image.load("x.png")
o_img = pg.image.load("o.png")

# Resizing images
x_img = pg.transform.scale(x_img, (70, 70))
o_img = pg.transform.scale(o_img, (70, 70))
openning = pg.transform.scale(openning, (width, height + 100))


# Launch the game
def game_opening():
    screen.blit(openning, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 8)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 8)
    # Drawing horizontal line
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 8)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 8)
    draw_status()


#
def draw_status():
    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Win"
    if draw:
        message = "Game Draw!"
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    # Copy the rendered message onto the board
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()


#
def check_win():
    global TTT, winner, draw
    # Check for winning rows
    for row in range(0, 3):
        if ((TTT[row][0] == TTT[row][1] == TTT[row][2]) and (TTT[row][0] is not None)):
            winner = TTT[row][0]
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6), 5)
    # Check for winning columns
    for col in range(0, 3):
        if ((TTT[0][col] == (TTT[1][col]) == (TTT[2][col])) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            pg.draw.line(screen, (255, 0, 0), ((col + 1) * height / 3 - height / 6, 0),
                         ((col + 1) * height / 3 - height / 6, height), 5)
    # Check for diagonal winner
    if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)):
        winner = TTT[0][0]
        pg.draw.line(screen, (250, 0, 0), (50, 50), (350, 350), 5)
    if ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)):
        winner = TTT[0][2]
        pg.draw.line(screen, (255, 0, 0), (350, 50), (50, 350), 5)
    if (all([all(row) for row in TTT]) and winner is not None):
        draw = True
    draw_status()


#
def draw_xo(row, col):
    global TTT, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30
    if col == 1:
        posy = 30
    if col == 2:
        posy = height / 3 + 30
    if col == 3:
        posy = height / 3 * 2 + 30
    TTT[row - 1][col - 1] = XO
    if (XO == "x"):
        screen.blit(x_img, (posy, posx))
        XO = "o"
    else:
        screen.blit(o_img, (posy, posx))
        XO = "x"
    pg.display.update()


#
def user_click():
    # Get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # Get column of mouse click (1-3)
    if (x < width / 3):
        col = 1
    elif (x < width / 3 * 2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None
    # Get row of mouse click (1-3)
    if (y < height / 3):
        row = 1
    elif (y < height / 3 * 2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    if (row and col and TTT[row - 1][col - 1] is None):
        global XO
        # Draw the x or o on screen
        draw_xo(row, col)
        check_win()


#
def reset_game():
    global TTT, winner, XO, draw
    time.sleep(2)
    XO = 'x'
    draw = False
    game_opening()
    winner = None
    TTT = [[None] * 3, [None] * 3, [None] * 3]
    draw_status()


#
game_opening()
#
while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if (winner or draw):
                time.sleep(3)
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
