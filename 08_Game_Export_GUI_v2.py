
from tkinter import *
from functools import partial # to prevent unwanted windows

import random



class Game:
    def __init__(self):

        # Formatting variable  ...
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with the user calculations
        self.round_stats_list = ['silver ($4) | copper ($2) | lead ($0) - Cost:$10 | Payback: $6 | Current Balance: $46'
                                 'silver ($4) | copper ($2) | lead ($0) - Cost:$10 | Payback: $6 | Current Balance: $46',
                                 'silver ($4) | gold ($10) | lead ($0) - Cost:$10 | Payback: $14 | Current Balance: $50']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                font="Arial 24 bold", padx=10, pady=10)
        self.heading_label.grid(row=0)

        # Instructions
        self.stats_button= Button(self.game_frame, text="Game Stats",
                                    font="Arial 14", pady=10, padx=10,
                                    command=lambda: self.to_stats(self.round_stats_list,self.game_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_history, game_stats):
        GameStats(self, game_history, game_stats)

class GameStats:
    def __init__(self, partner, game_history, game_stats):

        print(game_history)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # if user press cross at the top, closes help and 'releases' help button
        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,partner))

        # set up GUI
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Heading (row 0)
        self.stats_heading_label = Label(self.stats_frame, text="Game Statistics", font="arial 19 bold")

        self.stats_heading_label.grid(row=0)

        # To export <instruction> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Here are you Game Statistics."
                                               "Please use the Export button to"
                                               "access the result of each"
                                               "round that you played",
                                         wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10,pady=10)
        self.export_instructions.grid(row=1)

        # Start Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Starting balance (row 2.0)
        self.start_balance_label = Label(self.details_frame, text="Starting Balance: ", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0,padx=0 )

        self.start_balance_value_label = Label(self.details_frame,  font=content,
                                               text="${}".format(game_stats[1]),anchor="w")
        self.start_balance_value_label.grid(row=0, column=1,padx=0 )


        # Current Balance (row 2.2)
        self.current_balance_label = Label(self.details_frame, text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="${}".format(game_stats[1]),anchor="w")
        self.current_balance_value_label.grid(row=1,column=1, padx=0)

        if game_stats[1] > game_stats[0]:
            win_loss = "Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost (row 2.3)
        self.wind_loss_label = Label(self.details_frame, text=win_loss, font=heading, anchor="e")

        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount), fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=1, padx=0)

        # round played (row 2.4)
        self.game_played_label = Label(self.details_frame, text="Round Played", font=heading,anchor="e")

        self.game_played_label.grid(row=4, column= 0, padx = 0)

        self.game_played_value_label = Label(self.details_frame, font=content, text=len(game_history), anchor="w")

        self.game_played_value_label.grid(row=4, column=1, padx=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white", font="arial 14 bold",
                                  command=partial(self.close_stats, partner))

        self.dismiss_btn.grid(row=5,column=0 , pady=10)

        # Export Button
        self.export_button = Button(self.details_frame, text="Export",
                                    font="Arial 12 bold", command=lambda: self.export(game_history, game_stats))
        self.export_button.grid(row=5, column=1)

    def close_stats(self, partner):
        # put help button back to normal...
        partner.stats_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, game_history, all_game_stats):
        Export(self, game_history, all_game_stats)


class Export:
    def __init__(self, partner, game_history, all_game_stats):

        print(game_history)

        # disable help button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.export_box = Toplevel()

        # if user press cross at the top, closes help and 'releases' help button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # set yp export heading row 0
        self.how_heading = Label(self.export_frame, text="Export/ Instruction", font="arial 14 bold")
        self.how_heading.grid(row=0)

        # history text (label, row 1 )
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename "
                                      "in the box below"
                                      "and press the SAVE "
                                      "button to save your "
                                      "calculation history"
                                      "to the text file",
                                 wrap=250, font="arial 10 italic",
                                 justify=LEFT, width=40)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "entered below"
                                                         "already exists,"
                                                         "its content will be "
                                                         "replaced with your calculation history",
                                 justify=LEFT, bg='#ffafaf', fg='maroon',
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg='maroon')
        self.save_error_label.grid(row=4)

        # Save \ Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save \ Cancel BUTTON (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history, all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self,partner, game_history, game_stats):

            # Regular expression to check filename is valid
            valid_char = "[A-Za-z0-9_]"
            has_error = "no"

            filename = self.filename_entry.get()
            print(filename)

            # filename = input("Enter a filename: ")
            # print(filename)

            for letter in filename:
                if re.match(valid_char, letter):
                    continue

                elif letter == " ":
                    problem = "(no spaces allowed)"
                else:
                    problem = ("(no {}'s allowed)".format(letter))
                has_error = "yes"
                break

            if filename == "":
                problem = "can't be blank"
                has_error = "yes"

            if has_error == "yes":
                # Display error message
                self.save_error_label.config(text="invalid filename - {}".format(problem))
                # Change entry box background to pick
                self.filename_entry.config(bg="#ffafaf")
                print()

            else:
                # if there are no error, generate text file and then close dialouge
                filename = filename + ".txt"

                # create file to hold data
                f = open(filename, "w+")

                # Heading for Stats
                f.write("Game Statistics \n\n")

                # Game stats
                for round in game_stats:
                    f.write(round + "\n")

                # Heading for Rounds
                f.write("\nRound Details\n\n")

                # add new line at the end of each item
                for item in game_history:
                    f.write(item + "\n")

                # close file
                f.close()

    def close_export(self, partner):
        # Put export button back
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Game()
    root.mainloop()
