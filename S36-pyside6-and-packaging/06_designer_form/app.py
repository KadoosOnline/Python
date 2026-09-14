'''The same `.ui` trick, but organised as a class.

Looking every widget up with `findChild` in the middle of a callback (which is
what the first version of this course did) means:

* the same three lines are repeated in every function,
* a typo in an objectName is only discovered when the user clicks,
* and `findChild` can return `None`, which then explodes far from the cause.

So: look each widget up ONCE, in `__init__`, store it on `self`, and check the
result immediately. After that the rest of the class is ordinary Python.

`QLineEdit.returnPressed` fires when the user presses Enter in the field --
connect it to the same slot as the button and the form feels much better.
'''

import sys
from pathlib import Path

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                               QPushButton, QWidget)


class GreetingWindow:
    '''Wraps the window loaded from window.ui.'''

    def __init__(self) -> None:
        path = Path(__file__).with_name('window.ui')
        self.window: QWidget = QUiLoader().load(str(path))
        if self.window is None:
            raise RuntimeError(f'Cannot load {path}')

        self.name_edit = self._find(QLineEdit, 'editName')
        self.city_box = self._find(QComboBox, 'comboCity')
        self.hello_label = self._find(QLabel, 'labelHello')
        self.hello_button = self._find(QPushButton, 'btnHello')

        self.hello_button.clicked.connect(self.say_hello)
        self.name_edit.returnPressed.connect(self.say_hello)

    def _find(self, widget_type: type, name: str):
        '''findChild, but it complains at start-up instead of at click time.'''
        widget = self.window.findChild(widget_type, name)
        if widget is None:
            raise RuntimeError(f'window.ui has no {widget_type.__name__} '
                               f'called {name!r}')
        return widget

    def say_hello(self) -> None:
        name = self.name_edit.text().strip()
        if not name:
            self.hello_label.setText('Please type a name.')
            return
        city = self.city_box.currentText()
        self.hello_label.setText(f'Hello {name} from {city}!')

    def show(self) -> None:
        self.window.show()


def main() -> None:
    app = QApplication(sys.argv)
    window = GreetingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
