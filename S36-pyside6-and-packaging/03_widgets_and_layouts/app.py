'''The widgets you will actually use, and the four layouts.

Widgets
    QLabel        text or a picture
    QLineEdit     one line of text          .text()
    QTextEdit     many lines                .toPlainText()
    QPushButton   a button
    QCheckBox     a tick box                .isChecked()
    QRadioButton  one choice out of several (group them in a QButtonGroup)
    QComboBox     a drop-down list          .currentText() / .currentIndex()
    QSpinBox      a whole number            .value()   <- already an int!
    QSlider       a slider                  .value()
    QListWidget   a list                    .currentItem()

Layouts
    QVBoxLayout   one under the other
    QHBoxLayout   one next to the other
    QGridLayout   rows and columns (like tkinter's grid)
    QFormLayout   "label: field" pairs -- the right tool for a form

`addStretch()` inserts empty space that grows, which is how you push widgets
to the top or to one side.

Notice `QSpinBox.value()`: unlike tkinter's `Spinbox.get()`, Qt gives you a
real `int`, and the widget itself refuses anything that is not a number.
'''

import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSpinBox, QVBoxLayout, QWidget)


PRICES = {'Introduction to Python': 4_500_000,
          'Advanced Python': 5_200_000,
          'Web with Flask': 3_800_000}


class RegistrationForm(QWidget):
    '''A course registration form built with QFormLayout.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Registration')
        self.resize(480, 320)

        self.name_edit = QLineEdit()
        self.course_box = QComboBox()
        self.course_box.addItems(PRICES)          # the keys of the dict

        self.sessions_box = QSpinBox()
        self.sessions_box.setRange(1, 20)
        self.sessions_box.setValue(20)

        self.student_box = QCheckBox('I am a student (20 % off)')

        form = QFormLayout()
        form.addRow('Full name:', self.name_edit)
        form.addRow('Course:', self.course_box)
        form.addRow('Sessions:', self.sessions_box)
        form.addRow('', self.student_box)

        self.result = QLabel('')
        self.result.setStyleSheet('font-size: 15px; font-weight: bold;')

        compute = QPushButton('Compute the price')
        clear = QPushButton('Clear')
        compute.clicked.connect(self.compute)
        clear.clicked.connect(self.clear_form)

        buttons = QHBoxLayout()
        buttons.addStretch()               # push the buttons to the right
        buttons.addWidget(clear)
        buttons.addWidget(compute)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(self.result)
        layout.addStretch()
        layout.addLayout(buttons)
        self.setLayout(layout)

    def compute(self) -> None:
        name = self.name_edit.text().strip()
        if not name:
            self.result.setText('Please type your name first.')
            return

        course = self.course_box.currentText()
        sessions = self.sessions_box.value()          # already an int
        price = PRICES[course] * sessions // 20
        if self.student_box.isChecked():
            price = int(price * 0.8)

        self.result.setText(f'{name}: {course}, {sessions} sessions '
                            f'-> {price:,} toman')

    def clear_form(self) -> None:
        self.name_edit.clear()
        self.course_box.setCurrentIndex(0)
        self.sessions_box.setValue(20)
        self.student_box.setChecked(False)
        self.result.clear()


def main() -> None:
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
