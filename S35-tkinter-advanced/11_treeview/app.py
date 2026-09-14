'''`ttk.Treeview`: the table widget. This is the heart of the final project.

Key points:

* `columns=(...)` names the columns; `show='headings'` hides the extra tree
  column that Treeview draws on the left by default.
* `heading(col, text=...)` is the title, `column(col, width=..., anchor=...)`
  is the look of the cells.
* `insert('', tk.END, values=(...))` adds a row and returns its ITEM ID.
* `selection()` gives the ids of the selected rows;
  `item(id)['values']` gives the cells of one row.
* Sorting by clicking a title: read all rows, sort them in Python, and put them
  back with `move()`.

A very common beginner bug: Treeview turns everything into text for display,
so `item(...)['values']` may hand back a string where you stored a number
(and vice-versa). Never trust those values as the source of truth -- keep the
real data in Python, as we do here with `self.people`.
'''

import tkinter as tk
from tkinter import ttk


PEOPLE = [
    {'name': 'Sara',  'city': 'Rasht',   'age': 21, 'score': 18.5},
    {'name': 'Ali',   'city': 'Tabriz',  'age': 25, 'score': 15.0},
    {'name': 'Reza',  'city': 'Rasht',   'age': 19, 'score': 19.75},
    {'name': 'Mina',  'city': 'Shiraz',  'age': 23, 'score': 12.25},
    {'name': 'Hasan', 'city': 'Lahijan', 'age': 30, 'score': 16.0},
]

COLUMNS = ('name', 'city', 'age', 'score')
TITLES = {'name': 'Name', 'city': 'City', 'age': 'Age', 'score': 'Score'}


class TableDemo:
    '''A searchable, sortable table.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Treeview')
        root.geometry('620x420')

        self.people = list(PEOPLE)          # the real data lives here
        self.sort_column = 'name'
        self.sort_reverse = False

        top = ttk.Frame(root)
        top.pack(fill='x', padx=10, pady=10)
        ttk.Label(top, text='Search:').pack(side='left')
        self.search_var = tk.StringVar()
        entry = ttk.Entry(top, textvariable=self.search_var, width=20)
        entry.pack(side='left', padx=5)
        # Refresh on every key press instead of waiting for a button.
        entry.bind('<KeyRelease>', lambda event: self.refresh())

        self.tree = ttk.Treeview(root, columns=COLUMNS, show='headings',
                                 selectmode='browse')
        for column in COLUMNS:
            # `lambda c=column:` freezes the current value of `column`;
            # without it every heading would sort by the LAST column.
            self.tree.heading(column, text=TITLES[column],
                              command=lambda c=column: self.sort_by(c))
            self.tree.column(column, width=120, anchor='center')
        self.tree.pack(fill='both', expand=True, padx=10)

        scrollbar = ttk.Scrollbar(root, orient='vertical',
                                  command=self.tree.yview)
        self.tree.config(yscrollcommand=scrollbar.set)

        self.status = ttk.Label(root, text='')
        self.status.pack(pady=8)

        # Double click and Enter both show the selected person.
        self.tree.bind('<Double-1>', lambda event: self.show_selected())
        self.tree.bind('<Return>', lambda event: self.show_selected())

        self.refresh()

    def visible_people(self) -> list[dict]:
        '''The rows that match the search box.'''
        needle = self.search_var.get().strip().lower()
        if not needle:
            return self.people
        return [person for person in self.people
                if needle in person['name'].lower()
                or needle in person['city'].lower()]

    def refresh(self) -> None:
        '''Rebuild the table from scratch: clear, then insert.'''
        self.tree.delete(*self.tree.get_children())
        rows = sorted(self.visible_people(),
                      key=lambda person: person[self.sort_column],
                      reverse=self.sort_reverse)
        for person in rows:
            self.tree.insert('', tk.END,
                             values=tuple(person[c] for c in COLUMNS))
        self.status.config(text=f'{len(rows)} of {len(self.people)} rows')

    def sort_by(self, column: str) -> None:
        '''Click the same title twice to reverse the order.'''
        if column == self.sort_column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = column
            self.sort_reverse = False
        self.refresh()

    def show_selected(self) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0])['values']
        self.status.config(text=f'Selected: {values[0]} from {values[1]}')


def main() -> None:
    root = tk.Tk()
    TableDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
