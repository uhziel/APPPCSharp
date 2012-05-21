#!/usr/bin/env python2

class Frame():
    """frame"""
    score = 0

    def add(self, pins):
        self.score += pins

class Game():
    """game"""

    _score = 0
    _throws = [0] * 21
    _current_throw = 0

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins

    def get_score(self):
        return self._score

    def score_from_frame(self, frame):
        score = 0
        for i in range(2 * frame):
            score += self._throws[i]

        return score
