'''The two modal forms of the library application.

Both dialogs follow the pattern of example 10:

    dialog = BookDialog(parent, book=row)
    parent.wait_window(dialog)
    if dialog.result is not None:
        ...   # the user pressed Save

`result` is a dictionary of clean, already validated values -- the caller never
has to look inside the widgets.
'''

import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


class FormDialog(tk.Toplevel):
    '''Shared behaviour of the two forms: modal, Save / Cancel, Enter, Escape.'''

    def __init__(self, parent: tk.Misc, title: str) -> None:
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.result: dict | None = None

        self.body = ttk.Frame(self, padding=10)
        self.body.pack(fill='both', expand=True)

        buttons = ttk.Frame(self, padding=(10, 0, 10, 10))
        buttons.pack(fill='x')
        ttk.Button(buttons, text='Save', width=10,
                   command=self.on_save).pack(side='right', padx=4)
        ttk.Button(buttons, text='Cancel', width=10,
                   command=self.destroy).pack(side='right')

        self.bind('<Return>', lambda event: self.on_save())
        self.bind('<Escape>', lambda event: self.destroy())
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.transient(parent)
        self.grab_set()

    def add_field(self, row: int, label: str, value: str = '') -> tk.StringVar:
        '''Add one "label + entry" line and give back its variable.'''
        ttk.Label(self.body, text=label).grid(row=row, column=0,
                                              padx=5, pady=5, sticky='e')
        variable = tk.StringVar(value=value)
        entry = ttk.Entry(self.body, textvariable=variable, width=30)
        entry.grid(row=row, column=1, padx=5, pady=5)
        if row == 0:
            entry.focus_set()       # the cursor starts in the first field
        return variable

    def on_save(self) -> None:
        '''Subclasses validate, fill `self.result` and call `self.destroy()`.'''
        raise NotImplementedError


class BookDialog(FormDialog):
    '''Add or edit one book.'''

    def __init__(self, parent: tk.Misc, book: sqlite3.Row | None = None) -> None:
        super().__init__(parent, 'Edit the book' if book else 'New book')
        # `book['author'] or ''` because a NULL column arrives as None.
        self.title_var = self.add_field(0, 'Title:', book['title'] if book else '')
        self.author_var = self.add_field(1, 'Author:',
                                         (book['author'] or '') if book else '')
        self.isbn_var = self.add_field(2, 'ISBN:',
                                       (book['isbn'] or '') if book else '')
        self.year_var = self.add_field(
            3, 'Year:', str(book['year']) if book and book['year'] else '')

    def on_save(self) -> None:
        title = self.title_var.get().strip()
        if not title:
            messagebox.showerror('Invalid form',
                                 'The title cannot be empty.', parent=self)
            return

        year_text = self.year_var.get().strip()
        year: int | None = None
        if year_text:
            # An empty year is allowed; a wrong one is not.
            if not year_text.isdigit() or not 1000 <= int(year_text) <= 2100:
                messagebox.showerror('Invalid form',
                                     'The year must be between 1000 and 2100.',
                                     parent=self)
                return
            year = int(year_text)

        self.result = {'title': title,
                       'author': self.author_var.get().strip(),
                       'isbn': self.isbn_var.get().strip(),
                       'year': year}
        self.destroy()


class MemberDialog(FormDialog):
    '''Add or edit one member.'''

    def __init__(self, parent: tk.Misc,
                 member: sqlite3.Row | None = None) -> None:
        super().__init__(parent, 'Edit the member' if member else 'New member')
        self.name_var = self.add_field(0, 'Name:',
                                       member['name'] if member else '')
        self.phone_var = self.add_field(
            1, 'Phone:', (member['phone'] or '') if member else '')
        self.email_var = self.add_field(
            2, 'E-mail:', (member['email'] or '') if member else '')

    def on_save(self) -> None:
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror('Invalid form',
                                 'The name cannot be empty.', parent=self)
            return

        email = self.email_var.get().strip()
        if email and '@' not in email:
            messagebox.showerror('Invalid form',
                                 'That does not look like an e-mail address.',
                                 parent=self)
            return

        self.result = {'name': name,
                       'phone': self.phone_var.get().strip(),
                       'email': email}
        self.destroy()
