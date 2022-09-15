import unittest
from board import Point, Board, Fields

class TestBoard(unittest.TestCase):

    board = None

    @classmethod
    def setUpClass(cls):
        pass

    def test_setting_field(self):
        board = Board(width=10, height=10)
        p1_ok = Point(0,0)
        p2_ok = Point(9, 9)
        p3_bad = Point(9, 10)
        p4_bad = Point(-1,2)
        self.assertTrue(p1_ok in board)
        self.assertTrue(p2_ok in board)
        self.assertFalse(p3_bad in board)
        self.assertFalse(p4_bad in board)

        with self.assertRaises(IndexError):
            board.get_field(p3_bad)

        with self.assertRaises(IndexError):
            board.get_field(p4_bad)

        self.assertEqual(board.set_field(p1_ok, '╩'), '╩')
        self.assertEqual(board.set_field(p1_ok, ' '), ' ')

        with self.assertRaises(ValueError):
            board.set_field(p1_ok, 'x')

class TestField(unittest.TestCase):

    def test_symbol_validation(self):        
        self.assertTrue(Fields.validate_sign('╩'))
        self.assertTrue(Fields.validate_sign(' '))
        self.assertFalse(Fields.validate_sign('x'))
