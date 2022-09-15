import unittest
from utils import Point, Presets, is_point_inside

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(0,0)
        self.p2 = Point(9, 3)

    def test_point(self):
        self.assertEqual(self.p1.x, 0)
        self.assertEqual(self.p1.y, 0)
        self.assertEqual(self.p2.x, 9)
        self.assertEqual(self.p2.y, 3)

