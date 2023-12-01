from chess_base import Knight, King, Rook, Bishop, Queen, Pawn, Desk
from functions import cell_to_coordinates, coordinates_to_cell
from constants import *


chess_desk = Desk()
white_figures_dict = {"knight": Knight(True),
                      "king": King(True),
                      "rook": Rook(True),
                      "bishop": Bishop(True),
                      "queen": Queen(True),
                      "pawn": Pawn(True)}
black_figures_dict = {"knight": Knight(False),
                      "king": King(False),
                      "rook": Rook(False),
                      "bishop": Bishop(False),
                      "queen": Queen(False),
                      "pawn": Pawn(False)}


def chessboard_arrangement():
    print("""if you want to add figure than write 'add-figure-color-cell'
if you want to remove figure than write 'remove-cell'
if you want to set standard chess write 'standard_chess'
if you edited the board than write 'stop'
figures: knight, king, rook, bishop, queen, pawn
colors: white, black""")
    while True:
        act = input().split("-")
        if ((act[0] == "add") and (act[1] in ["knight", "king", "rook", "bishop", "queen", "pawn"]) and
                (act[2] in ["white", "black"]) and (len(act) == 4) and (len(act[3]) == 2)):
            try:
                if act[2] == "white":
                    chess_desk.add(*cell_to_coordinates(act[3]), white_figures_dict.get(act[1]))
                else:
                    chess_desk.add(*cell_to_coordinates(act[3]), black_figures_dict.get(act[1]))
            except ValueError:
                print("Input error")
        elif act[0] == "remove" and len(act) == 2:
            chess_desk.remove(*cell_to_coordinates(act[1]))
        elif act[0] == "standard_chess" and len(act) == 1:
            chess_desk.regular_chess()
        elif act[0] == "stop" and len(act) == 1:
            break
        else:
            print("Input error")


def first_move_color():
    color = input("who move first(white/black): ")
    if color == "white":
        pass
    elif color == "black":
        chess_desk.change_color()
    else:
        print("Input error")
        first_move_color()


def main():
    chessboard_arrangement()
    first_move_color()

    game = True
    while game:
        print(chess_desk)
        if chess_desk.get_color() == WHITE:
            print("White's move")
        else:
            print("Black's move")
        cell_1, cell_2 = input("Write your move: ").split("-")
        x1, y1 = cell_to_coordinates(cell_1)
        x2, y2 = cell_to_coordinates(cell_2)
        figure = chess_desk.desk[y1 - 1][x1 - 1]
        if not figure:
            print("The figure on this square was not found")
        elif figure.get_color() != chess_desk.get_color():
            print("You choose a figure with the wrong color")
        elif figure.check_move(x1, y1, x2, y2) and chess_desk.check_move(x1, y1, x2, y2):
            chess_desk.move(x1, y1, x2, y2)
            chess_desk.change_color()
        # elif figure.check_attack(x1, y1, x2, y2) and chess_desk.check_attack(x1, y1, x2, y2):
        #     chess_desk.move(x1, y1, x2, y2)
        #     chess_desk.change_color()


main()
