#!/usr/bin/env python2
import unittest
import bowling

class FrameTest(unittest.TestCase):
    """
    test class frame
    """

    def test_score_no_throws(self):
        frame = bowling.Frame()
        self.assertEqual(0, frame.score)

if __name__ == '__main__':
    unittest.main()
