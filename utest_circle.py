import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    
    def test_area_radius_one(self):
        """Тест площади круга с радиусом 1"""
        result = area(1)
        expected = math.pi
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_area_radius_zero(self):
        """Тест площади круга с радиусом 0"""
        result = area(0)
        self.assertEqual(result, 0)
    
    def test_area_radius_positive(self):
        """Тест площади круга с радиусом 5"""
        result = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_radius_one(self):
        """Тест периметра круга с радиусом 1"""
        result = perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_perimeter_radius_zero(self):
        """Тест периметра круга с радиусом 0"""
        result = perimeter(0)
        self.assertEqual(result, 0)
    
    def test_perimeter_radius_positive(self):
        """Тест периметра круга с радиусом 3"""
        result = perimeter(3)
        expected = 6 * math.pi
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
