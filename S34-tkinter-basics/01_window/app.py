'''The smallest possible Tkinter program: one empty window.'''

import tkinter as tk


def main() -> None:
    # Tk() creates the main window. There must be exactly one per program.
    root = tk.Tk()

    root.title('A simple program')      # the text of the title bar
    root.geometry('400x300')            # 'WIDTHxHEIGHT', in pixels

    # mainloop() starts the EVENT LOOP: the program now waits for clicks and
    # key presses, and it does not return until the window is closed.
    # Nothing written after mainloop() runs before that.
    root.mainloop()


if __name__ == '__main__':
    main()
