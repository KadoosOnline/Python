'''The main window: four tabs, three tables, and not one line of SQL.

Why this window is written in CODE while the dialogs come from Qt Designer:
Designer is at its best for a STATIC form -- a fixed set of labels and fields,
which is exactly what the three dialogs are. A window whose tables are built
from a dictionary of columns is shorter, and much easier to change, in Python.
Knowing when to use which is part of the job.

The two habits that keep this file honest:

1. Every screen is rebuilt by a `refresh_*` method, and an action calls
   `refresh_all()`. Trying to patch one row of a table by hand is how a
   display starts disagreeing with the database.
2. The table is a DISPLAY. The real row is remembered in
   `self.book_rows[table_row]`, never read back out of the widget. (That was
   the bug of session 35: a Treeview handed back the word "yes" for a number.)
'''

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import (QAbstractItemView, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QMainWindow, QMessageBox,
                               QPushButton, QTableWidget, QTableWidgetItem,
                               QTabWidget, QVBoxLayout, QWidget)

from core import services
from core.database import session_scope
from core.models import Book, Borrow, Member
from core.services import LibraryError

from .dialogs import BookDialog, LendDialog, MemberDialog


BOOK_COLUMNS = ['ID', 'Title', 'Author', 'Publisher', 'Year', 'State']
MEMBER_COLUMNS = ['ID', 'Name', 'Card', 'Phone', 'E-mail', 'Books out']
LOAN_COLUMNS = ['ID', 'Book', 'Member', 'Lent on', 'Due', 'State']

LATE_COLOUR = QColor('#ffd9d9')


def build_table(columns: list[str]) -> QTableWidget:
    '''A read-only table, one whole row selected at a time.'''
    table = QTableWidget(0, len(columns))
    table.setHorizontalHeaderLabels(columns)
    table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
    # The user reads the table and edits through the dialogs.
    table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setSectionResizeMode(
        1, QHeaderView.ResizeMode.Stretch)
    table.setSortingEnabled(True)
    return table


def fill_row(table: QTableWidget, row: int, values: list) -> None:
    for column, value in enumerate(values):
        item = QTableWidgetItem(str(value))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        table.setItem(row, column, item)


class MainWindow(QMainWindow):
    '''The whole application.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Kadoos library')
        self.resize(1000, 620)

        # table row -> the object it was built from
        self.book_rows: dict[int, Book] = {}
        self.member_rows: dict[int, Member] = {}
        self.loan_rows: dict[int, Borrow] = {}

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tabs.addTab(self._build_books_tab(), 'Books')
        self.tabs.addTab(self._build_members_tab(), 'Members')
        self.tabs.addTab(self._build_loans_tab(), 'Loans')
        self.tabs.addTab(self._build_stats_tab(), 'Statistics')

        self._build_menu()
        self.statusBar().showMessage('Ready')

        self.refresh_all()

    # -- menu --------------------------------------------------------------
    def _build_menu(self) -> None:
        file_menu = self.menuBar().addMenu('&File')

        refresh = QAction('&Refresh', self)
        refresh.setShortcut('F5')
        refresh.triggered.connect(self.refresh_all)
        file_menu.addAction(refresh)

        file_menu.addSeparator()

        quit_action = QAction('&Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        help_menu = self.menuBar().addMenu('&Help')
        about = QAction('&About', self)
        about.triggered.connect(self.show_about)
        help_menu.addAction(about)

    def show_about(self) -> None:
        QMessageBox.information(
            self, 'About',
            'Kadoos library\n\n'
            'The capstone project of the Python course, Rasht.\n'
            'PySide6 + SQLAlchemy.')

    # -- books tab ---------------------------------------------------------
    def _build_books_tab(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)

        self.book_search = QLineEdit()
        self.book_search.setPlaceholderText('search a title, an author...')
        # textChanged fires on every key press: the list filters as you type.
        self.book_search.textChanged.connect(self.refresh_books)

        top = QHBoxLayout()
        top.addWidget(QLabel('Search:'))
        top.addWidget(self.book_search)
        layout.addLayout(top)

        self.books_table = build_table(BOOK_COLUMNS)
        self.books_table.doubleClicked.connect(self.edit_book)
        layout.addWidget(self.books_table)

        buttons = QHBoxLayout()
        for text, slot in [('Add', self.add_book), ('Edit', self.edit_book),
                           ('Delete', self.delete_book)]:
            button = QPushButton(text)
            button.clicked.connect(slot)
            buttons.addWidget(button)
        buttons.addStretch()
        layout.addLayout(buttons)

        return page

    def refresh_books(self) -> None:
        search = self.book_search.text().strip()
        self.books_table.setSortingEnabled(False)   # sorting while filling
        self.books_table.setRowCount(0)             # scrambles the rows
        self.book_rows.clear()

        with session_scope() as session:
            for row, book in enumerate(services.list_books(session, search)):
                self.books_table.insertRow(row)
                fill_row(self.books_table, row,
                         [book.id, book.title, book.author or '',
                          book.publisher or '', book.year or '',
                          'out' if book.is_out else 'on the shelf'])
                self.book_rows[row] = book

        self.books_table.setSortingEnabled(True)

    def selected_book(self) -> Book | None:
        row = self.books_table.currentRow()
        book = self.book_rows.get(row)
        if book is None:
            QMessageBox.information(self, 'Nothing selected',
                                    'Please select a book first.')
        return book

    def add_book(self) -> None:
        dialog = BookDialog(self)
        if not dialog.exec():
            return
        with session_scope() as session:
            services.create_book(session, **dialog.data)
        self.refresh_all()
        self.statusBar().showMessage(f'"{dialog.data["title"]}" was added.')

    def edit_book(self) -> None:
        book = self.selected_book()
        if book is None:
            return
        dialog = BookDialog(self, book)
        if not dialog.exec():
            return
        try:
            with session_scope() as session:
                # The object came from a session that is now closed: fetch it
                # again inside this transaction before changing it.
                fresh = session.get(Book, book.id)
                if fresh is None:
                    raise LibraryError('That book no longer exists.')
                services.update_book(session, fresh, **dialog.data)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot save', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The book was saved.')

    def delete_book(self) -> None:
        book = self.selected_book()
        if book is None:
            return
        if QMessageBox.question(
                self, 'Confirm',
                f'Delete "{book.title}"?\nIts loan history goes with it.'
        ) != QMessageBox.StandardButton.Yes:
            return
        try:
            with session_scope() as session:
                fresh = session.get(Book, book.id)
                if fresh is not None:
                    services.delete_book(session, fresh)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot delete', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The book was deleted.')

    # -- members tab -------------------------------------------------------
    def _build_members_tab(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)

        self.member_search = QLineEdit()
        self.member_search.setPlaceholderText('search a name, a card number...')
        self.member_search.textChanged.connect(self.refresh_members)

        top = QHBoxLayout()
        top.addWidget(QLabel('Search:'))
        top.addWidget(self.member_search)
        layout.addLayout(top)

        self.members_table = build_table(MEMBER_COLUMNS)
        self.members_table.doubleClicked.connect(self.edit_member)
        layout.addWidget(self.members_table)

        buttons = QHBoxLayout()
        for text, slot in [('Add', self.add_member),
                           ('Edit', self.edit_member),
                           ('Delete', self.delete_member)]:
            button = QPushButton(text)
            button.clicked.connect(slot)
            buttons.addWidget(button)
        buttons.addStretch()
        layout.addLayout(buttons)

        return page

    def refresh_members(self) -> None:
        search = self.member_search.text().strip()
        self.members_table.setSortingEnabled(False)
        self.members_table.setRowCount(0)
        self.member_rows.clear()

        with session_scope() as session:
            for row, member in enumerate(services.list_members(session,
                                                               search)):
                self.members_table.insertRow(row)
                fill_row(self.members_table, row,
                         [member.id, member.full_name, member.card_number,
                          member.phone or '', member.email or '',
                          len(member.open_borrows)])
                self.member_rows[row] = member

        self.members_table.setSortingEnabled(True)

    def selected_member(self) -> Member | None:
        member = self.member_rows.get(self.members_table.currentRow())
        if member is None:
            QMessageBox.information(self, 'Nothing selected',
                                    'Please select a member first.')
        return member

    def add_member(self) -> None:
        dialog = MemberDialog(self)
        if not dialog.exec():
            return
        try:
            with session_scope() as session:
                services.create_member(session, **dialog.data)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot add the member', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The member was added.')

    def edit_member(self) -> None:
        member = self.selected_member()
        if member is None:
            return
        dialog = MemberDialog(self, member)
        if not dialog.exec():
            return
        try:
            with session_scope() as session:
                fresh = session.get(Member, member.id)
                if fresh is not None:
                    services.update_member(session, fresh, **dialog.data)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot save', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The member was saved.')

    def delete_member(self) -> None:
        member = self.selected_member()
        if member is None:
            return
        if QMessageBox.question(
                self, 'Confirm', f'Delete {member.full_name}?'
        ) != QMessageBox.StandardButton.Yes:
            return
        try:
            with session_scope() as session:
                fresh = session.get(Member, member.id)
                if fresh is not None:
                    services.delete_member(session, fresh)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot delete', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The member was deleted.')

    # -- loans tab ---------------------------------------------------------
    def _build_loans_tab(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)

        layout.addWidget(QLabel('Books that are out (late loans in red)'))

        self.loans_table = build_table(LOAN_COLUMNS)
        layout.addWidget(self.loans_table)

        buttons = QHBoxLayout()
        for text, slot in [('Lend a book...', self.lend_book),
                           ('Take it back', self.return_book),
                           ('Extend by 14 days', self.extend_loan)]:
            button = QPushButton(text)
            button.clicked.connect(slot)
            buttons.addWidget(button)
        buttons.addStretch()
        layout.addLayout(buttons)

        return page

    def refresh_loans(self) -> None:
        self.loans_table.setSortingEnabled(False)
        self.loans_table.setRowCount(0)
        self.loan_rows.clear()

        with session_scope() as session:
            for row, loan in enumerate(services.open_borrows(session)):
                self.loans_table.insertRow(row)
                state = (f'{loan.days_late} day(s) late' if loan.is_late
                         else 'in time')
                fill_row(self.loans_table, row,
                         [loan.id, loan.book.title, loan.member.full_name,
                          loan.borrow_date.strftime('%Y-%m-%d'),
                          loan.due_date.strftime('%Y-%m-%d'), state])
                if loan.is_late:
                    for column in range(self.loans_table.columnCount()):
                        self.loans_table.item(row, column).setBackground(
                            LATE_COLOUR)
                self.loan_rows[row] = loan

        self.loans_table.setSortingEnabled(True)

    def selected_loan(self) -> Borrow | None:
        loan = self.loan_rows.get(self.loans_table.currentRow())
        if loan is None:
            QMessageBox.information(self, 'Nothing selected',
                                    'Please select a loan first.')
        return loan

    def lend_book(self) -> None:
        with session_scope() as session:
            members = services.list_members(session)
            books = services.available_books(session)

        if not members:
            QMessageBox.information(self, 'Nobody to lend to',
                                    'Add a member first.')
            return
        if not books:
            QMessageBox.information(self, 'Nothing to lend',
                                    'Every book is already out.')
            return

        dialog = LendDialog(self, members, books)
        if not dialog.exec():
            return

        try:
            with session_scope() as session:
                book = session.get(Book, dialog.data['book_id'])
                member = session.get(Member, dialog.data['member_id'])
                if book is None or member is None:
                    raise LibraryError('That book or member no longer exists.')
                services.lend_book(session, book, member,
                                   days=dialog.data['days'])
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot lend', str(error))
            return

        self.refresh_all()
        self.statusBar().showMessage('The loan was recorded.')

    def return_book(self) -> None:
        loan = self.selected_loan()
        if loan is None:
            return
        try:
            with session_scope() as session:
                fresh = session.get(Borrow, loan.id)
                if fresh is None:
                    raise LibraryError('That loan no longer exists.')
                services.return_book(session, fresh)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot take it back', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The book is back on the shelf.')

    def extend_loan(self) -> None:
        loan = self.selected_loan()
        if loan is None:
            return
        try:
            with session_scope() as session:
                fresh = session.get(Borrow, loan.id)
                if fresh is None:
                    raise LibraryError('That loan no longer exists.')
                services.extend_loan(session, fresh)
        except LibraryError as error:
            QMessageBox.warning(self, 'Cannot extend', str(error))
            return
        self.refresh_all()
        self.statusBar().showMessage('The loan was extended by 14 days.')

    # -- statistics tab ----------------------------------------------------
    def _build_stats_tab(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        self.stats_label = QLabel()
        self.stats_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.stats_label.setStyleSheet('font-size: 14px;')
        layout.addWidget(self.stats_label)
        layout.addStretch()
        return page

    def refresh_stats(self) -> None:
        with session_scope() as session:
            numbers = services.statistics(session)

        popular = '\n'.join(f'    {title} — {times} time(s)'
                            for title, times in numbers['popular'])

        self.stats_label.setText(
            f'Books:            {numbers["books"]}\n'
            f'Members:          {numbers["members"]}\n'
            f'On loan:          {numbers["on_loan"]}\n'
            f'On the shelf:     {numbers["available"]}\n'
            f'Late:             {numbers["late"]}\n\n'
            f'Most borrowed:\n{popular or "    (nothing yet)"}\n\n'
            f'{datetime.now():%Y-%m-%d %H:%M}')

    # -- shared ------------------------------------------------------------
    def refresh_all(self) -> None:
        '''One change can affect every tab, so refresh them all.'''
        self.refresh_books()
        self.refresh_members()
        self.refresh_loans()
        self.refresh_stats()
