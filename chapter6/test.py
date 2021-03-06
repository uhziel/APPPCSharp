#!/usr/bin/env python2
import unittest
import bowling

class FrameTest(unittest.TestCase):
    """
    test class Frame
    """

    def test_score_no_throws(self):
        frame = bowling.Frame()
        self.assertEqual(0, frame.score)

    def test_add_one_throw(self):
        frame = bowling.Frame()
        frame.add(5)
        self.assertEqual(5, frame.score)

class GameTest(unittest.TestCase):
    """
    test class Game
    """
    _game = 0

    def setUp(self):
        self._game = bowling.Game()

    def test_two_throws_no_mark(self):
        self._game.add(5)
        self._game.add(4)
        self.assertEqual(9, self._game.get_score())
        self.assertEqual(2, self._game.current_frame)

    def test_four_throws_no_mark(self):
        self._game.add(5)
        self._game.add(4)
        self._game.add(7)
        self._game.add(2)
        self.assertEqual(18, self._game.get_score())
        self.assertEqual(9, self._game.score_from_frame(1))
        self.assertEqual(18, self._game.score_from_frame(2))
        self.assertEqual(3, self._game.current_frame)

    def test_simple_spare(self):
        self._game.add(3)
        self._game.add(7)
        self._game.add(3)
        self.assertEqual(13, self._game.score_from_frame(1))
        self.assertEqual(2, self._game.current_frame)

    def test_simple_frame_after_spare(self):
        self._game.add(3)
        self._game.add(7)
        self._game.add(3)
        self._game.add(2)
        self.assertEqual(13, self._game.score_from_frame(1))
        self.assertEqual(18, self._game.score_from_frame(2))
        self.assertEqual(18, self._game.get_score())
        self.assertEqual(3, self._game.current_frame)

    def test_simple_strike(self):
        self._game.add(10)
        self._game.add(3)
        self._game.add(6)
        self.assertEqual(19, self._game.score_from_frame(1))
        self.assertEqual(28, self._game.get_score())
        self.assertEqual(3, self._game.current_frame)

    def test_perfect_game(self):
        for i in range(12):
            self._game.add(10)

        self.assertEqual(300, self._game.get_score())
        self.assertEqual(11, self._game.current_frame)

    def test_end_of_array(self):
        for i in range(9):
            self._game.add(0)
            self._game.add(0)

        self._game.add(2)
        self._game.add(8)
        self._game.add(10)
        self.assertEqual(20, self._game.get_score())

    def test_sample_array(self):
        self._game.add(1)
        self._game.add(4)
        self._game.add(4)
        self._game.add(5)
        self._game.add(6)
        self._game.add(4)
        self._game.add(5)
        self._game.add(5)
        self._game.add(10)
        self._game.add(0)
        self._game.add(1)
        self._game.add(7)
        self._game.add(3)
        self._game.add(6)
        self._game.add(4)
        self._game.add(10)
        self._game.add(2)
        self._game.add(8)
        self._game.add(6)

        self.assertEqual(133, self._game.get_score())

    def test_heart_break(self):
        for i in range(11):
            self._game.add(10)
        self._game.add(9)

        self.assertEqual(299, self._game.get_score())

    def test_tenth_frame_spare(self):
        for i in range(9):
            self._game.add(10)
        self._game.add(9)
        self._game.add(1)
        self._game.add(1)

        self.assertEqual(270, self._game.get_score())

if __name__ == '__main__':
    unittest.main()
