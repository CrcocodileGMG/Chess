from checkers_base import CheckersFigure, Checker, CheckersKing, CheckersDesk
from constants import *
import pygame
from math import ceil


WHITE_COLOR = pygame.Color(255, 255, 255, 255)
GRAY_COLOR = pygame.Color(128, 128, 128, 255)
SIZE = WIDTH, HEIGHT = 544, 544
FPS = 60
WHITE_KING, WHITE_CHECKER, BLACK_KING, BLACK_CHECKER = (pygame.image.load("WHITE_KING.png"),
                                                        pygame.image.load("WHITE_CHECKER.png"),
                                                        pygame.image.load("BLACK_KING.png"),
                                                        pygame.image.load("BLACK_CHECKER.png"))
FIGURES = {str(Checker(WHITE)): WHITE_CHECKER,
           str(Checker(BLACK)): BLACK_CHECKER,
           str(CheckersKing(WHITE)): WHITE_KING,
           str(CheckersKing(BLACK)): BLACK_KING}


class Cell:
    def __init__(self, indent_x, indent_y, side, color):
        self.indent_x, self.indent_y = indent_x, indent_y
        self.side = side
        self.color = color

    def get_inf(self):
        return self.indent_x, self.indent_y

    def update(self, figure=None):
        pygame.draw.rect(screen, self.color, (self.indent_x, self.indent_y, self.side, self.side))
        if figure is not None:
            screen.blit(figure, self.get_inf())


class Desk:
    def __init__(self, indent_x, indent_y, side):
        self.indent_x, self.indent_y = indent_x, indent_y
        self.side = side
        self.desk = []
        for y in range(7, -1, -1):
            line = []
            for x in range(8):
                line.append(Cell(self.indent_x + (self.get_cell_side()) * x,
                                 (self.indent_y + (self.get_cell_side()) * y), self.get_cell_side(),
                                 (WHITE_COLOR if (x + y) % 2 == 0 else GRAY_COLOR)))
            self.desk.append(line)

    def get_cell_side(self):
        return self.side / 8

    def get_cell(self, x, y):
        return self.desk[y - 1][x - 1]

    def cells_update(self):
        for y in range(1, 9):
            for x in range(1, 9):
                figure = checkers_desk.get_cell(x, y)
                if figure is None:
                    self.get_cell(x, y).update()
                else:
                    self.get_cell(x, y).update(FIGURES.get(str(figure)))

    def cell_coordinate(self, x_pixels, y_pixels):
        return (ceil((x_pixels - self.indent_x) / (self.side / 8)),
                ceil((self.side - (y_pixels - self.indent_y)) / (self.side / 8)))


clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
desk = Desk(0, 0, 544)
checkers_desk = CheckersDesk()
checkers_desk.add(3, 7, Checker(WHITE))
checkers_desk.add(2, 2, Checker(BLACK))
checkers_desk.add(8, 1, Checker(WHITE))
checkers_desk.add(7, 2, Checker(BLACK))
checkers_desk.add(4, 8, Checker(BLACK))
selected_cell = list()

game = True
while game:
    desk.cells_update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                axis = Ox, Oy = desk.cell_coordinate(event.pos[0], event.pos[1])
                if len(selected_cell) != 0:
                    if (checkers_desk.check_move(selected_cell[0], selected_cell[1], Ox, Oy) and
                            checkers_desk.get_cell(selected_cell[0], selected_cell[1]).check_move(selected_cell[0],
                                                                                                  selected_cell[1], Ox,
                                                                                                  Oy)):
                        checkers_desk.move(selected_cell[0], selected_cell[1], Ox, Oy)
                    elif (checkers_desk.check_attack(selected_cell[0], selected_cell[1], Ox, Oy) and
                          checkers_desk.get_cell(selected_cell[0], selected_cell[1]).check_attack(selected_cell[0],
                                                                                                  selected_cell[1], Ox,
                                                                                                  Oy)):
                        checkers_desk.move(selected_cell[0], selected_cell[1], Ox, Oy)
                        checkers_desk.clear_line(selected_cell[0], selected_cell[1], Ox, Oy)
                    selected_cell = list()
                elif checkers_desk.get_cell(Ox, Oy) is not None:
                    selected_cell = [Ox, Oy]
        if event.type == pygame.QUIT:
            game = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
