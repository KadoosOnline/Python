'''messagebox: the standard dialog boxes.

    showinfo / showwarning / showerror  -> just an OK button
    askyesno / askokcancel              -> return True or False
    askquestion                         -> returns 'yes' or 'no'
'''

import tkinter as tk
from tkinter import messagebox


def main() -> None:
    root = tk.Tk()
    root.title('Message boxes')
    root.geometry('400x300')

    def show_info() -> None:
        messagebox.showinfo('Information', 'This is an information message')

    def show_warning() -> None:
        messagebox.showwarning('Warning', 'This is a warning')

    def show_error() -> None:
        messagebox.showerror('Error', 'A critical error happened')

    def ask_question() -> None:
        # The answer is used to decide what to do next.
        if messagebox.askyesno('Question', 'Do you want to close the program?'):
            root.destroy()

    tk.Button(root, text='Show information', command=show_info).pack(pady=5)
    tk.Button(root, text='Show a warning', command=show_warning).pack(pady=5)
    tk.Button(root, text='Show an error', command=show_error).pack(pady=5)
    tk.Button(root, text='Ask and quit', command=ask_question).pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
