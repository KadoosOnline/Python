'''Showing a picture -- and the famous "my image is invisible" trap.

`tk.PhotoImage` understands GIF, PNG, PGM and PPM out of the box.
(For JPEG you need the external package Pillow: `pip install pillow`.)

THE TRAP
--------
Tk does not keep a Python reference to the image; only the C level of Tk knows
about it. If the only Python name that points to the PhotoImage disappears,
the garbage collector frees the object and the label shows... nothing.
The rule is: keep the image alive yourself, for example by storing it on the
widget (`label.image = photo`) or on `self`.

Here we build the window in a class, so `self.photo` keeps the reference.
'''

import tkinter as tk
from pathlib import Path


# The picture sits next to this file, so the program works no matter which
# folder you run it from.
IMAGE_PATH = Path(__file__).parent / 'picture.gif'


class ImageWindow:
    '''A window that shows one picture.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title('Image viewer')
        self.root.geometry('600x500')

        try:
            # str() because Tk wants a plain string, not a Path.
            self.photo = tk.PhotoImage(file=str(IMAGE_PATH))
        except tk.TclError:
            # Wrong format or missing file: say so instead of crashing.
            tk.Label(root,
                     text=f'Cannot load {IMAGE_PATH.name}\n'
                          '(PhotoImage supports GIF / PNG / PGM / PPM)',
                     fg='red').pack(pady=40)
            return

        # `self.photo` is what keeps the image alive.
        tk.Label(root, image=self.photo).pack(padx=10, pady=10)
        tk.Label(root,
                 text=f'{self.photo.width()} x {self.photo.height()} pixels'
                 ).pack()


def main() -> None:
    root = tk.Tk()
    ImageWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
