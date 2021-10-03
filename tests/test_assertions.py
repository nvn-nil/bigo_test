# -*- coding: utf-8 -*-
import unittest

from bigo_test.assertions import assertBigO
from bigo_test.complexity import Linear, Quadratic
from bigo_test.exceptions import WrongTimeComplexity


class TestBasicAssertions(unittest.TestCase):
    def test_simple_sorting_function_assertion(self):
        def max_function(number_list):
            max_ = 0
            for el in number_list:
                if el > max_:
                    max_ = el
            return max_

        def input_generator(numbers):
            return list(range(numbers))

        assertBigO(max_function, input_generator, Linear)

        with self.assertRaises(WrongTimeComplexity):
            assertBigO(max_function, input_generator, Quadratic)


if __name__ == "__main__":
    unittest.main()
