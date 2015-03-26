#!/usr/bin/python

import time
import sys
import pickle


class Player(object):
    def __init__(self, name):
        self.name = name


class Clock(object):
    def __init__(self, seed=None, speed=None):
        self.ticks_hour = 100
        self.ticks_day = 1200 # 12 hours/day
        self.ticks_month = 33600 # 28 days/month
        self.ticks_year = 403200 # 12 months/year
        if seed is None:
            seed = int(time.time())
        self.seed = seed
        if speed is None:
            speed = 1
        self.speed = speed

    def update(self):
        self.tick = (int(time.time()) - self.seed) * self.speed
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
            pickle.dump(self, f, 0)
            print("Saved. Goodbye!")


def load(filename=None):
    if filename is None:
        filename = "savefile"
    try:
        with open(filename, "r") as f:
            game = pickle.load(f)
            print("Welcome back!")
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

if __name__ == "__main__":
    main()
