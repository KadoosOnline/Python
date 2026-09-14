'''A Frame is an invisible box used to GROUP widgets.

Each frame has its own geometry manager, so one part of the window can use
pack() while another uses grid().
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Using frames')
    root.geometry('400x300')

    # fill='x' -> the frame takes the whole width.
    top_frame = tk.Frame(root, bg='lightblue', height=100)
    top_frame.pack(fill='x')

    tk.Label(top_frame, text='Top section', bg='lightblue').pack(pady=30)

    # fill='both' + expand=True -> the frame takes all the remaining space.
    bottom_frame = tk.Frame(root, bg='darkred')
    bottom_frame.pack(fill='both', expand=True)

    # side= decides where pack() puts the widget inside its parent.
    tk.Button(bottom_frame, text='Left button').pack(side='left',
                                                     padx=10, pady=10)
    tk.Button(bottom_frame, text='Right button').pack(side='right',
                                                      padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
