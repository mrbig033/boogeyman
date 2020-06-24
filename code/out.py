class GameOut:
    def __init__(self):
        self.line = None
        self.lines = [
            [
                "Everything goes back to normal.",
                "Your journey has just begun!",
                "Please enter a valid option.",
            ],
            [
                "You drop on a pool of liquid making a splash.",
                "The evil mechas capture you.",
                "Please enter a valid option.",
            ],
            [
                "You arrive at NeoCity without problem.",
                "A mutant dog bites you in the ass. Maybe next time.",
                "Please enter a valid option.",
            ],
        ]

    def initial_text(self):
        print(
            """
    \tOn your left hand, there's a blue pill.
    \tIn the right one, there's a red pill.
    \n\t[1] Take the blue pill.
    \t[2] Take the red pill."""
        )

    def _print_fmt(self, text_in):
        print(f"\n\t{text_in}\n")

    def get_line(self, sublevel=0, level=0):
        self._print_fmt(self.lines[level - 1][sublevel])
