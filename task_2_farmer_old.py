def get_square(field, n, m):
    left_border = []  # 1, 4 ,5
    up_border = []  # 2, 3
    down_border = []  # 6, 7
    symb = 7
    for row in range(m):
        for col in range(n):
            if field[row][col] == 0:
                if row == 0:
                    if col == 0:  # 1
                        if not (field[row][col + 1], field[row + 1][col]) == (1, 1):
                            field[row][col] = symb
                            left_border.append([row, col])
                    elif col == n-1:  # 3
                        if not (field[row][col - 1], field[row + 1][col]) == (1, 1):
                            field[row][col] = symb
                            up_border.append([row, col])
                    else:  # 2
                        if not (field[row][col - 1], field[row + 1][col], field[row][col + 1]) == (1, 1, 1):
                            field[row][col] = symb
                            up_border.append([row, col])
                elif row == m-1:
                    if col == 0:  # 5
                        if not (field[row][col + 1], field[row - 1][col]) == (1, 1):
                            field[row][col] = symb
                            left_border.append([row, col])
                    elif col == n-1:  # 7
                        if not (field[row][col - 1], field[row - 1][col]) == (1, 1):
                            field[row][col] = symb
                            down_border.append([row, col])
                    else:  # 6
                        if not (field[row][col - 1], field[row - 1][col], field[row][col + 1]) == (1, 1, 1):
                            field[row][col] = symb
                            down_border.append([row, col])
                elif col == 0:  # 4
                    if not (field[row-1][col], field[row + 1][col], field[row][col + 1]) == (1, 1, 1):
                        field[row][col] = symb
                        left_border.append([row, col])
                elif col == n-1:  # 8
                    if not (field[row-1][col], field[row + 1][col], field[row][col - 1]) == (1, 1, 1):
                        field[row][col] = symb
                else:  # 9
                    if not ((field[row-1][col], field[row + 1][col], field[row][col + 1], field[row][col - 1]) == (1, 1, 1, 1)
                            or sorted([field[row-1][col], field[row + 1][col], field[row][col + 1], field[row][col - 1]]) in ((0, 1, 1, 1), (1, 1, 1, symb))):
                        field[row][col] = symb
    symb_out = '-'
    for row in field:
        row.insert(0, symb_out)
        row.insert(len(row), symb_out)
    field.insert(0, [symb_out for _ in range(len(field[0]))])
    field.insert(len(field), [symb_out for _ in range(len(field[0]))])
    cash = set()

    # def road(row, col):


    for row in field:
        print(*row)


if __name__ == '__main__':
    n_input, m_input = tuple(map(int, input().split()))
    field_input = []
    for k in range(m_input):
        field_input.append(list(map(int, input().split())))
    get_square(field_input, n_input, m_input)