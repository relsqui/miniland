#!/usr/bin/python

import time
import sys
import pickle


class Player(object):
    def __init__(self, name):
        self.name = name


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
        time_string = "{} years, {} months, {} days, and {}.{} hours"
        return time_string.format(self.years, self.months, self.days, self.hours, self.minutes)

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


class Game(object):
    def __init__(self, player, clock):
        self.player = player
        self.clock = clock


    def loop(self):
        while True:
            line = raw_input("> ")
            self.clock.update()
            if line == "quit":
                break
            elif line.startswith("name "):
                name = line.split(None, 1)[1]
                self.player.name = name
                print("OK. Hi, {n}.".format(n=name))
            elif line == "save":
                self.save()
                print("OK. Saved.")
            elif line == "tick":
                print(self.clock.tick)
            elif line == "time":
                print(self.clock.time())
            elif line == "who":
                print("You are {n}.".format(n=self.player.name))
            else:
                print("OK ({l})".format(l=line))

    def save(self):
        with open("savefile", "w") as f:
            self.last_tick = self.clock.tick
            self.last_timestamp = int(time.time())
            pickle.dump(self, f, 0)


def load(filename=None):
    if filename is None:
        filename = "savefile"
    try:
        with open(filename, "r") as f:
            game = pickle.load(f)
            last_tick = game.last_tick
            game.clock.update()
            diff_ticks = MiniTime(game.clock.tick - last_tick)
            print("Welcome back! I haven't seen you in {t}.".format(t=str(diff_ticks)))
            return game
    except IOError as e:
        if e.errno == 2:
            # File doesn't exist.
            print("Welcome! What shall I call you?")
            name = raw_input("% ")
            print("Hi, {n}.".format(n=name))
            return Game(Player(name), Clock())
        else:
            print("Couldn't read savefile ('{e}'). Quitting, just to be safe.".format(e=e.strerror))
            sys.exit(2)

def main():
    game = load()
    game.loop()
    game.save()
    print("Saved. Goodbye!")

if __name__ == "__main__":
    main()
