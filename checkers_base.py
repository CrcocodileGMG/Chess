from functions import cell_to_coordinates, coordinates_to_cell
from constants import *


class Figure:
    """
        Args:
            color (bool): input format: True(white), False(black)
    """

    def __init__(self, color: bool):
        self.__color = color

    def get_color(self):
        return self.__color

    def get_char(self):
        return self.__str__()

    def __str__(self) -> str:
        """
            Returns:
                figure display (str)
        """

        if self.__color:
            return self.char_black
        return self.char_white


class Checker(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.char_white = "⛀"
        self.char_black = "⛂"

    def check_move(self, x1, y1, x2, y2):
        if self.get_color() == WHITE:
            if abs(x2 - x1) == 1 and y2 - y1 == 1:
                return True
        else:
            if abs(x2 - x1) == 1 and y1 - y2 == 1:
                return True
        return False

    def check_attack(self, x1, y1, x2, y2):
        if self.get_color() == WHITE:
            if abs(x2 - x1) == 2 and y2 - y1 == 2:
                return True
        else:
            if abs(x2 - x1) == 2 and y1 - y2 == 2:
                return True
        return False


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.char_white = "⛁"
        self.char_black = "⛃"

    @staticmethod
    def check_move(x1, y1, x2, y2):
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        return False

    @staticmethod
    def check_attack(x1, y1, x2, y2):
        if abs(x1 - x2) == abs(y1 - y2) and abs(x1 - x2) > 1:
            return True
        return False


class Desk:
    def __init__(self):
        self.desk = [[None for _ in range(8)] for _ in range(8)]
        self.__move_color = WHITE

    def __str__(self) -> str:
        output = str()
        for i in range(8):
            output += str(8 - i) + " "
            for j in range(8):
                figure = self.desk[7 - i][j]
                if figure is None:
                    output += "※ "
                    continue
                output += figure.get_char() + " "
            output = output[:-1]
            output += "\n"
        output += "   A   B   C  D   E   F  G   H"
        return output

    def standard_checkers(self):
        self.desk = [[Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE), None],
                     [None, Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE)],
                     [Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE), None, Checker(WHITE), None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK)],
                     [Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK), None],
                     [None, Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK), None, Checker(BLACK)]]

    def change_color(self):
        self.__move_color = not self.__move_color

    def get_color(self) -> bool:
        return self.__move_color

    def add(self, x, y, figure):
        self.desk[y - 1][x - 1] = figure

    def remove(self, x, y):
        self.desk[y - 1][x - 1] = None

    def get_cell(self, x, y):
        return self.desk[y - 1][x - 1]

    def move(self, x1, y1, x2, y2):
        if isinstance(self.get_cell(x1, y1), Checker) and self.get_cell(x1, y1).get_color() and y1 == 7:
            self.desk[y2 - 1][x2 - 1] = King(WHITE)
            self.desk[y1 - 1][x1 - 1] = None
        elif isinstance(self.get_cell(x1, y1), Checker) and not self.get_cell(x1, y1).get_color() and y1 == 2:
            self.desk[y2 - 1][x2 - 1] = King(BLACK)
            self.desk[y1 - 1][x1 - 1] = None
        else:
            self.desk[y2 - 1][x2 - 1] = self.desk[y1 - 1][x1 - 1]
            self.desk[y1 - 1][x1 - 1] = None

    def clear_line(self, x1, y1, x2, y2):
        if x1 < x2 and y1 < y2:
            for i in range(1, x2 - x1):
                if self.get_cell(x1 + i, y1 + i) is not None:
                    self.remove(x1 + i, y1 + i)
                    break
        elif x1 < x2 and y2 < y1:
            for i in range(1, x2 - x1):
                if self.get_cell(x1 + i, y1 - i) is not None:
                    self.remove(x1 + i, y1 - i)
                    break
        elif x2 < x1 and y2 < y1:
            for i in range(1, abs(x2 - x1)):
                if self.get_cell(x1 - i, y1 - i) is not None:
                    self.remove(x1 - i, y1 - i)
                    break
        elif x2 < x1 and y1 < y2:
            for i in range(1, abs(x2 - x1)):
                if self.get_cell(x1 - i, y1 + i) is not None:
                    self.remove(x1 - i, y1 + i)
                    break

    def check_move(self, x1, y1, x2, y2):
        if abs(y2 - y1) == abs(x2 - x1):
            if x1 < x2 and y1 < y2:
                for i in range(1, x2 - x1 + 1):
                    if self.get_cell(x1 + i, y1 + i) is not None:
                        return False
            elif x1 < x2 and y2 < y1:
                for i in range(1, x2 - x1 + 1):
                    if self.get_cell(x1 + i, y1 - i) is not None:
                        return False
            elif x2 < x1 and y2 < y1:
                for i in range(1, abs(x2 - x1) + 1):
                    if self.get_cell(x1 - i, y1 - i) is not None:
                        return False
            elif x2 < x1 and y1 < y2:
                for i in range(1, abs(x2 - x1) + 1):
                    if self.get_cell(x1 - i, y1 + i) is not None:
                        return False
        return True

    def check_attack(self, x1, y1, x2, y2):
        figure_count_line = 0
        if abs(y2 - y1) == abs(x2 - x1):
            if x1 < x2 and y1 < y2:
                for i in range(1, x2 - x1):
                    if self.get_cell(x1 + i, y1 + i) is not None:
                        if self.get_cell(x1, y1).get_color() != self.get_cell(x1 + i, y1 + i).get_color():
                            figure_count_line += 1
                        else:
                            return False
                    if figure_count_line == 2:
                        return False
            elif x1 < x2 and y2 < y1:
                for i in range(1, x2 - x1):
                    if self.get_cell(x1 + i, y1 - i) is not None:
                        if self.get_cell(x1, y1).get_color() != self.get_cell(x1 + i, y1 - i).get_color():
                            figure_count_line += 1
                        else:
                            return False
                    if figure_count_line == 2:
                        return False
            elif x2 < x1 and y2 < y1:
                for i in range(1, abs(x2 - x1)):
                    if self.get_cell(x1 - i, y1 - i) is not None:
                        if self.get_cell(x1, y1).get_color() != self.get_cell(x1 - i, y1 - i).get_color():
                            figure_count_line += 1
                        else:
                            return False
                    if figure_count_line == 2:
                        return False
            elif x2 < x1 and y1 < y2:
                for i in range(1, abs(x2 - x1)):
                    if self.get_cell(x1 - i, y1 + i) is not None:
                        if self.get_cell(x1, y1).get_color() != self.get_cell(x1 - i, y1 + i).get_color():
                            figure_count_line += 1
                        else:
                            return False
                    if figure_count_line == 2:
                        return False
            if figure_count_line == 1 and self.get_cell(x2, y2) is None:
                return True
        return False

    def check_continue(self):
        white_figure = False
        black_figure = False
        for line in self.desk:
            for cell in line:
                if cell is not None:
                    if cell.get_color():
                        white_figure = True
                    elif not cell.get_color():
                        black_figure = True
                    if white_figure and black_figure:
                        return True
        return False

    def check_black_checker_can_move(self, x, y, color):
        if y != 1:
            if x == 1:
                if self.get_cell(x + 1, y - 1) is None:
                    return True
                elif y != 2:
                    if self.get_cell(x + 1, y - 1).get_color() == (not color) and self.get_cell(x + 2, y - 2) is None:
                        return True
            elif x == 2:
                if self.get_cell(x - 1, y - 1) is None or self.get_cell(x + 1, y - 1) is None:
                    return True
                elif y != 2:
                    if self.get_cell(x + 1, y - 1).get_color() == (not color) and self.get_cell(x + 2, y - 2) is None:
                        return True
            elif x == 7:
                if self.get_cell(x - 1, y - 1) is None or self.get_cell(x + 1, y - 1) is None:
                    return True
                elif y != 2:
                    if self.get_cell(x - 1, y - 1).get_color() == (not color) and self.get_cell(x - 2, y - 2) is None:
                        return True
            elif x == 8:
                if self.get_cell(x - 1, y - 1) is None:
                    return True
                elif y != 2:
                    if self.get_cell(x - 1, y - 1).get_color() == (not color) and self.get_cell(x - 2, y - 2) is None:
                        return True
            else:
                if self.get_cell(x - 1, y - 1) is None or self.get_cell(x + 1, y - 1) is None:
                    return True
                elif y != 2:
                    if ((self.get_cell(x + 1, y - 1).get_color() == (not color) and
                         self.get_cell(x + 2, y - 2) is None) or
                            (self.get_cell(x - 1, y - 1).get_color() == (not color) and
                             self.get_cell(x - 2, y - 2) is None)):
                        return True
        return False

    def check_white_checker_can_move(self, x, y, color):
        if y != 8:
            if x == 1:
                if self.get_cell(x + 1, y + 1) is None:
                    return True
                elif y != 7:
                    if self.get_cell(x + 1, y + 1).get_color() == (not color) and self.get_cell(x + 2, y + 2) is None:
                        return True
            elif x == 2:
                if self.get_cell(x - 1, y + 1) is None or self.get_cell(x + 1, y + 1) is None:
                    return True
                elif y != 7:
                    if self.get_cell(x + 1, y + 1).get_color() == (not color) and self.get_cell(x + 2, y + 2) is None:
                        return True
            elif x == 7:
                if self.get_cell(x - 1, y + 1) is None or self.get_cell(x + 1, y + 1) is None:
                    return True
                elif y != 7:
                    if self.get_cell(x - 1, y + 1).get_color() == (not color) and self.get_cell(x - 2, y + 2) is None:
                        return True
            elif x == 8:
                if self.get_cell(x - 1, y + 1) is None:
                    return True
                elif y != 7:
                    if self.get_cell(x - 1, y + 1).get_color() == (not color) and self.get_cell(x - 2, y + 2) is None:
                        return True
            else:
                if self.get_cell(x - 1, y + 1) is None or self.get_cell(x + 1, y + 1) is None:
                    return True
                elif y != 7:
                    if ((self.get_cell(x + 1, y + 1).get_color() == (not color) and
                         self.get_cell(x + 2, y + 2) is None) or
                        (self.get_cell(x - 1, y + 1).get_color() == (not color) and
                         self.get_cell(x - 2, y + 2) is None)):
                        return True
        return False

    def check_can_move(self, x, y):
        if isinstance(self.get_cell(x, y), Checker):
            if self.get_cell(x, y).get_color() == WHITE:
                return self.check_white_checker_can_move(x, y, WHITE)
            elif self.get_cell(x, y).get_color() == BLACK:
                return self.check_black_checker_can_move(x, y, BLACK)
        return (self.check_white_checker_can_move(x, y, self.get_cell(x, y).get_color()) or
                self.check_black_checker_can_move(x, y, self.get_cell(x, y).get_color()))

    def draw(self, color):
        for y in range(1, 9):
            for x in range(1, 9):
                if self.get_cell(x, y) is not None and self.get_cell(x, y).get_color() == color:
                    if self.check_can_move(x, y):
                        return False
        return True

    def check_winner(self):
        for line in self.desk:
            for cell in line:
                if cell is not None:
                    if cell.get_color():
                        return True
                    else:
                        return False

    def is_empty(self):
        if self.desk == [[None for _ in range(8)] for _ in range(8)]:
            return True
        return False
