#!/usr/bin/python

import time

class Clock(object):
    ticks_hour = 100
    ticks_day = 1200 # 12 hours/day
    ticks_month = 33600 # 28 days/month
    ticks_year = 403200 # 12 months/year

    def __init__(self, seed=None, speed=None):
        if seed is None:
            seed = time.time()
        self.seed = seed
        if speed is None:
            speed = 1
        self.speed = speed

    def update(self):
        self.tick = int((time.time() - self.seed) * self.speed)
        self.year = self.tick / self.ticks_year
        remaining = self.tick - (self.year * self.ticks_year)
        self.month = remaining / self.ticks_month
        remaining = remaining - (self.month * self.ticks_month)
        self.day = remaining / self.ticks_day
        remaining = remaining - (self.day * self.ticks_day)
        self.hour = remaining / self.ticks_hour
        self.minute = remaining - (self.hour * self.ticks_hour)

    def time(self):
        time_string = "It is {h}.{n:02} on day {d} of month {m}, year {y}."
        return time_string.format(y=self.year, m=self.month, d=self.day, h=self.hour, n=self.minute)


clock = Clock(speed=367)
clock.update()
while True:
    line = raw_input("> ")
    clock.update()
    if line == "quit":
        break
    elif line == "tick":
        print clock.tick
    elif line == "time":
        print clock.time()
    else:
        print "OK ({})".format(line)
