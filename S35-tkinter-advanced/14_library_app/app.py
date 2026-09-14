'''Library manager -- the project of session 35.

It puts together everything of sessions 34 and 35 plus the SQLite of
session 31:

    Notebook   -> three tabs
    Treeview   -> the tables of books, members and current loans
    Toplevel   -> the modal Add / Edit forms (dialogs.py)
    Combobox   -> choose the member and the book to lend
    messagebox -> confirmations and errors
    sqlite3    -> the storage (database.py)

Design decisions worth remembering:

* The GUI NEVER writes SQL. It calls methods of `Database`.
* The rows we show are kept in `self.book_rows` / `self.member_rows`, indexed
  by the Treeview item id. The widget is only a display; the truth stays in
  Python. (Reading values back out of a Treeview gives you strings and
  translated words such as 'yes', which is how the original version of this
  program ended up saving the word 'yes' into the `year` column.)
* Every refresh method rebuilds one part of the screen, and an action calls
  every refresh that its change can affect -- lending a book changes the books
  tab, the loans tab AND the combo boxes.

Run it with:  python app.py
'''

import tkinter as tk
from tkinter import messagebox, ttk

from database import Database
from dialogs import BookDialog, MemberDialog


BOOK_COLUMNS = {'id': ('ID', 50), 'title': ('Title', 220),
                'author': ('Author', 150), 'isbn': ('ISBN', 110),
                'year': ('Year', 60), 'available': ('Available', 80)}

MEMBER_COLUMNS = {'id': ('ID', 50), 'name': ('Name', 180),
                  'phone': ('Phone', 120), 'email': ('E-mail', 200),
                  'join_date': ('Member since', 130)}

LOAN_COLUMNS = {'id': ('ID', 50), 'book_title': ('Book', 240),
                'member_name': ('Member', 180), 'borrow_date': ('Lent on', 130)}


def build_tree(parent: tk.Misc, columns: dict[str, tuple[str, int]]
               ) -> ttk.Treeview:
    '''Create a Treeview with a vertical scrollbar and return it.'''
    frame = ttk.Frame(parent)
    frame.pack(fill='both', expand=True, padx=5, pady=5)

    tree = ttk.Treeview(frame, columns=list(columns), show='headings',
                        selectmode='browse')
    for key, (title, width) in columns.items():
        tree.heading(key, text=title)
        tree.column(key, width=width, anchor='center')

    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    tree.config(yscrollcommand=scrollbar.set)
    tree.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')
    return tree


class LibraryApp:
    '''The main window.'''

    def __init__(self, root: tk.Tk, db: Database) -> None:
        self.root = root
        self.db = db
        root.title('Library manager')
        root.geometry('900x560')
        root.minsize(700, 450)

        # Treeview item id -> the sqlite3.Row it was built from.
        self.book_rows: dict[str, object] = {}
        self.member_rows: dict[str, object] = {}

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=8, pady=8)
        self._build_books_tab()
        self._build_members_tab()
        self._build_loans_tab()

        self.status = ttk.Label(root, anchor='w', relief='sunken', padding=4)
        self.status.pack(fill='x', side='bottom')

        self.refresh_all()
        root.protocol('WM_DELETE_WINDOW', self.on_close)

    # -- books tab ---------------------------------------------------------
    def _build_books_tab(self) -> None:
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Books')

        top = ttk.Frame(tab)
        top.pack(fill='x', padx=5, pady=5)
        ttk.Label(top, text='Search:').pack(side='left')
        self.book_search = tk.StringVar()
        entry = ttk.Entry(top, textvariable=self.book_search, width=25)
        entry.pack(side='left', padx=5)
        entry.bind('<KeyRelease>', lambda event: self.refresh_books())
        ttk.Button(top, text='Clear',
                   command=self.clear_book_search).pack(side='left')

        self.books_tree = build_tree(tab, BOOK_COLUMNS)
        self.books_tree.bind('<Double-1>', lambda event: self.edit_book())

        buttons = ttk.Frame(tab)
        buttons.pack(fill='x', padx=5, pady=5)
        ttk.Button(buttons, text='Add', command=self.add_book).pack(side='left')
        ttk.Button(buttons, text='Edit',
                   command=self.edit_book).pack(side='left', padx=4)
        ttk.Button(buttons, text='Delete',
                   command=self.delete_book).pack(side='left')

    def clear_book_search(self) -> None:
        self.book_search.set('')
        self.refresh_books()

    def refresh_books(self) -> None:
        self.books_tree.delete(*self.books_tree.get_children())
        self.book_rows.clear()
        for row in self.db.list_books(self.book_search.get().strip()):
            item = self.books_tree.insert(
                '', tk.END,
                values=(row['id'], row['title'], row['author'] or '',
                        row['isbn'] or '', row['year'] or '',
                        'yes' if row['available'] else 'no'))
            self.book_rows[item] = row

    def selected_book(self):
        '''The sqlite3.Row of the selected book, or None (with a warning).'''
        selection = self.books_tree.selection()
        if not selection:
            messagebox.showwarning('Nothing selected',
                                   'Please select a book first.')
            return None
        return self.book_rows[selection[0]]

    def add_book(self) -> None:
        dialog = BookDialog(self.root)
        self.root.wait_window(dialog)
        if dialog.result is None:
            return
        self.db.add_book(**dialog.result)
        self.refresh_all()
        self.set_status(f'Added the book "{dialog.result["title"]}".')

    def edit_book(self) -> None:
        book = self.selected_book()
        if book is None:
            return
        dialog = BookDialog(self.root, book)
        self.root.wait_window(dialog)
        if dialog.result is None:
            return
        self.db.update_book(book['id'], **dialog.result)
        self.refresh_all()
        self.set_status(f'Book #{book["id"]} updated.')

    def delete_book(self) -> None:
        book = self.selected_book()
        if book is None:
            return
        if not book['available']:
            messagebox.showerror('Cannot delete',
                                 'This book is lent out. Take it back first.')
            return
        if not messagebox.askyesno(
                'Confirm', f'Really delete "{book["title"]}"?\n'
                           'Its borrowing history goes away with it.'):
            return
        self.db.delete_book(book['id'])
        self.refresh_all()
        self.set_status(f'Book #{book["id"]} deleted.')

    # -- members tab -------------------------------------------------------
    def _build_members_tab(self) -> None:
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Members')

        top = ttk.Frame(tab)
        top.pack(fill='x', padx=5, pady=5)
        ttk.Label(top, text='Search:').pack(side='left')
        self.member_search = tk.StringVar()
        entry = ttk.Entry(top, textvariable=self.member_search, width=25)
        entry.pack(side='left', padx=5)
        entry.bind('<KeyRelease>', lambda event: self.refresh_members())
        ttk.Button(top, text='Clear',
                   command=self.clear_member_search).pack(side='left')

        self.members_tree = build_tree(tab, MEMBER_COLUMNS)
        self.members_tree.bind('<Double-1>', lambda event: self.edit_member())

        buttons = ttk.Frame(tab)
        buttons.pack(fill='x', padx=5, pady=5)
        ttk.Button(buttons, text='Add',
                   command=self.add_member).pack(side='left')
        ttk.Button(buttons, text='Edit',
                   command=self.edit_member).pack(side='left', padx=4)
        ttk.Button(buttons, text='Delete',
                   command=self.delete_member).pack(side='left')

    def clear_member_search(self) -> None:
        self.member_search.set('')
        self.refresh_members()

    def refresh_members(self) -> None:
        self.members_tree.delete(*self.members_tree.get_children())
        self.member_rows.clear()
        for row in self.db.list_members(self.member_search.get().strip()):
            item = self.members_tree.insert(
                '', tk.END,
                values=(row['id'], row['name'], row['phone'] or '',
                        row['email'] or '', row['join_date']))
            self.member_rows[item] = row

    def selected_member(self):
        selection = self.members_tree.selection()
        if not selection:
            messagebox.showwarning('Nothing selected',
                                   'Please select a member first.')
            return None
        return self.member_rows[selection[0]]

    def add_member(self) -> None:
        dialog = MemberDialog(self.root)
        self.root.wait_window(dialog)
        if dialog.result is None:
            return
        self.db.add_member(**dialog.result)
        self.refresh_all()
        self.set_status(f'Added the member "{dialog.result["name"]}".')

    def edit_member(self) -> None:
        member = self.selected_member()
        if member is None:
            return
        dialog = MemberDialog(self.root, member)
        self.root.wait_window(dialog)
        if dialog.result is None:
            return
        self.db.update_member(member['id'], **dialog.result)
        self.refresh_all()
        self.set_status(f'Member #{member["id"]} updated.')

    def delete_member(self) -> None:
        member = self.selected_member()
        if member is None:
            return
        if not messagebox.askyesno(
                'Confirm', f'Really delete "{member["name"]}"?'):
            return
        self.db.delete_member(member['id'])
        self.refresh_all()
        self.set_status(f'Member #{member["id"]} deleted.')

    # -- loans tab ---------------------------------------------------------
    def _build_loans_tab(self) -> None:
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Lend / return')

        box = ttk.LabelFrame(tab, text='Lend a book', padding=10)
        box.pack(fill='x', padx=10, pady=10)

        ttk.Label(box, text='Member:').grid(row=0, column=0, padx=5)
        self.member_combo = ttk.Combobox(box, state='readonly', width=28)
        self.member_combo.grid(row=0, column=1, padx=5)

        ttk.Label(box, text='Book:').grid(row=0, column=2, padx=5)
        self.book_combo = ttk.Combobox(box, state='readonly', width=28)
        self.book_combo.grid(row=0, column=3, padx=5)

        ttk.Button(box, text='Lend',
                   command=self.lend_book).grid(row=0, column=4, padx=10)

        # The combo boxes show text, so we keep the ids in parallel lists.
        self.member_ids: list[int] = []
        self.book_ids: list[int] = []

        box2 = ttk.LabelFrame(tab, text='Books that are out', padding=5)
        box2.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        self.loans_tree = build_tree(box2, LOAN_COLUMNS)
        ttk.Button(box2, text='Take the book back',
                   command=self.return_book).pack(pady=5)

    def refresh_combos(self) -> None:
        members = self.db.list_members()
        self.member_ids = [row['id'] for row in members]
        self.member_combo['values'] = [f'#{row["id"]} {row["name"]}'
                                       for row in members]
        books = self.db.available_books()
        self.book_ids = [row['id'] for row in books]
        self.book_combo['values'] = [f'#{row["id"]} {row["title"]}'
                                     for row in books]
        # `current(0)` fails on an empty list, so check first.
        self.member_combo.set(self.member_combo['values'][0] if members else '')
        self.book_combo.set(self.book_combo['values'][0] if books else '')

    def refresh_loans(self) -> None:
        self.loans_tree.delete(*self.loans_tree.get_children())
        for row in self.db.open_borrowings():
            self.loans_tree.insert('', tk.END,
                                   values=(row['id'], row['book_title'],
                                           row['member_name'],
                                           row['borrow_date']))

    def lend_book(self) -> None:
        member_index = self.member_combo.current()
        book_index = self.book_combo.current()
        if member_index < 0 or book_index < 0:
            messagebox.showerror('Cannot lend',
                                 'Choose both a member and an available book.')
            return
        try:
            self.db.borrow(self.book_ids[book_index],
                           self.member_ids[member_index])
        except ValueError as error:
            # Raised when the book was taken in the meantime.
            messagebox.showerror('Cannot lend', str(error))
        self.refresh_all()
        self.set_status('Loan recorded.')

    def return_book(self) -> None:
        selection = self.loans_tree.selection()
        if not selection:
            messagebox.showwarning('Nothing selected',
                                   'Please select a loan first.')
            return
        loan_id = self.loans_tree.item(selection[0])['values'][0]
        try:
            self.db.give_back(int(loan_id))
        except ValueError as error:
            messagebox.showerror('Cannot return', str(error))
        self.refresh_all()
        self.set_status('The book is back on the shelf.')

    # -- shared ------------------------------------------------------------
    def refresh_all(self) -> None:
        self.refresh_books()
        self.refresh_members()
        self.refresh_combos()
        self.refresh_loans()

    def set_status(self, message: str) -> None:
        self.status.config(text=message)

    def on_close(self) -> None:
        self.db.close()
        self.root.destroy()


def main() -> None:
    db = Database()
    root = tk.Tk()
    LibraryApp(root, db)
    root.mainloop()


if __name__ == '__main__':
    main()
