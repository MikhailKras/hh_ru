import unittest
from task_1_resumes import solution_two as func


class TestResumes(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(func([1, 2, 3], [1, 2, 3, 4], 11), 5)

    def test_case2(self):
        self.assertEqual(func([5, 1, 1, 1, 1], [1, 3, 3, 3, 3], 10), 6)

    def test_case3(self):
        self.assertEqual(func([4, 2, 4, 6, 1, 7], [2, 1, 8, 5], 10), 4)

    def test_last_item_big(self):
        self.assertEqual(func([2, 2, 20, 3], [1, 1, 1, 1000], 3), 3)

    def test_big_sum(self):
        self.assertEqual(func([1, 1, 1], [1, 1, 1], 1000), 6)


if __name__ == '__main__':
    unittest.main()