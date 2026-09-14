'''A Label shows text (or an image) that the user cannot edit.'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Showing a label')
    root.geometry('400x300')

    # Every widget receives its PARENT as its first argument.
    label = tk.Label(root, text='Welcome to my program')

    # Creating a widget is not enough: it must be placed with a geometry
    # manager, otherwise it stays invisible.
    label.pack()

    # A widget takes many options.
    tk.Label(
        root,
        text='Kadoos Institute, Rasht',
        font=('Arial', 18, 'bold'),
        fg='white',                 # foreground = the color of the text
        bg="#224160",               # background
        padx=20,
        pady=10,
    ).pack(pady=20)

    root.mainloop()


if __name__ == '__main__':
    main()
