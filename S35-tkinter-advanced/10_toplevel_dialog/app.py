'''A second window: `Toplevel`, and how to make it a real dialog.

`tk.Tk()` is created ONCE, for the main window. Every other window is a
`tk.Toplevel(parent)`.

To turn a Toplevel into a proper modal dialog:

* `transient(parent)` -- it stays above its parent and minimises with it
* `grab_set()`        -- the rest of the program stops receiving clicks
* `wait_window()`     -- the caller waits until the dialog is closed

Because we wait, the dialog can RETURN a value, just like a function.
'''

import tkinter as tk


class SettingsDialog(tk.Toplevel):
    '''Ask for a user name and a font size; return them, or None on Cancel.'''

    def __init__(self, parent: tk.Misc, username: str, size: int) -> None:
        super().__init__(parent)
        self.title('Settings')
        self.geometry('320x180')
        self.resizable(False, False)

        # None means "the user cancelled".
        self.result: tuple[str, int] | None = None

        self.name_var = tk.StringVar(value=username)
        self.size_var = tk.IntVar(value=size)

        tk.Label(self, text='User name:').grid(row=0, column=0,
                                               padx=10, pady=10, sticky='e')
        tk.Entry(self, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self, text='Font size:').grid(row=1, column=0,
                                               padx=10, pady=10, sticky='e')
        tk.Spinbox(self, from_=8, to=32, textvariable=self.size_var,
                   width=5).grid(row=1, column=1, sticky='w')

        buttons = tk.Frame(self)
        buttons.grid(row=2, column=0, columnspan=2, pady=20)
        tk.Button(buttons, text='OK', width=8,
                  command=self.on_ok).pack(side='left', padx=5)
        tk.Button(buttons, text='Cancel', width=8,
                  command=self.destroy).pack(side='left', padx=5)

        self.transient(parent)      # keep it above the main window
        self.grab_set()             # make it modal
        # Closing with the X button is the same as pressing Cancel.
        self.protocol('WM_DELETE_WINDOW', self.destroy)

    def on_ok(self) -> None:
        name = self.name_var.get().strip()
        if not name:
            self.title('Settings - the name cannot be empty')
            return
        self.result = (name, self.size_var.get())
        self.destroy()


class MainWindow:
    '''The main window, which opens the dialog and uses its answer.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title('Main window')
        root.geometry('440x300')

        self.username = 'guest'
        self.size = 14

        self.label = tk.Label(root, text='')
        self.label.pack(pady=40)

        tk.Button(root, text='Settings...',
                  command=self.open_settings).pack()

        self.refresh()

    def refresh(self) -> None:
        self.label.config(text=f'Hello {self.username}!',
                          font=('Arial', self.size))

    def open_settings(self) -> None:
        dialog = SettingsDialog(self.root, self.username, self.size)
        # Nothing below this line runs until the dialog is closed.
        self.root.wait_window(dialog)
        if dialog.result is not None:
            self.username, self.size = dialog.result
            self.refresh()


def main() -> None:
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
