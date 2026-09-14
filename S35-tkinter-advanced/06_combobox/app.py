'''`ttk`: the themed widgets -- and `Combobox`, the drop-down list.

`tkinter.ttk` contains newer versions of several widgets. They look like the
buttons of the operating system and they add widgets that plain `tkinter` does
not have at all: `Combobox`, `Notebook`, `Treeview`, `Progressbar`.

Rule of thumb for this course: use `ttk` when it offers the widget, and plain
`tk` for `Text`, `Canvas` and `Listbox` (ttk has no version of those).

`state='readonly'` stops the user from typing his own value in the box.
`<<ComboboxSelected>>` is a VIRTUAL event: we react with `bind`, not `command`.
'''

import tkinter as tk
from tkinter import ttk


CITIES = {
    'Rasht': 'Gilan',
    'Bandar Anzali': 'Gilan',
    'Lahijan': 'Gilan',
    'Tabriz': 'East Azerbaijan',
    'Shiraz': 'Fars',
    'Mashhad': 'Razavi Khorasan',
}


class ComboboxDemo:
    '''Choose a city, see its province.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Combobox')
        root.geometry('420x260')

        ttk.Label(root, text='City:').pack(pady=(20, 5))

        self.city_var = tk.StringVar()
        combo = ttk.Combobox(root, textvariable=self.city_var,
                             values=list(CITIES), state='readonly', width=25)
        combo.current(0)                    # select the first entry
        combo.pack()

        # A virtual event: it fires every time the selection changes.
        combo.bind('<<ComboboxSelected>>', self.on_select)

        self.answer = ttk.Label(root, text='', font=('Arial', 12))
        self.answer.pack(pady=20)

        self.on_select()                    # show the first answer at once

    def on_select(self, event: 'tk.Event | None' = None) -> None:
        '''`bind` calls us with an event object; `self.on_select()` does not.'''
        city = self.city_var.get()
        self.answer.config(text=f'{city} is in {CITIES[city]} province.')


def main() -> None:
    root = tk.Tk()
    ComboboxDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
