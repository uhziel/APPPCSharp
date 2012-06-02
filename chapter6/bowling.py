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
        self._throws = [0] * 21
        self._current_throw = 0
        self._first_throw = True
        self._ball = 0
        self.current_frame = 1

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1

        self._adjust_current_frame(pins)

    def _adjust_current_frame(self, pins):
        if self._first_throw:
            if pins == 10:
                self.current_frame += 1
            else:
                self._first_throw = False
        else:
            self.current_frame += 1
            self._first_throw = True

        if self.current_frame > 11:
            self.current_frame = 11

    def get_score(self):
        return self.score_from_frame(self.current_frame - 1)

    def score_from_frame(self, frame):
        score = 0
        self._ball = 0
        for i in range(frame):
            if self.is_strike():
                frame_score = 10 + self.get_next_two_balls_for_strike()
                self._ball += 1
            elif self.is_spare():
                frame_score = 10 + self.get_next_ball_for_spare()
                self._ball += 2
            else:
                frame_score = self.get_next_two_balls_in_frame()
                self._ball += 2

            score += frame_score

        return score

    def is_strike(self):
        return self._throws[self._ball] == 10

    def is_spare(self):
        return (self._throws[self._ball] + self._throws[self._ball + 1]) == 10

    def get_next_two_balls_for_strike(self):
        return self._throws[self._ball + 1] + self._throws[self._ball + 2]

    def get_next_ball_for_spare(self):
        return self._throws[self._ball + 2]

    def get_next_two_balls_in_frame(self):
        return self._throws[self._ball] + self._throws[self._ball + 1]
