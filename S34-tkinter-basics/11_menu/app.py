'''A menu bar.

    Menu(root)                 -> the bar itself
    root.config(menu=menubar)  -> attach it to the window
    add_cascade                -> a menu that opens a sub-menu
    add_command                -> an entry that runs a function
    tearoff=0                  -> remove the old dashed line at the top
'''

import tkinter as tk
from tkinter import messagebox


def main() -> None:
    root = tk.Tk()
    root.title('A program with a menu')
    root.geometry('400x300')

    label = tk.Label(root, text='Use the menu above', font=('Arial', 14))
    label.pack(pady=50)

    def new_file() -> None:
        label.config(text='New file')

    def open_file() -> None:
        label.config(text='Open file')

    def show_about() -> None:
        messagebox.showinfo('About', 'This program is a teaching example.')

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New', command=new_file)
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_separator()
    # root.destroy() closes the window properly; root.quit() only stops the loop.
    file_menu.add_command(label='Exit', command=root.destroy)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=help_menu)
    help_menu.add_command(label='About', command=show_about)

    root.mainloop()


if __name__ == '__main__':
    main()
