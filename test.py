import unittest
from main import DataCapture

class TestMain(unittest.TestCase):
    def setUp(self):
        self.actual = DataCapture()
        self.actual.add(1)
        self.actual.add(2)
        self.actual.add(3)
        self.actual.add(4)
        self.actual.add(5)

    def test_add_should_be_equal(self):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.actual.data, expected)
    
    def test_add_should_not_be_equal(self):
        expected = [1, 2]
        self.assertNotEqual(self.actual.data, expected)
    
    def test_add_not_an_integer(self):
        with self.assertRaises(ValueError):
            self.actual.add('a')
    
    def test_add_negative_number(self):
        with self.assertRaises(ValueError):
            self.actual.add(-1)
    
    def test_less_should_be_equal(self):
        number = 4
        expected = [1, 2, 3]
        self.assertEqual(self.actual.less(number), expected)

    def test_less_should_not_be_equal(self):
        number = 4
        expected = [1, 2, 3, 4]
        self.assertNotEqual(self.actual.less(number), expected)
    
    def test_between_should_be_equal(self):
        number1 = 2
        number2 = 4
        expected = [2, 3, 4]
        self.assertEqual(self.actual.between(number1, number2), expected)
    
    def test_between_should_not_be_equal(self):
        number1 = 2
        number2 = 4
        expected = [2, 3]
        self.assertNotEqual(self.actual.between(number1, number2), expected)

    def test_greater_should_be_equal(self):
        number = 3
        expected = [4, 5]
        self.assertEqual(self.actual.greater(number), expected)
    
    def test_greater_should_not_be_equal(self):
        number = 3
        expected = [4]
        self.assertNotEqual(self.actual.greater(number), expected)
    
    def test_build_stats_should_be_equal(self):
        expected = {
            'min': 1,
            'max': 5,
            'avg': 3,
            'sum': 15
        }
        self.assertEqual(self.actual.build_stats(), expected)

    def test_build_stats_should_not_be_equal(self):
        expected = {
            'min': 1,
            'max': 5,
            'avg': 2,
            'sum': 15
        }
        self.assertNotEqual(self.actual.build_stats(), expected)
    
if __name__ == '__main__':
    unittest.main()