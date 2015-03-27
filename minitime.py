#!/usr/bin/python

import time


class MiniTime(object):
    """
    There are 100 ticks/minutes in an hour,
    12 hours (1200 ticks) in a day,
    7 days (84 hours, 8400 ticks) in a week,
    4 weeks (28 days, 336 hours, 33600 ticks) in a month,
    and 12 months (48 weeks, 336 days, 4036 hours, 403600 ticks) in a year.
    """
    def __init__(self, ticks=0):
        self.set_ticks(ticks)
        self.ticks = ticks

    def __str__(self):
        time_string = "{y} years, {m} months, {d} days, and {h}.{n:02} hours"
        return time_string.format(y=self.years, m=self.months, d=self.days, h=self.hours, n=self.minutes)

    def set_ticks(self, ticks):
        self.years = 0
        while ticks > 403200:
            ticks -= 403200
            self.years += 1
        self.months = 0
        while ticks > 33600:
            ticks -= 33600
            self.months += 1
        self.days = 0
        while ticks > 1200:
            ticks -= 1200
            self.days += 1
        self.hours = 0
        while ticks > 100:
            ticks -= 100
            self.hours += 1
        self.minutes = ticks


class Clock(object):
    def __init__(self, seed=None, speed=None):
        if seed is None:
            seed = int(time.time())
        self.seed = seed
        if speed is None:
            speed = 1
        self.speed = speed

    def update(self):
        self.tick = (int(time.time()) - self.seed) * self.speed

    def time(self):
        t = MiniTime(self.tick)
        time_string = "It is {h}.{n:02} on day {d} of month {m}, year {y}."
        return time_string.format(y=t.years, m=t.months+1, d=t.days+1, h=t.hours, n=t.minutes)
