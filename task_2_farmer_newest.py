def some_func(field, n, m):
    visited = set()
    region_coords = []
    row_adj = [-1, 0, 1, -1, 1, -1, 0, 1]
    col_adj = [-1, -1, -1, 0, 0, 1, 1, 1]

    def check_item(row_, col_):
        return 0 <= row_ < m and 0 <= col_ < n and (row_, col_) not in visited and field[row_][col_]

    def get_coords(start_pos):
        path = set()
        stack = [start_pos]
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.add(vertex)
            for h in range(8):
                if check_item(vertex[0] + row_adj[h], vertex[1] + col_adj[h]):
                    stack.append((vertex[0] + row_adj[h], vertex[1] + col_adj[h]))
        visited.update(path)
        return path

    for i in range(m):
        for j in range(n):
            if field[i][j] and (i, j) not in visited:
                start = (i, j)
                region_coords.append(get_coords(start))
    eff_squares = []
    if region_coords:
        region_coords = list(filter(lambda x: len(x) > 1, region_coords))
        for region in region_coords:
            region = list(region)
            min_row = region[0][0]
            min_col = region[0][1]
            max_row = region[0][0]
            max_col = region[0][1]
            for row, col in region:
                min_row = min(min_row, row)
                min_col = min(min_col, col)
                max_row = max(max_row, row)
                max_col = max(max_col, col)
            square = (max_row - min_row + 1) * (max_col - min_col + 1)
            eff = 0
            for y in range(min_row, max_row+1):
                for x in range(min_col, max_col+1):
                    if field[y][x]:
                        eff += 1
            eff_squares.append([eff/square, square])
        if eff_squares:
            return max(eff_squares)[1]
        else:
            return 0
    else:
        return 0


if __name__ == '__main__':
    n_input, m_input = tuple(map(int, input().split()))
    field_input = []
    for k in range(m_input):
        field_input.append(list(map(int, input().split())))
    print(some_func(field_input, n_input, m_input))
