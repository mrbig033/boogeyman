#!/usr/bin/env python3

from os import system
from usr_in import UsrInput
from out import GameOut

system("clear")


class Game:
    def __init__(self):
        self.level = 0
        self.usr_input = UsrInput()
        self.out = GameOut()

    def run(self):
        self.out.initial_text()
        self.usr_input.get_input()
        self.out.print_out(
            self.level, self.usr_input.usr_in
        )
        self.level += 1


game = Game()
game.run()
