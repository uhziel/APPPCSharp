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

    def test_one_throw(self):
        game = bowling.Game()
        game.add(4)
        self.assertEqual(4, game.get_score())

    def test_two_throws_no_mark(self):
        game = bowling.Game()
        game.add(5)
        game.add(4)
        self.assertEqual(9, game.get_score())

    def test_four_throws_no_mark(self):
        game = bowling.Game()
        game.add(5)
        game.add(4)
        game.add(7)
        game.add(2)
        self.assertEqual(18, game.get_score())
        self.assertEqual(9, game.score_from_frame(1))
        self.assertEqual(18, game.score_from_frame(2))

if __name__ == '__main__':
    unittest.main()
