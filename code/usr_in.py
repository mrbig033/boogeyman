#!/usr/bin/env python3


class UsrInput:
    def __init__(self):
        self.usr_in = None

    def get_input(self):
        self.usr_in = input(
            "\n\tEnter the desired dialogue option:\n\t"
        )
        return self.usr_in
