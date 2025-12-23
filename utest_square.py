import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    
    def test_area_positive(self):
        """Тест площади квадрата с положительной стороной"""
        result = area(5)
        self.assertEqual(result, 25)
    
    def test_area_zero(self):
        """Тест площади квадрата со стороной 0"""
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_one(self):
        """Тест площади квадрата со стороной 1"""
        result = area(1)
        self.assertEqual(result, 1)
    
    def test_perimeter_positive(self):
        """Тест периметра квадрата с положительной стороной"""
        result = perimeter(5)
        self.assertEqual(result, 20)
    
    def test_perimeter_zero(self):
        """Тест периметра квадрата со стороной 0"""
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_decimal(self):
        """Тест периметра квадрата с дробной стороной"""
        result = perimeter(2.5)
        self.assertEqual(result, 10.0)

if __name__ == '__main__':
    unittest.main()
