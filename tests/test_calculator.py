import unittest

from src.calculator import add, subtract, divide
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(subtract(2, 4), -2)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(50, 50), 0)
    
    def test_divide(self):
        self.assertEqual(divide(-5, -5), 1)
        self.assertEqual(divide(20, 4), 5)
        self.assertEqual(divide(-5, 20), -0.25)
    
    if __name__ == '__main__':
        unittest.main()