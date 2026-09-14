'''Everything you can ask of the window itself.

* `geometry('WxH+X+Y')`  -- size AND position on the screen
* `resizable(False, False)` -- forbid resizing (width, height)
* `minsize()` / `maxsize()` -- limits when resizing IS allowed
* `attributes('-topmost', True)` -- keep the window above the others
* `winfo_screenwidth()` / `winfo_screenheight()` -- the size of the screen,
  which is what we need to centre a window
* `iconify()` / `deiconify()` -- minimise and restore
'''

import tkinter as tk


def centre(window: tk.Misc, width: int, height: int) -> None:
    '''Place `window` in the middle of the screen with the given size.'''
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    # The format is 'WIDTHxHEIGHT+X+Y'.
    window.geometry(f'{width}x{height}+{x}+{y}')


class WindowOptions:
    '''Buttons that change the window they live in.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title('Window options')
        centre(root, 460, 320)
        root.minsize(300, 200)      # cannot be made smaller than this

        self.locked = False
        self.on_top = False

        tk.Label(root, text='Try the buttons, then resize the window.',
                 font=('Arial', 11)).pack(pady=15)

        self.lock_button = tk.Button(root, text='Lock the size',
                                     width=22, command=self.toggle_lock)
        self.lock_button.pack(pady=4)

        self.top_button = tk.Button(root, text='Always on top: off',
                                    width=22, command=self.toggle_topmost)
        self.top_button.pack(pady=4)

        tk.Button(root, text='Centre again', width=22,
                  command=lambda: centre(root, 460, 320)).pack(pady=4)

        tk.Button(root, text='Minimise for 2 seconds', width=22,
                  command=self.blink).pack(pady=4)

    def toggle_lock(self) -> None:
        self.locked = not self.locked
        self.root.resizable(not self.locked, not self.locked)
        self.lock_button.config(
            text='Unlock the size' if self.locked else 'Lock the size')

    def toggle_topmost(self) -> None:
        self.on_top = not self.on_top
        self.root.attributes('-topmost', self.on_top)
        self.top_button.config(
            text=f'Always on top: {"on" if self.on_top else "off"}')

    def blink(self) -> None:
        self.root.iconify()                       # minimise
        # `after` runs deiconify 2000 ms later WITHOUT freezing the program.
        self.root.after(2000, self.root.deiconify)


def main() -> None:
    root = tk.Tk()
    WindowOptions(root)
    root.mainloop()


if __name__ == '__main__':
    main()
