import fileinput


def main():

    matrix = []
    color_islands = 0

    for line in fileinput.input():
        if line == '\n':
            break
        matrix.append(list(line.rstrip('\n')))

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 'X':
                color = matrix[row][col]
                matrix[row][col] = 'X'
                fill_color(color, row, col, matrix)
                color_islands += 1
                for new_row in matrix:
                    print(" ".join(new_row))
                print("####################", '\n')

    print(color_islands)


def fill_color(color, row, col, matrix):

    for neighbour in find_neighbors(row, col, len(matrix) - 1, len(matrix[0]) - 1):
        if matrix[neighbour[0]][neighbour[1]] == color:
            matrix[neighbour[0]][neighbour[1]] = 'X'
            fill_color(color, neighbour[0], neighbour[1], matrix)


def find_neighbors(row, col, X_max, Y_max):
    return [(x2, y2) for x2 in range(row - 1, row + 2)
            for y2 in range(col - 1, col + 2)
            if (-1 < row <= X_max and
                -1 < col <= Y_max and
                (row != x2 or col != y2) and
                (0 <= x2 <= X_max) and
                (0 <= y2 <= Y_max))]


if __name__ == '__main__':
    main()
