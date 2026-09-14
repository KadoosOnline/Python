'''`QMessageBox`: the four standard dialogs, and asking a question.

    QMessageBox.information(parent, title, text)
    QMessageBox.warning(parent, title, text)
    QMessageBox.critical(parent, title, text)
    QMessageBox.question(parent, title, text)  -> a StandardButton

`question` RETURNS which button was pressed, so you always compare it:

    if answer == QMessageBox.StandardButton.Yes:

`QFileDialog` is the Qt equivalent of tkinter's `filedialog`. It returns a
TUPLE `(path, selected_filter)`, and the path is an empty string on Cancel --
forgetting the tuple is the classic first mistake.

`closeEvent` is how a Qt window intercepts its own close button, the way
`protocol('WM_DELETE_WINDOW', ...)` did in tkinter.
'''

import sys

from PySide6.QtWidgets import (QApplication, QFileDialog, QLabel, QMessageBox,
                               QPushButton, QVBoxLayout, QWidget)


class DialogDemo(QWidget):
    '''One button per kind of dialog.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Dialogs')
        self.resize(420, 340)

        self.answer_label = QLabel('-')

        layout = QVBoxLayout()
        for text, slot in [('Information', self.show_information),
                           ('Warning', self.show_warning),
                           ('Critical', self.show_critical),
                           ('Question', self.ask_question),
                           ('Open a file...', self.open_file)]:
            button = QPushButton(text)
            button.clicked.connect(slot)
            layout.addWidget(button)
        layout.addWidget(self.answer_label)
        self.setLayout(layout)

    def show_information(self) -> None:
        QMessageBox.information(self, 'Kadoos', 'Everything went well.')

    def show_warning(self) -> None:
        QMessageBox.warning(self, 'Kadoos', 'Be careful with that.')

    def show_critical(self) -> None:
        QMessageBox.critical(self, 'Kadoos', 'Something went wrong!')

    def ask_question(self) -> None:
        answer = QMessageBox.question(self, 'Kadoos', 'Do you like Python?')
        # Always compare against the StandardButton values.
        liked = answer == QMessageBox.StandardButton.Yes
        self.answer_label.setText('You answered: ' + ('yes' if liked else 'no'))

    def open_file(self) -> None:
        # getOpenFileName returns (path, filter) -- never forget the tuple.
        path, _filter = QFileDialog.getOpenFileName(
            self, 'Open', '', 'Text files (*.txt);;All files (*)')
        if not path:                       # Cancel
            return
        self.answer_label.setText(f'You chose: {path}')

    def closeEvent(self, event) -> None:
        '''Qt calls this when the user clicks the X button.'''
        answer = QMessageBox.question(self, 'Exit', 'Really close the program?')
        if answer == QMessageBox.StandardButton.Yes:
            event.accept()                 # let the window close
        else:
            event.ignore()                 # keep it open


def main() -> None:
    app = QApplication(sys.argv)
    window = DialogDemo()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
