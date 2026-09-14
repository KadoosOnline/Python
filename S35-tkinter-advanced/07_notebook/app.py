'''`ttk.Notebook`: several pages (tabs) in one window.

Each tab is simply a `Frame` that we hand to `notebook.add()`. Everything we
already know -- labels, buttons, grid, pack -- works inside that frame.

`ttk.Progressbar` shows up here as a bonus: `determinate` mode is driven by its
`value` (0-100).
'''

import tkinter as tk
from tkinter import ttk


class NotebookDemo:
    '''A window with three tabs.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Tabs')
        root.geometry('520x400')

        notebook = ttk.Notebook(root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        notebook.add(self._build_welcome_tab(notebook), text='Welcome')
        notebook.add(self._build_form_tab(notebook), text='Form')
        notebook.add(self._build_progress_tab(notebook), text='Progress')

    def _build_welcome_tab(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent)
        ttk.Label(frame, text='Welcome to the first tab!',
                  font=('Arial', 14)).pack(pady=40)
        return frame

    def _build_form_tab(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent)
        ttk.Label(frame, text='Name:').grid(row=0, column=0, padx=10, pady=10)
        self.name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1)
        self.hello = ttk.Label(frame, text='')
        self.hello.grid(row=1, column=0, columnspan=2, pady=20)
        ttk.Button(frame, text='Say hello',
                   command=self.say_hello).grid(row=2, column=0, columnspan=2)
        return frame

    def _build_progress_tab(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent)
        self.bar = ttk.Progressbar(frame, length=300, mode='determinate')
        self.bar.pack(pady=40)
        ttk.Button(frame, text='+10 %',
                   command=self.step_bar).pack()
        return frame

    def say_hello(self) -> None:
        name = self.name_var.get().strip()
        self.hello.config(text=f'Hello {name}!' if name else 'Type a name.')

    def step_bar(self) -> None:
        # The bar stops at 100; start again from zero.
        self.bar['value'] = (self.bar['value'] + 10) % 110


def main() -> None:
    root = tk.Tk()
    NotebookDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
