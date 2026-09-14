'''A windowed application, built to survive being frozen into an .exe.

Two things make this example different from a normal PySide6 program:

1. Every path goes through `paths.py` (read the comments in that file).
   `notes.json` is saved next to the executable, so the notes are still there
   the next time the user starts the program.

2. There is no `print()` for errors. A `--windowed` build has NO console at
   all: `print` output goes nowhere and an uncaught exception kills the
   program in silence. Anything the user must see goes into a QMessageBox,
   and anything you want for yourself goes into a log FILE (session 19).

Build it with:

    pyinstaller --onefile --windowed --icon=app.ico app.py

Then run `dist/app.exe`, add a few notes, close it, and start it again: the
notes are still there, and `notes.json` sits next to the .exe.
'''

import json
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QListWidget, QMessageBox, QPushButton,
                               QVBoxLayout, QWidget)

from paths import data_path, is_frozen, resource_path


NOTES_FILE = 'notes.json'


class NotesWindow(QWidget):
    '''A note list that saves itself to a JSON file.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Kadoos notes')
        self.resize(460, 380)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText('a new note...')
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add_note)
        self.edit.returnPressed.connect(self.add_note)

        top = QHBoxLayout()
        top.addWidget(self.edit)
        top.addWidget(add_button)

        self.list_widget = QListWidget()

        remove_button = QPushButton('Remove the selected note')
        remove_button.clicked.connect(self.remove_note)

        # Showing where the file lives makes the lesson visible at run time.
        self.status = QLabel(f'file: {data_path(NOTES_FILE)}\n'
                             f'frozen: {is_frozen()}')
        self.status.setWordWrap(True)
        self.status.setStyleSheet('color: gray; font-size: 11px;')

        layout = QVBoxLayout()
        layout.addLayout(top)
        layout.addWidget(self.list_widget)
        layout.addWidget(remove_button)
        layout.addWidget(self.status)
        self.setLayout(layout)

        self.load_notes()

    def load_notes(self) -> None:
        path = data_path(NOTES_FILE)
        if not path.exists():           # first run: nothing to load
            return
        try:
            with open(path, 'r', encoding='utf-8') as file:
                notes = json.load(file)
        except (OSError, json.JSONDecodeError) as error:
            # No console in a --windowed build: the user must SEE this.
            QMessageBox.warning(self, 'Cannot read the notes',
                                f'{path}\n\n{error}')
            return
        self.list_widget.addItems(notes)

    def save_notes(self) -> None:
        notes = [self.list_widget.item(row).text()
                 for row in range(self.list_widget.count())]
        path = data_path(NOTES_FILE)
        try:
            with open(path, 'w', encoding='utf-8') as file:
                # ensure_ascii=False keeps Persian text readable in the file.
                json.dump(notes, file, ensure_ascii=False, indent=2)
        except OSError as error:
            QMessageBox.critical(self, 'Cannot save the notes',
                                 f'{path}\n\n{error}')

    def add_note(self) -> None:
        text = self.edit.text().strip()
        if not text:
            return
        self.list_widget.addItem(text)
        self.edit.clear()
        self.save_notes()

    def remove_note(self) -> None:
        row = self.list_widget.currentRow()
        if row < 0:
            return
        self.list_widget.takeItem(row)
        self.save_notes()


def main() -> None:
    app = QApplication(sys.argv)

    # The window icon is read from the bundle, so it goes through
    # resource_path(); it must be shipped with --add-data (example 12).
    icon_file = resource_path('app.ico')
    if icon_file.exists():
        app.setWindowIcon(QIcon(str(icon_file)))

    window = NotesWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
