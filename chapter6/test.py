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

    def test_one_throw(self):
        self._game.add(4)
        self.assertEqual(4, self._game.get_score())
        self.assertEqual(1, self._game.current_frame)

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

    def test_simple_frame_after_spare(self):
        self._game.add(3)
        self._game.add(7)
        self._game.add(3)
        self._game.add(2)
        self.assertEqual(13, self._game.score_from_frame(1))
        self.assertEqual(18, self._game.score_from_frame(2))

if __name__ == '__main__':
    unittest.main()
