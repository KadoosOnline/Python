'''`Canvas`: drawing, and mouse events with `bind`.

`bind(sequence, function)` connects an event to a function. The function
receives an EVENT object; `event.x` and `event.y` are the mouse position
inside the widget.

Useful sequences:
    '<Button-1>'         left button pressed
    '<B1-Motion>'        moved while the left button is held down
    '<ButtonRelease-1>'  left button released
    '<Key>' / '<Return>' a key / the Enter key

Canvas drawing methods return an ITEM ID, which you can later move, recolour
or delete: `create_line`, `create_oval`, `create_rectangle`, `create_text`.
'''

import tkinter as tk
from tkinter import colorchooser


class PaintApp:
    '''A very small drawing program.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Paint')
        root.geometry('640x480')

        self.colour = 'black'
        self.width = 3
        # The point the line is drawn from; None while the button is up.
        self.last: tuple[int, int] | None = None

        toolbar = tk.Frame(root)
        toolbar.pack(fill='x', padx=5, pady=5)
        tk.Button(toolbar, text='Colour...',
                  command=self.pick_colour).pack(side='left', padx=2)
        tk.Button(toolbar, text='Erase all',
                  command=self.clear).pack(side='left', padx=2)
        tk.Scale(toolbar, from_=1, to=20, orient='horizontal',
                 label='Thickness',
                 command=self.set_width).pack(side='left', padx=10)
        self.preview = tk.Label(toolbar, text='   ', bg=self.colour)
        self.preview.pack(side='left', padx=10)

        self.canvas = tk.Canvas(root, bg='white')
        self.canvas.pack(fill='both', expand=True, padx=5, pady=5)

        self.canvas.bind('<Button-1>', self.start_stroke)
        self.canvas.bind('<B1-Motion>', self.draw)
        self.canvas.bind('<ButtonRelease-1>', self.end_stroke)

    def pick_colour(self) -> None:
        # askcolor returns ((r, g, b), '#rrggbb') or (None, None) on Cancel.
        _rgb, hex_colour = colorchooser.askcolor(color=self.colour)
        if hex_colour:
            self.colour = hex_colour
            self.preview.config(bg=self.colour)

    def set_width(self, value: str) -> None:
        self.width = int(value)

    def clear(self) -> None:
        # 'all' is the tag every item carries.
        self.canvas.delete('all')

    def start_stroke(self, event: tk.Event) -> None:
        self.last = (event.x, event.y)

    def draw(self, event: tk.Event) -> None:
        if self.last is None:
            return
        # A stroke is a chain of short straight lines between two mouse events.
        self.canvas.create_line(self.last[0], self.last[1], event.x, event.y,
                                fill=self.colour, width=self.width,
                                capstyle='round', smooth=True)
        self.last = (event.x, event.y)

    def end_stroke(self, event: tk.Event) -> None:
        self.last = None


def main() -> None:
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
