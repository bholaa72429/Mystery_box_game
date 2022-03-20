from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery heading (row 0)
        self.mystery_box_label = Label(self.start_frame,
                                        text="Mystery Box Game",
                                        font="Arial 19 bold",
                                        #bg=background_color,
                                        padx=10, pady=10)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                          "(between $5 and $50) in the box "
                                          "below. Then choose the stakes."
                                          "The higher the stakes, "
                                          "the more you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)


        # Entry box... (row 2)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 15 bold")
        self.start_amount_entry.grid(row=2)

        # button frame (row=3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Button goes here ...
        button_font = "Arial 12 bold"

        # ORANGE low stakes button
        self.lowstakes_button = Button(self.stakes_frame,text="Low ($5)",
                                       command=lambda: self.to_game(1),
                                       font=button_font, bg="#FF9933")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # YELLOW medium stakes button...
        self.lowstakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                       command=lambda: self.to_game(2),
                                       font=button_font, bg="#99FF33")

        self.lowstakes_button.grid(row=2, column=2, pady=10)

        # GREEN high stakes button
        self.lowstakes_button = Button(self.stakes_frame, text="High ($15)",
                                       command=lambda: self.to_game(3),
                                       font=button_font, bg="#09FF33")
        self.lowstakes_button.grid(row=0, column=0, pady=10)

        # Help button
        self.help_button = Button(self.start_frame, text="Help to Play",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=4,pady=10)


    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)

class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()