#!/usr/bin/python

import game

def main():
    g = game.load()
    g.loop()
    g.save()
    print("Saved. Goodbye!")

if __name__ == "__main__":
    main()
