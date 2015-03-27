#!/usr/bin/python

import time
import sys
import pickle

import minitime


class Player(object):
    def __init__(self, name):
        self.name = name


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
            elif line.startswith("speed"):
                if " " in line:
                    self.clock.speed = int(line.split(None, 1)[1])
                else:
                    self.clock.speed = 1
                print("OK. Going at {s}x speed.".format(s=self.clock.speed))
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


def load(filename=None):
    if filename is None:
        filename = "savefile"
    try:
        with open(filename, "r") as f:
            game = pickle.load(f)
            diff_ticks = game.clock.update()
            print("Welcome back! I haven't seen you in {t}.".format(t=str(diff_ticks)))
            return game
    except IOError as e:
        if e.errno == 2:
            # File doesn't exist.
            print("Welcome! What shall I call you?")
            name = raw_input("% ")
            print("Hi, {n}.".format(n=name))
            return Game(Player(name), minitime.Clock())
        else:
            print("Couldn't read savefile ('{e}'). Quitting, just to be safe.".format(e=e.strerror))
            sys.exit(2)
