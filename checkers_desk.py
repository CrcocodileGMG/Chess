from checkers_base import CheckersFigure, Checker, CheckersKing, CheckersDesk
from functions import cell_to_coordinates, coordinates_to_cell
from constants import *


checkers_desk = CheckersDesk()
white_figures_dict = {"checker": Checker(WHITE),
                      "king": CheckersKing(WHITE)}
black_figures_dict = {"checker": Checker(BLACK),
                      "king": CheckersKing(BLACK)}


def chessboard_arrangement():
    print("""if you want to add figure than write 'add-figure-color-cell'
if you want to remove figure than write 'remove-cell'
if you want to set standard checkers write 'standard_checkers'
if you edited the board than write 'stop'
figures: checker, king
colors: white, black""")
    while True:
        act = input().split("-")
        if ((act[0] == "add") and (act[1] in ["checker", "king"]) and
                (act[2] in ["white", "black"]) and (len(act) == 4) and (len(act[3]) == 2)):
            try:
                if act[2] == "white":
                    checkers_desk.add(*cell_to_coordinates(act[3]), white_figures_dict.get(act[1]))
                else:
                    checkers_desk.add(*cell_to_coordinates(act[3]), black_figures_dict.get(act[1]))
            except ValueError:
                print("Input error")
        elif act[0] == "remove" and len(act) == 2:
            checkers_desk.remove(*cell_to_coordinates(act[1]))
        elif act[0] == "standard_checkers" and len(act) == 1:
            checkers_desk.standard_checkers()
        elif act[0] == "stop" and len(act) == 1:
            if (checkers_desk.is_empty() or not checkers_desk.check_continue() or
                    checkers_desk.draw(checkers_desk.get_color())):
                print("Error: the board is empty or no white/black figures or there's a draw already")
                continue
            break
        else:
            print("Input error")


def first_move_color():
    color = input("who move first(white/black): ")
    if color == "white":
        pass
    elif color == "black":
        checkers_desk.change_color()
    else:
        print("Input error")
        first_move_color()


def main():
    first_move_color()
    chessboard_arrangement()
    game = checkers_desk.check_continue()
    while game:
        print(checkers_desk)
        if checkers_desk.get_color() == WHITE:
            print("White's move")
        else:
            print("Black's move")
        cell_1, cell_2 = input("Write your move: ").split("-")
        x1, y1 = cell_to_coordinates(cell_1)
        x2, y2 = cell_to_coordinates(cell_2)
        figure = checkers_desk.get_cell(x1, y1)
        if not figure:
            print("The figure on this square was not found")
        elif figure.get_color() != checkers_desk.get_color():
            print("You choose a figure with the wrong color")
        elif figure.check_move(x1, y1, x2, y2) and checkers_desk.check_move(x1, y1, x2, y2):
            checkers_desk.move(x1, y1, x2, y2)
            checkers_desk.change_color()
        elif figure.check_attack(x1, y1, x2, y2) and checkers_desk.check_attack(x1, y1, x2, y2):
            checkers_desk.move(x1, y1, x2, y2)
            checkers_desk.clear_line(x1, y1, x2, y2)
            checkers_desk.change_color()
        else:
            print("Impossible move")
        game = checkers_desk.check_continue()
    if checkers_desk.check_winner():
        print(checkers_desk)
        print("White won")
    else:
        print(checkers_desk)
        print("Black won")


main()
