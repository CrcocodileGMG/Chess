import pygame
from math import ceil


WHITE_COLOR = pygame.Color(255, 255, 255, 255)
GRAY_COLOR = pygame.Color(128, 128, 128, 255)
RED_COLOR = pygame.Color(255, 0, 0, 255)
SIZE = WIDTH, HEIGHT = 400, 400
FPS = 60


class Figure:
    def __init__(self, x, y, side):
        self.x, self.y = x, y
        self.side = side

    def update(self):
        pygame.draw.rect(screen, RED_COLOR, desk.get_cell_coordinate(self.x, self.y))

    def set_crds(self, x, y):
        self.x = x
        self.y = y


class Cell:
    def __init__(self, indent_x, indent_y, side, color):
        self.indent_x, self.indent_y = indent_x, indent_y
        self.side = side
        self.color = color

    def get_inf(self):
        return self.indent_x, self.indent_y, self.side, self.side

    def update(self):
        pygame.draw.rect(screen, self.color, (self.indent_x, self.indent_y, self.side, self.side))


class Desk:
    def __init__(self, indent_x, indent_y, side):
        self.indent_x, self.indent_y = indent_x, indent_y
        self.side = side
        self.desk = []
        for y in range(7, -1, -1):
            line = []
            for x in range(8):
                line.append(Cell(self.indent_x + (self.side / 8) * x,
                                 (self.indent_y + (self.side / 8) * y), self.side / 8,
                                 (WHITE_COLOR if (x + y) % 2 == 0 else GRAY_COLOR)))
            self.desk.append(line)

    def update(self):
        for line in self.desk:
            for cell in line:
                cell.update()

    def get_cell_coordinate(self, x, y):
        return self.desk[y - 1][x - 1].get_inf()

    def cell_coordinate(self, x_pixels, y_pixels):
        return (ceil((x_pixels - self.indent_x) / (self.side / 8)),
                ceil((self.side - (y_pixels - self.indent_y)) / (self.side / 8)))


clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
desk = Desk(0, 0, 400)
red_square = Figure(1, 1, 50)

game = True
while game:
    desk.update()
    red_square.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = desk.cell_coordinate(event.pos[0], event.pos[1])
                red_square.set_crds(x, y)
        if event.type == pygame.QUIT:
            game = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
