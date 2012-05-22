#!/usr/bin/env python2

class Frame():
    """frame"""

    def __init__(self):
        self.score = 0

    def add(self, pins):
        self.score += pins


class Game():
    """game"""

    def __init__(self):
        self._score = 0
        self._throws = [0] * 21
        self._current_throw = 0
        self.current_frame = 0

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins
        self.current_frame = 1

    def get_score(self):
        return self._score

    def score_from_frame(self, frame):
        score = 0
        ball = 0
        for i in range(frame):
            first_throw = self._throws[ball]
            ball += 1
            second_throw = self._throws[ball]
            ball += 1
            frame_score = first_throw + second_throw

            if frame_score == 10:
                frame_score += self._throws[ball]

            score += frame_score

        return score
