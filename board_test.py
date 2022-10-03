import unittest
from board import Board, PipeType
from utils import Point, Presets

class TestBoard(unittest.TestCase):

    board = None

    @classmethod
    def setUpClass(cls):
        pass

    def test_setting_field(self):
        presets = Presets().with_width(10).with_height(10).with_end_point(Point(9, 9)).validate()

        board = Board(presets)
        p1_ok = Point(0,0)
        p2_ok = Point(9, 9)
        p3_bad = Point(9, 10)
        p4_bad = Point(-1,2)
        self.assertTrue(p1_ok in board)
        self.assertTrue(p2_ok in board)
        self.assertFalse(p3_bad in board)
        self.assertFalse(p4_bad in board)

        with self.assertRaises(IndexError):
            board.get_pipe(p3_bad)

        with self.assertRaises(IndexError):
            board.get_pipe(p4_bad)

        self.assertEqual(board.set_pipe(p1_ok, '╩'), '╩')
        self.assertEqual(board.set_pipe(p1_ok, ' '), ' ')

        with self.assertRaises(ValueError):
            board.set_pipe(p1_ok, 'x')

class TestField(unittest.TestCase):
    def test_symbol_validation(self):        
        self.assertTrue(PipeType.validate_symbol('╩'))
        self.assertTrue(PipeType.validate_symbol(' '))
        self.assertFalse(PipeType.validate_symbol('x'))
