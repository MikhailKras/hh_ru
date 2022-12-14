from task_1_resumes import solution_two
import time
import random


def stress_test(func, size_n: tuple, size_m: tuple):
    n1, n2 = size_n
    m1, m2 = size_m
    counter = 0
    while True:
        a = [random.randint(1, 10000) for _ in range(random.randint(n1, n2))]
        b = [random.randint(1, 10000) for _ in range(random.randint(m1, m2))]
        max_sum = random.randint(1, 200_000_000)
        start = time.time()
        solution_two(a, b, max_sum)
        end = time.time() - start
        counter += 1
        if end > 1:
            print(f'time: {end}s', len(a), len(b), max_sum)
            break
        # print(counter, a, b, max_sum, f'time: {end}s')
        # print(f'time: {end}s', len(a), len(b), max_sum)


stress_test(solution_two, (3, 10000), (3, 10000))
