'''Qt Designer: draw the window, write only the behaviour.

Qt Designer is a program where you drag widgets onto a window with the mouse
and save the result as a `.ui` file -- which is plain XML, so you can open
`window.ui` in a text editor and read it.

Start it with:

    pyside6-designer                # comes with PySide6

There are TWO ways to use a `.ui` file from Python:

  A. Load it at RUN TIME with `QUiLoader` (this example).
     Nothing to regenerate when the design changes -- but the editor cannot
     help you: `findChild` names are just strings.

  B. COMPILE it once into a Python class (example 08):
         pyside6-uic window.ui -o ui_window.py
     Faster to start, and the auto-completion of your editor works.

Rules for the `.ui` file:

* Give every widget you touch from Python a clear objectName in Designer
  (`labelTitle`, `btnClose`, `editName`...). That name is what `findChild`
  looks for.
* Always put the widgets in a LAYOUT (right click on the form ->
  "Lay out" -> "Lay Out Vertically"). Without a layout the widgets keep the
  pixel positions you gave them and the window looks broken when it is resized
  or when the user has a different font size.
'''

import sys
from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget


def load_ui(name: str) -> QWidget:
    '''Load a .ui file that sits next to this script.'''
    # `with_name` keeps the folder of THIS file, so the program works no
    # matter which directory you run it from.
    path = Path(__file__).with_name(name)
    window = QUiLoader().load(str(path))
    if window is None:
        # A typo in the file name, or invalid XML.
        raise RuntimeError(f'Cannot load {path}')
    return window


def main() -> None:
    app = QApplication(sys.argv)
    window = load_ui('window.ui')

    # findChild(type, objectName) -> the widget, or None if the name is wrong.
    title = window.findChild(QLabel, 'labelTitle')
    button = window.findChild(QPushButton, 'btnClose')
    if title is None or button is None:
        raise RuntimeError('An objectName does not match window.ui')

    title.setText('Welcome to Kadoos Institute!')
    button.clicked.connect(window.close)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
