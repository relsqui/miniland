#!/usr/bin/python

import time
import math


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
        self.ticks = ticks
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
        self.day_of_year = self.days + (28 * self.months)
        self.hours = 0
        while ticks > 100:
            ticks -= 100
            self.hours += 1
        self.minutes = ticks

    def time(self):
        return "{h}.{n:02}".format(h=self.hours, n=self.minutes)


class Clock(object):
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time())
        self.seed = seed

    def __getstate__(self):
        odict = self.__dict__.copy()
        odict["speed"] = 1
        return odict

    def update(self):
        self.tick = self.last_tick
        self.tick += (int(time.time()) - self.last_timestamp) * self.speed
        diff_ticks = self.tick - self.last_tick
        self.last_tick = self.tick
        self.last_timestamp = int(time.time())
        self.t = MiniTime(self.tick)
        sun_offset = int(math.cos(2*math.pi*self.t.day_of_year/336)*100)+100
        self.sunrise = MiniTime(sun_offset)
        self.sunset = MiniTime(800 - sun_offset)
        return MiniTime(diff_ticks)

    def time(self):
        t = self.t
        time_string = "It is {h}.{n:02} on day {d} of month {m}, year {y}."
        times = {"h":t.hours, "n":t.minutes, "d":t.days, "m":t.months, "y":t.years}
        time_string = time_string.format(**times)
        sun_string = "Sunrise is at {rise}. Sunset is at {set}."
        suns = {"rise":self.sunrise.time(), "set":self.sunset.time()}
        sun_string = sun_string.format(**suns)
        speed_string = "Current clock speed is {speed}x.".format(speed=self.speed)
        return "\n".join([time_string, sun_string, speed_string])
