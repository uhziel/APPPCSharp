#!/usr/bin/env python2

class Frame():
    """frame"""
    score = 0

    def add(self, pins):
        self.score += pins

class Game():
    """game"""

    _score = 0

    def add(self, pins):
        self._score += pins

    def get_score(self):
        return self._score
