'''The smallest possible Qt program.

Qt is a big C++ toolkit for desktop applications. `PySide6` is the OFFICIAL
Python binding, made by the Qt company itself. (`PyQt6` is a different binding
of the same library, by another company: almost the same code, a different
licence. Everything in this session works in PyQt6 by changing the import
lines and `.exec()` -- see the README.)

Install it once with:

    pip install PySide6

Every Qt program has the same four steps:

    1. app = QApplication(sys.argv)   -- exactly one per program
    2. build the widgets
    3. window.show()                  -- widgets are hidden until you say so
    4. app.exec()                     -- the event loop, like tkinter mainloop

`app.exec()` returns when the last window is closed; we hand its value to
`sys.exit()` so the operating system knows how the program ended.
'''

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class HelloWindow(QWidget):
    '''In Qt you make your own window by inheriting from a widget class.'''

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Kadoos - first Qt window')
        self.resize(420, 220)

        title = QLabel('Welcome to Kadoos Institute!')
        # A stylesheet: Qt understands a subset of CSS.
        title.setStyleSheet('font-size: 20px; font-weight: bold;')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel('This window is built with PySide6.')
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # A layout places the widgets for you and follows the window when it
        # is resized. Never position widgets by hand with move()/setGeometry().
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        self.setLayout(layout)


def main() -> None:
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
