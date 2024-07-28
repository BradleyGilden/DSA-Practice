"""
Grid Traveler problem completed with tabulation method by adding right and bottom values consecutively
knowing that gridTraveler(1, 1) = 1
"""

def gridTraveler(col, row):
    """grid traveler sol"""
    table = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

    if col > 0 and row > 0:
        table[1][1] = 1

    for i in range(row + 1):
        for j in range(col + 1):
            # add current value to right and bottom
            if j < col:
                table[i][j + 1] += table[i][j]
            if i < row:
                table[i + 1][j] += table[i][j]

    return table[row][col]


if __name__ == '__main__':
    print(gridTraveler(4, 3))
    print(gridTraveler(100, 50))