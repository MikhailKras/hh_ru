class GraphDFS:
    def __init__(self, graph):
        self.N = len(graph)
        self.M = len(graph[0])
        self.graph = graph
        self.visited = set()
        self.top = []
        self.down = []
        self.first_last = []
        self.coords = set()
        self.clip = []

    def check_item(self, i, j):
        return 0 <= i < self.N and 0 <= j < self.M and (i, j) not in self.visited and self.graph[i][j]

    def dfs(self, i, j):
        row_adj = [-1, 0, 1, -1, 1, -1, 0, 1]
        col_adj = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.visited.add((i, j))
        for h in range(8):
            if self.check_item(i + row_adj[h], j + col_adj[h]):
                self.dfs(i + row_adj[h], j + col_adj[h])

    def get_coords(self):
        counter = 0
        for i in range(self.N):
            for j in range(self.M):
                if (i, j) not in self.visited and self.graph[i][j]:
                    self.clip.append(self.visited)
                    self.dfs(i, j)
                    self.top.append((i, j))
                    self.graph[i][j] = 'x'
                    counter += 1
        print(f'{self.clip=}')

        self.visited.clear()
        for i in range(self.N-1, -1, -1):
            for j in range(self.M-1, -1, -1):
                if (i, j) not in self.visited and self.graph[i][j]:
                    self.dfs(i, j)
                    self.down.append((i, j))
                    self.graph[i][j] = 'z'

        for first, last in zip(range(len(self.top)), range(len(self.down) - 1, -1, -1)):
            self.first_last.append([self.top[first], self.down[last]])
        #     self.graph[self.first[first][0]][self.first[first][1]], self.graph[self.last[last][0]][self.last[last][1]] = 'x', 'x'
        for row in self.graph:
            print(*row)
        return self.first_last, counter

    def clarify_coords(self):
        self.get_coords()
        # First
        # def clarify_first(x, y):


if __name__ == '__main__':
    n_input, m_input = tuple(map(int, input().split()))
    field_input = []
    for k in range(m_input):
        field_input.append(list(map(int, input().split())))
    inst = GraphDFS(field_input)
    print(inst.get_coords())
