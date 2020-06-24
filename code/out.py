class GameOut:
    def __init__(self, usr_choice, line):
        self.usr_choice = usr_choice
        self.line = line

    def initial_text(self):
        print(
            """
    \tOn your left hand, there's a blue pill.
    \tIn the right one, there's a red pill.
    \n\t[1] Take the blue pill.
    \t[2] Take the red pill."""
        )

    def dialogue_chooser(self, level, sublevel):
        lines = [
            [
                "Everything goes back to normal.",
                "Your journey has just begun!",
                "Please enter a valid option.",
            ],
            ["L11", "L12", "L13"],
            ["L21", "L22", "L23"],
        ]
        self.line = lines[level][sublevel]

    def _print_fmt(self, text_in):
        print(f"\n\t{text_in}\n")

    def chooser(self, usr_choice):
        self.usr_choice = usr_choice
        if self.usr_choice == "1":
            self._print_fmt(
                "Everything goes back to normal."
            )
        elif self.usr_choice == "2":
            self._print_fmt(
                "Your journey has just begun!"
            )
        else:
            self._print_fmt(
                "Please enter a valid option."
            )

    def print_out(self):
        if self.usr_choice == "1":
            self._print_fmt(
                "Everything goes back to normal."
            )
        elif self.usr_choice == "2":
            self._print_fmt(
                "Your journey has just begun!"
            )
        else:
            self._print_fmt(
                "Please enter a valid option."
            )
