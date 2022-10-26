from task_2_farmer_old import get_square as func
from task_2_farmer_new import GraphDFS
from task_2_farmer_newest import some_func
import random


def stress_tests(f, range_n: tuple, range_m: tuple, iterations, cls=False):
    for i in range(iterations):
        n = random.randint(*range_n)
        m = random.randint(*range_m)
        field = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
        for row in field:
            print(*row)
        if cls:
            cls = GraphDFS(field)
            print(cls.get_coords())
        else:
            f(field, n, m)
        print('-'*20)


if __name__ == '__main__':
    n1, n2 = 2, 100
    stress_tests(some_func, (n1, n2), (n1, n2), 20000, cls=False)
