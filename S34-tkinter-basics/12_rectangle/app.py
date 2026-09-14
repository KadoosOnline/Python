'''A small calculation form.

The important part is the VALIDATION: everything an Entry gives back is text,
so float() can fail and must be protected.
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Rectangle')
    root.geometry('320x220')

    tk.Label(root, text='Length:').grid(row=0, column=0,
                                        padx=10, pady=5, sticky='e')
    entry_length = tk.Entry(root, width=20)
    entry_length.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text='Width:').grid(row=1, column=0,
                                       padx=10, pady=5, sticky='e')
    entry_width = tk.Entry(root, width=20)
    entry_width.grid(row=1, column=1, padx=10, pady=5)

    result = tk.Label(root, text='')
    result.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate() -> None:
        try:
            length = float(entry_length.get())
            width = float(entry_width.get())
        except ValueError:
            result.config(text='Please enter two numbers.', fg='red')
            return

        if length <= 0 or width <= 0:
            result.config(text='The values must be positive.', fg='red')
            return

        area = length * width
        perimeter = (length + width) * 2
        result.config(text=f'Area: {area:g}   Perimeter: {perimeter:g}',
                      fg='green')

    tk.Button(root, text='Calculate', command=calculate).grid(
        row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
