def solution_two(a, b, max_sum):
    if sum(a) + sum(b) <= max_sum:
        return len(a) + len(b)

    def get_right(lst, left, right):
        sum_check = sum(lst[left: right])
        while sum_check > max_sum and right > left:
            sum_check -= lst[right]
            right -= 1
        return right

    def check_average(lst_a, a_left, a_right, lst_b, b_left, b_right):
        a_numerator = sum(lst_a[a_left: a_right])
        a_denominator = len(lst_a[a_left: a_right])
        b_numerator = sum(lst_b[b_left: b_right])
        b_denominator = len(lst_b[b_left: b_right])
        if a_left == a_right:
            a_numerator = lst_a[left_a]
            a_denominator = 1
        if b_left == b_right:
            b_numerator = lst_b[left_b]
            b_denominator = 1
        if a_numerator/a_denominator == b_numerator/b_denominator:
            return lst_a[left_a] > lst_b[left_b]
        return a_numerator/a_denominator > b_numerator/b_denominator

    left_a, left_b = 0, 0
    right_a, right_b = len(a) - 1, len(b) - 1
    counter = 0
    while max_sum >= 0:
        # print(left_a, right_a, left_b, right_b)
        if left_a <= right_a and left_b <= right_b:
            right_a, right_b = get_right(a, left_a, right_a), get_right(b, left_b, right_b)
            if check_average(a, left_a, right_a, b, left_b, right_b):
                max_sum -= b[left_b]
                left_b += 1
            else:
                max_sum -= a[left_a]
                left_a += 1
        elif left_b <= right_b:
            right_b = get_right(b, left_b, right_b)
            max_sum -= b[left_b]
            left_b += 1
        elif left_a <= right_a:
            right_a = get_right(a, left_a, right_a)
            max_sum -= a[left_a]
            left_a += 1
        else:
            return counter
        counter += 1
        if max_sum == 0:
            return counter
    return counter - 1


if __name__ == '__main__':
    # n, m, s = tuple(map(int, input().split()))
    # ab, a_, b_ = [], [], []
    # for i in range(max(n, m)):
    #     ab.append(list(map(lambda x: int(x) if x.isdigit() else x, input().split())))
    # a_ = [x[0] for x in ab if isinstance(x[0], int)]
    # b_ = [x[1] for x in ab if isinstance(x[1], int)]
    # print(solution_two(a_, b_, s))
    print(solution_two([3, 2, 3, 6, 2, 10], [2, 7, 3, 5, 8, 9], 10))
    print(solution_two([1, 1, 1], [1, 1, 1], 6))
    print(solution_two([1, 7, 3, 1], [1, 5, 3, 10, 7], 3))
