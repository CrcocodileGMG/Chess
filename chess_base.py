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


class Knight(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♘"
        self.char_white = "♞"

    @staticmethod
    def check_move(x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                True if the figure can move from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if abs(x2 - x1) == 2 and abs(y2 - y1) == 1 or abs(x2 - x1) == 1 and abs(y2 - y1) == 2:
            return True
        return False

    @staticmethod
    def move_cells(x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Display cells where KNIGHT can move
            Return:
                List with cells where figure can move
        """

        move_cells = []
        for crd1, crd2 in [(x + 2, y + 1),
                           (x + 2, y - 1),
                           (x - 2, y + 1),
                           (x - 2, y - 1),
                           (x + 1, y + 2),
                           (x + 1, y - 2),
                           (x - 1, y + 2),
                           (x - 1, y - 2)]:
            if 0 < crd1 < 9 and 0 < crd2 < 9:
                move_cells.append(coordinates_to_cell(crd1, crd2))
        return move_cells


class King(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♔"
        self.char_white = "♚"

    @staticmethod
    def check_move(x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                True if the figure can move from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if (abs(x2 - x1) == 1 or abs(x2 - x1) == 0) and (abs(y2 - y1) == 1 or abs(y2 - y1) == 0):
            return True
        return False

    @staticmethod
    def move_cells(x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Display cells where KING can move
            Return:
                List with cells where figure can move
        """

        move_cells = []
        for crd1, crd2 in [(x + 1, y + 1),
                           (x + 1, y - 1),
                           (x - 1, y + 1),
                           (x - 1, y - 1),
                           (x, y + 1),
                           (x, y - 1),
                           (x + 1, y),
                           (x - 1, y)]:
            if 0 < crd1 < 9 and 0 < crd2 < 9:
                move_cells.append(coordinates_to_cell(crd1, crd2))
        return move_cells


class Rook(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♖"
        self.char_white = "♜"

    @staticmethod
    def check_move(x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                True if the figure can move from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
            return True
        return False

    @staticmethod
    def move_cells(x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Display cells where ROOK can move
            Return:
                List with cells where figure can move
        """

        move_cells = [coordinates_to_cell(x, 1),
                      coordinates_to_cell(x, 2),
                      coordinates_to_cell(x, 3),
                      coordinates_to_cell(x, 4),
                      coordinates_to_cell(x, 5),
                      coordinates_to_cell(x, 6),
                      coordinates_to_cell(x, 7),
                      coordinates_to_cell(x, 8),
                      coordinates_to_cell(1, y),
                      coordinates_to_cell(2, y),
                      coordinates_to_cell(3, y),
                      coordinates_to_cell(4, y),
                      coordinates_to_cell(5, y),
                      coordinates_to_cell(6, y),
                      coordinates_to_cell(7, y),
                      coordinates_to_cell(8, y)]
        move_cells.remove(coordinates_to_cell(x, y))
        move_cells.remove(coordinates_to_cell(x, y))
        return move_cells


class Bishop(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♗"
        self.char_white = "♝"

    @staticmethod
    def check_move(x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                True if the figure can move from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if abs(x2 - x1) == abs(y2 - y1) and not (x1 == x2 and y1 == y2):
            return True
        return False

    @staticmethod
    def move_cells(x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Display cells where BISHOP can move
            Return:
                List with cells where figure can move
        """

        move_cells = []
        for crd in range(1, 9):    # check where the bishop can move right up
            if x + crd < 9 and y + crd < 9:
                move_cells.append(coordinates_to_cell(x + crd, y + crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move left up
            if x + crd < 9 and y - crd > 0:
                move_cells.append(coordinates_to_cell(x + crd, y - crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move right down
            if x - crd > 0 and y + crd < 9:
                move_cells.append(coordinates_to_cell(x - crd, y + crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move left down
            if x - crd > 0 and y - crd > 0:
                move_cells.append(coordinates_to_cell(x - crd, y - crd))
            else:
                break
        return move_cells


class Queen(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♕"
        self.char_white = "♛"

    @staticmethod
    def check_move(x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                True if the figure can move from coordinate(x1, y1) to coordinate(x2, y2), else False
        """
        if (((x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2)) or
                ((abs(x1 - x2) == abs(y1 - y2)) and not (x1 == x2 and y1 == y2))):
            return True
        return False

    @staticmethod
    def move_cells(x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Display cells where QUEEN can move
            Return:
                List with cells where figure can move
        """

        move_cells = [coordinates_to_cell(x, 1),
                      coordinates_to_cell(x, 2),
                      coordinates_to_cell(x, 3),
                      coordinates_to_cell(x, 4),
                      coordinates_to_cell(x, 5),
                      coordinates_to_cell(x, 6),
                      coordinates_to_cell(x, 7),
                      coordinates_to_cell(x, 8),
                      coordinates_to_cell(1, y),
                      coordinates_to_cell(2, y),
                      coordinates_to_cell(3, y),
                      coordinates_to_cell(4, y),
                      coordinates_to_cell(5, y),
                      coordinates_to_cell(6, y),
                      coordinates_to_cell(7, y),
                      coordinates_to_cell(8, y)]
        move_cells.remove(coordinates_to_cell(x, y))
        move_cells.remove(coordinates_to_cell(x, y))
        for crd in range(1, 9):    # check where the bishop can move right up
            if x + crd < 9 and y + crd < 9:
                move_cells.append(coordinates_to_cell(x + crd, y + crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move left up
            if x + crd < 9 and y - crd > 0:
                move_cells.append(coordinates_to_cell(x + crd, y - crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move right down
            if x - crd > 0 and y + crd < 9:
                move_cells.append(coordinates_to_cell(x - crd, y + crd))
            else:
                break
        for crd in range(1, 9):    # check where the bishop can move left down
            if x - crd > 0 and y - crd > 0:
                move_cells.append(coordinates_to_cell(x - crd, y - crd))
            else:
                break
        return move_cells


class Pawn(Figure):
    def __init__(self, color: bool):
        super().__init__(color)
        self.char_black = "♙"
        self.char_white = "♟"

    def check_move(self, x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                 True if the figure can MOVE from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if self.get_color():
            if x1 == x2 and (y1 == y2 - 1 or (y1 == 2 and y1 == y2 - 2)):
                return True
            return False
        else:
            if x1 == x2 and (y1 == y2 + 1 or (y1 == 7 and y1 == y2 + 2)):
                return True
            return False

    def check_attack(self, x1, y1, x2, y2) -> bool:
        """
            Args:
                x1(int): first coordinate along the letter axis
                y1(int): first coordinate along the numbers axis
                x2(int): second coordinate along the letter axis
                y2(int): second coordinate along the numbers axis
            Returns:
                 True if the figure can ATTACK from coordinate(x1, y1) to coordinate(x2, y2), else False
        """

        if self.get_color():
            if abs(x1 - x2) == 1 and y1 == y2 - 1:
                return True
            return False
        else:
            if abs(x1 - x2) == 1 and y1 == y2 + 1:
                return True
            return False

    def move_cells(self, x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Displays the cells on which the pawn can move (except for attack)
            Return:
                List with cells where figure can MOVE
        """

        if self.get_color() and y != 8:
            if y == 2:
                return [coordinates_to_cell(x, y + 1), coordinates_to_cell(x, y + 2)]
            return [coordinates_to_cell(x, y + 1)]
        elif not self.get_color() and y != 1:
            if y == 7:
                return [coordinates_to_cell(x, y - 1), coordinates_to_cell(x, y - 2)]
            return [coordinates_to_cell(x, y - 1)]
        return []

    def attack_cells(self, x, y) -> list:
        """
            Args:
                x(int): coordinate along the letter axis
                y(int): coordinate along the numbers axis
            Displays cells where a pawn can attack
            Return:
                List with cells where figure can ATTACK
        """

        if self.get_color() and y != 8:
            if x == 1:
                return [coordinates_to_cell(2, y + 1)]
            elif x == 8:
                return [coordinates_to_cell(7, y + 1)]
            return [coordinates_to_cell(x + 1, y + 1), coordinates_to_cell(x - 1, y + 1)]
        elif not self.get_color() and y != 1:
            if x == 1:
                return [coordinates_to_cell(2, y - 1)]
            elif x == 8:
                return [coordinates_to_cell(7, y - 1)]
            return [coordinates_to_cell(x + 1, y - 1), coordinates_to_cell(x - 1, y - 1)]
        return []


class Desk:
    """
        Args:
            desk (list): input format:
            [["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]]
            coordinate (str): input format A1-A2(first_coordinate - second_coordinate)
    """

    def __init__(self):
        self.desk = [[None for _ in range(8)] for _ in range(8)]
        self.__move_color = WHITE

    def __str__(self) -> str:
        """
            Returns:
                desk display (str)
        """

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

    def regular_chess(self):
        self.desk = [[Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
                      King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)],
                     [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
                      Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None, None],
                     [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
                      Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)],
                     [Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
                      King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)]]

    def change_color(self):
        """
            changes the color of a move to another
        """

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
        """
            replaces coordinate(x2, y2) with coordinate(x1, y1) and replaces coordinate(x1, y1) with None
            (makes a move)
        """

        self.desk[y2 - 1][x2 - 1] = self.desk[y1 - 1][x1 - 1]
        self.desk[y1 - 1][x1 - 1] = None

    def check_move(self, x1, y1, x2, y2):
        if x1 == x2 and y1 < y2:
            for y in range(y1 + 1, y2 + 1):
                if self.get_cell(x1, y) is not None:
                    return False
        elif x1 == x2 and y2 < y1:
            for y in range(y1 - 1, y2 - 1, -1):
                if self.get_cell(x1, y) is not None:
                    return False
        elif y1 == y2 and x1 < x2:
            for x in range(x1 + 1, x2 + 1):
                if self.get_cell(x, y1) is not None:
                    return False
        elif y1 == y2 and x2 < x1:
            for x in range(x1 - 1, x2 - 1, -1):
                if self.get_cell(x, y1) is not None:
                    return False
        elif abs(x2 - x1) == abs(y2 - y1):
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
        if x1 == x2 and y1 < y2:
            for y in range(y1 + 1, y2):
                if self.get_cell(x1, y) is not None:
                    return False
        elif x1 == x2 and y2 < y1:
            for y in range(y1 - 1, y2, -1):
                if self.get_cell(x1, y) is not None:
                    return False
        elif y1 == y2 and x1 < x2:
            for x in range(x1 + 1, x2):
                if self.get_cell(x, y1) is not None:
                    return False
        elif y1 == y2 and x2 < x1:
            for x in range(x1 - 1, x2, -1):
                if self.get_cell(x, y1) is not None:
                    return False
        elif abs(x2 - x1) == abs(y2 - y1):
            if x1 < x2 and y1 < y2:
                for i in range(1, x2 - x1):
                    if self.get_cell(x1 + i, y1 + i) is not None:
                        return False
            elif x1 < x2 and y2 < y1:
                for i in range(1, x2 - x1):
                    if self.get_cell(x1 + i, y1 - i) is not None:
                        return False
            elif x2 < x1 and y2 < y1:
                for i in range(1, abs(x2 - x1)):
                    if self.get_cell(x1 - i, y1 - i) is not None:
                        return False
            elif x2 < x1 and y1 < y2:
                for i in range(1, abs(x2 - x1)):
                    if self.get_cell(x1 - i, y1 + i) is not None:
                        return False
        if self.get_cell(x2, y2) is not None:
            if self.get_cell(x2, y2).get_color() != self.get_color():
                return True
        return False
