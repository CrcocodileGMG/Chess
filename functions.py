def cell_to_coordinates(cell: str) -> list:
    return ["ABCDEFGH".index(cell[0]) + 1, int(cell[1])]


def coordinates_to_cell(x, y) -> str:
    return "ABCDEFGH"[x - 1] + str(y)
