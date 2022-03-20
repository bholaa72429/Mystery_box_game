from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)


    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # hide starts up window
        root.withdraw()

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variable
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of the game
        self.balance.set(starting_balance)

        # GUI setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions
        self.instruction_label = Label(self.game_frame, wrap=300,
                                       justify=LEFT, text="Press enter. ",
                                       font="Arial 10", pady=10, padx=10)
        self.instruction_label.grid(row=1)



        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=3)

        self.play_button = Button(self.game_frame, text="Gain",
                                  padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=3)

    def reveal_boxes(self):
        # retrievel the balance from the initial function
        current_balance = self.balance.get()

        # Adjust the balance (subject game )
        # For testing purposes, just add 2
        current_balance += 2

        # set balance to adjsuted balance
        self.balance.set(current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()
