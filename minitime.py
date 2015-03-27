#!/usr/bin/python

import time
import math
import functools

import string_utils


@functools.total_ordering
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

    def __eq__(self, other):
        return self.ticks == other.ticks

    def __lt__(self, other):
        return self.ticks < other.ticks

    def __add__(self, other):
        return MiniTime(int(self) + int(other))

    def __sub__(self, other):
        return MiniTime(int(self) - int(other))

    def __int__(self):
        return self.ticks

    def __str__(self):
        keys = ["year", "month", "day", "hour", "minute"]
        keys = [k for k in keys if self[k+"s"]]
        strings = dict()
        for key in keys:
            count = self[key+"s"]
            denomination = key + string_utils.s(count)
            strings[key] = "{c} {d}".format(c=count, d=denomination)
        if keys == ["hour", "minute"]:
            return "{h}.{n:02}".format(h=self.hours, n=self.minutes)
        return string_utils.comma_and([strings[k] for k in keys])

    def __getitem__(self, key):
        return self.__dict__[key]

    def get_dict(self):
        return {"years":self.years, "months":self.months, "days":self.days, 
                "hours":self.hours, "minutes":self.minutes}

    def set_ticks(self, ticks):
        self.ticks = ticks
        self.years = 0
        while ticks >= 403200:
            ticks -= 403200
            self.years += 1
        self.months = 0
        while ticks >= 33600:
            ticks -= 33600
            self.months += 1
        self.days = 0
        while ticks >= 1200:
            ticks -= 1200
            self.days += 1
        self.day_of_year = self.days + (28 * self.months)
        self.hours = 0
        while ticks >= 100:
            ticks -= 100
            self.hours += 1
        self.minutes = ticks

    def time(self):
        return MiniTime(self.hours * 100 + self.minutes)

    def date(self):
        return self - self.time()


class Clock(object):
    def __init__(self, seed=None):
        if seed is None:
            seed = int(time.time())
        self.seed = seed
        self.last_tick = 0
        self.last_timestamp = seed
        self.speed = 1

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

    def almanac(self):
        parameters = dict()
        string = "Sunrise {rise_tense} at {rise}. Sunset {set_tense} at {set}."
        now = self.t.time()
        if self.sunrise < now:
            parameters["rise_tense"] = "was"
        else:
            parameters["rise_tense"] = "is"
        if self.sunset < now:
            parameters["set_tense"] = "was"
        else:
            parameters["set_tense"] = "is"
        parameters["rise"] = str(self.sunrise)
        parameters["set"] = str(self.sunset)
        return string.format(**parameters)

    def time(self):
        t = self.t
        time_string = "It is {t} on day {d} of month {m}, year {y}."
        times = {"t":str(t.time()), "d":t.days, "m":t.months, "y":t.years}
        time_string = time_string.format(**times)
        speed_string = "Current clock speed is {speed}x.".format(speed=self.speed)
        return "\n".join([time_string, self.almanac(), speed_string])
