'''Signals and slots -- the Qt way of reacting to the user.

In tkinter we wrote `command=my_function`. In Qt every widget EMITS signals:

    button.clicked          -- the button was pressed
    line_edit.textChanged   -- the text changed (sends the new text)
    slider.valueChanged     -- the value changed (sends the new value)

and you CONNECT a signal to a function (Qt calls it a "slot"):

    button.clicked.connect(self.on_click)      # no () -- pass the function

One signal can be connected to several slots, and one slot can serve several
signals. A signal that carries a value passes it to the slot as an argument:
that is why `on_text_changed` takes a `text` parameter.

Careful with `clicked`: it actually sends a `checked` boolean, so a slot
connected to it may receive `False` as an argument. Either accept it, or use a
`lambda` that ignores it -- as we do for the two counter buttons.
'''

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QVBoxLayout, QWidget)


class CounterWindow(QWidget):
    '''A counter and a live greeting.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Signals and slots')
        self.resize(440, 260)

        self.count = 0

        self.count_label = QLabel('0')
        self.count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.count_label.setStyleSheet('font-size: 28px;')

        plus = QPushButton('+')
        minus = QPushButton('-')
        reset = QPushButton('Reset')

        # `lambda:` swallows the `checked` argument that clicked sends.
        plus.clicked.connect(lambda: self.change(+1))
        minus.clicked.connect(lambda: self.change(-1))
        reset.clicked.connect(self.reset)

        buttons = QHBoxLayout()
        buttons.addWidget(minus)
        buttons.addWidget(reset)
        buttons.addWidget(plus)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('type your name...')
        self.greeting = QLabel('Hello!')
        # textChanged sends the new text to the slot.
        self.name_edit.textChanged.connect(self.on_name_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.count_label)
        layout.addLayout(buttons)          # a layout can hold another layout
        layout.addSpacing(20)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.greeting)
        self.setLayout(layout)

    def change(self, step: int) -> None:
        self.count += step
        self.count_label.setText(str(self.count))

    def reset(self) -> None:
        self.count = 0
        self.count_label.setText('0')

    def on_name_changed(self, text: str) -> None:
        name = text.strip()
        self.greeting.setText(f'Hello {name}!' if name else 'Hello!')


def main() -> None:
    app = QApplication(sys.argv)
    window = CounterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
