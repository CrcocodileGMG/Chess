import pygame
from math import ceil


WHITE_COLOR = pygame.Color(255, 255, 255, 255)
GRAY_COLOR = pygame.Color(128, 128, 128, 255)
SIZE = WIDTH, HEIGHT = 400, 400
FPS = 60


class Cell:
    def __init__(self, indent_x, indent_y, side, color):
        self.indent_x, self.indent_y = indent_x, indent_y
        self.side = side
        self.color = color

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

    def cell_coordinate(self, x_pixels, y_pixels):
        return (ceil((x_pixels - self.indent_x) / (self.side / 8)),
                ceil((self.side - (y_pixels - self.indent_y)) / (self.side / 8)))


clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
desk = Desk(0, 0, 400)
desk.update()
pygame.display.flip()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(desk.cell_coordinate(event.pos[0], event.pos[1]))
        if event.type == pygame.QUIT:
            game = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
