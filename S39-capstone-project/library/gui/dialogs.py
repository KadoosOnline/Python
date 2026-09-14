'''The three modal forms, each one built from a Qt Designer file.

They all follow the same contract (the one of session 35/36):

    dialog = BookDialog(parent, book)
    if dialog.exec():                 # True when the user pressed Save
        data = dialog.data            # already validated

`QDialog.exec()` shows the dialog modally and returns when it is closed:
truthy for `accept()`, falsy for `reject()`. That is the Qt version of the
`wait_window()` we used in tkinter.

The dialogs validate the SHAPE of the data (is the year a number? is the title
empty?). They do NOT know the rules of the library ("this book is already
out") -- those live in `core/services.py` and are checked when the data is
saved. Keeping the two apart is what stops a rule from being written twice.
'''

from PySide6.QtWidgets import (QComboBox, QDialog, QDialogButtonBox,
                               QLineEdit, QMessageBox, QPlainTextEdit,
                               QSpinBox, QVBoxLayout, QWidget)

from core.models import Book, Member

from .ui_loader import find, load_ui


class BaseDialog(QDialog):
    '''A QDialog whose content comes from a .ui file.

    QUiLoader gives us a separate QDialog widget, so we put it inside ours in
    a layout and keep the Save/Cancel wiring here, in one place.
    '''

    UI_FILE = ''

    def __init__(self, parent: QWidget | None, title: str) -> None:
        super().__init__(parent)
        self.setWindowTitle(title)

        self.ui = load_ui(self.UI_FILE)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui)
        self.resize(self.ui.size())

        self.buttons = find(self.ui, QDialogButtonBox, 'buttonBox')
        # `accepted` is emitted by Save/OK, `rejected` by Cancel.
        self.buttons.accepted.connect(self.on_accept)
        self.buttons.rejected.connect(self.reject)

        self.data: dict = {}

    def on_accept(self) -> None:
        '''Validate; call `self.accept()` only when everything is right.'''
        errors = self.collect()
        if errors:
            QMessageBox.warning(self, 'Please check the form',
                                '\n'.join(f'- {message}' for message in errors))
            return
        self.accept()

    def collect(self) -> list[str]:
        '''Fill `self.data` and return the list of problems.'''
        raise NotImplementedError


class BookDialog(BaseDialog):
    '''Add or edit a book.'''

    UI_FILE = 'book_dialog.ui'

    def __init__(self, parent: QWidget | None, book: Book | None = None) -> None:
        super().__init__(parent, 'Edit the book' if book else 'New book')

        self.title_edit = find(self.ui, QLineEdit, 'editTitle')
        self.author_edit = find(self.ui, QLineEdit, 'editAuthor')
        self.publisher_edit = find(self.ui, QLineEdit, 'editPublisher')
        self.year_edit = find(self.ui, QLineEdit, 'editYear')
        self.isbn_edit = find(self.ui, QLineEdit, 'editIsbn')
        self.description_edit = find(self.ui, QPlainTextEdit,
                                     'editDescription')

        if book is not None:
            self.title_edit.setText(book.title)
            self.author_edit.setText(book.author or '')
            self.publisher_edit.setText(book.publisher or '')
            self.year_edit.setText(str(book.year) if book.year else '')
            self.isbn_edit.setText(book.isbn or '')
            self.description_edit.setPlainText(book.description or '')

        self.title_edit.setFocus()

    def collect(self) -> list[str]:
        errors = []

        title = self.title_edit.text().strip()
        if len(title) < 2:
            errors.append('The title must be at least 2 characters long.')

        year_text = self.year_edit.text().strip()
        year = None
        if year_text:
            # An empty year is fine; a year that is not a number is not.
            if not year_text.isdigit() or not 1000 <= int(year_text) <= 2100:
                errors.append('The year must be a number between 1000 and 2100.')
            else:
                year = int(year_text)

        if errors:
            return errors

        self.data = {'title': title,
                     'author': self.author_edit.text().strip(),
                     'publisher': self.publisher_edit.text().strip(),
                     'year': year,
                     'isbn': self.isbn_edit.text().strip(),
                     'description': self.description_edit.toPlainText().strip()}
        return []


class MemberDialog(BaseDialog):
    '''Add or edit a member.'''

    UI_FILE = 'member_dialog.ui'

    def __init__(self, parent: QWidget | None,
                 member: Member | None = None) -> None:
        super().__init__(parent,
                         'Edit the member' if member else 'New member')

        self.first_edit = find(self.ui, QLineEdit, 'editFirstName')
        self.last_edit = find(self.ui, QLineEdit, 'editLastName')
        self.card_edit = find(self.ui, QLineEdit, 'editCardNumber')
        self.phone_edit = find(self.ui, QLineEdit, 'editPhone')
        self.email_edit = find(self.ui, QLineEdit, 'editEmail')

        if member is not None:
            self.first_edit.setText(member.first_name)
            self.last_edit.setText(member.last_name)
            self.card_edit.setText(member.card_number)
            self.phone_edit.setText(member.phone or '')
            self.email_edit.setText(member.email or '')

        self.first_edit.setFocus()

    def collect(self) -> list[str]:
        errors = []

        first = self.first_edit.text().strip()
        last = self.last_edit.text().strip()
        card = self.card_edit.text().strip()
        phone = self.phone_edit.text().strip()
        email = self.email_edit.text().strip()

        if not first:
            errors.append('The first name cannot be empty.')
        if not last:
            errors.append('The last name cannot be empty.')
        if not card.isdigit():
            errors.append('The card number must be digits only.')
        if phone and (len(phone) != 11 or not phone.startswith('09')
                      or not phone.isdigit()):
            errors.append('A phone number is 11 digits and starts with 09.')
        if email and '@' not in email:
            errors.append('That does not look like an e-mail address.')

        if errors:
            return errors

        self.data = {'first_name': first, 'last_name': last,
                     'card_number': card, 'phone': phone, 'email': email}
        return []


class LendDialog(BaseDialog):
    '''Choose a member and an available book.'''

    UI_FILE = 'lend_dialog.ui'

    def __init__(self, parent: QWidget | None, members: list[Member],
                 books: list[Book]) -> None:
        super().__init__(parent, 'Lend a book')

        self.member_combo = find(self.ui, QComboBox, 'comboMember')
        self.book_combo = find(self.ui, QComboBox, 'comboBook')
        self.days_spin = find(self.ui, QSpinBox, 'spinDays')

        # addItem(text, userData): Qt carries the id for us, so we never have
        # to parse it back out of the text (session 35 had to split a string).
        for member in members:
            self.member_combo.addItem(str(member), member.id)
        for book in books:
            self.book_combo.addItem(str(book), book.id)

        # Nothing to lend? Say so and disable Save instead of failing later.
        if not members or not books:
            self.buttons.button(QDialogButtonBox.StandardButton.Ok).setEnabled(
                False)

    def collect(self) -> list[str]:
        if self.member_combo.currentIndex() < 0:
            return ['There is no member to lend to.']
        if self.book_combo.currentIndex() < 0:
            return ['Every book is already lent out.']

        self.data = {'member_id': self.member_combo.currentData(),
                     'book_id': self.book_combo.currentData(),
                     'days': self.days_spin.value()}
        return []
