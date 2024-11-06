import unittest
from math_quiz import random_from_to, random_operator, calculate_problem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_from_to(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for _ in range(1000):
            rand_op = random_operator()
            self.assertTrue(rand_op in ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1,3,'-', '1 - 3', -2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                self.assertEqual(calculate_problem(num1,num2,operator)[0],expected_problem)
                self.assertEqual(calculate_problem(num1,num2,operator)[1],expected_answer)

if __name__ == "__main__":
    unittest.main()
