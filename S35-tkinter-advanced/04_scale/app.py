'''`Scale`: a slider that gives a number.

Two things to notice:

* The function given to `command=` is called by Tk with ONE argument: the new
  value, and it arrives as a STRING ('14'), never as an int.
* `widget.config(option=value)` changes an option after the widget was built.
  Here we change the font size of a label live.
'''

import tkinter as tk


class FontSizeDemo:
    '''A label whose font size follows a slider.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Slider')
        root.geometry('420x300')

        self.label = tk.Label(root, text='Sample text', font=('Arial', 14))
        self.label.pack(pady=20)

        scale = tk.Scale(root, from_=10, to=40, orient='horizontal',
                         length=250, label='Font size',
                         command=self.update_font)
        scale.set(14)               # this also fires update_font once
        scale.pack()

    def update_font(self, value: str) -> None:
        '''Tk passes the slider position as a string.'''
        self.label.config(font=('Arial', int(value)))


def main() -> None:
    root = tk.Tk()
    FontSizeDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
