"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Loki Strain.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame0 = ttk.Frame(root, padding=20)
    frame0.grid()


    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    hello_button = ttk.Button(frame0, text='Hello')
    hello_button.grid()


    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    hello_button['command'] = (lambda: hel())



    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    entry = ttk.Entry(frame0)
    entry.grid()


    entry_button = ttk.Button(frame0, text='ok?')
    entry_button.grid()
    entry_button['command'] = (lambda: hello_if_ok(entry.get()))





    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    entry1 = ttk.Entry(frame0)
    entry1.grid()




    entry1_button = ttk.Button(frame0, text='we print n of em')
    entry1_button.grid()
    entry1_button['command'] = lambda: n_times(entry.get(), int(entry1.get()))





    root.mainloop()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def hel():
    print('Hello')

def hello_if_ok(x):
    if x == 'ok':
        print('Hello')
    else:
        print('Goodbye')
def n_times(s,n):
    if type(n) == int:
        for k in range(n):
            print(s)



main()
