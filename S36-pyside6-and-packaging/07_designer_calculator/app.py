'''The calculator of Qt Designer -- rewritten.

THE ORIGINAL VERSION HAD FOUR PROBLEMS, and they are all worth showing:

1. `float(edit.text())` with nothing around it. An empty field or the word
   "abc" raised `ValueError`, the traceback went to a console the user of an
   .exe never sees, and the window simply did nothing.
2. Dividing by zero raised `ZeroDivisionError` for exactly the same reason.
3. `sum = num1 + num2` -- the name of the built-in function `sum`, shadowed.
4. Four functions of eight lines that differed by ONE character (`+ - * /`),
   each one looking the four widgets up again.

The fix for the last one is the `operator` module: `operator.add` IS the `+`
of Python as a normal function, so the operation becomes a value we can put in
a dictionary and pass around.

(Qt also offers `QDoubleValidator`, which stops the user from typing a letter
in the first place. Validating in the slot is still needed -- a validator can
be bypassed by pasting text, and an empty field is always allowed.)
'''

import operator
import sys
from pathlib import Path
from typing import Callable

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QWidget)


# The four operations, as data instead of as four copies of the same function.
OPERATIONS: dict[str, Callable[[float, float], float]] = {
    'btnAdd': operator.add,
    'btnSub': operator.sub,
    'btnMul': operator.mul,
    'btnDiv': operator.truediv,
}


class Calculator:
    '''A two-number calculator driven by calc.ui.'''

    def __init__(self) -> None:
        path = Path(__file__).with_name('calc.ui')
        self.window: QWidget = QUiLoader().load(str(path))
        if self.window is None:
            raise RuntimeError(f'Cannot load {path}')

        self.edit1 = self._find(QLineEdit, 'editNum1')
        self.edit2 = self._find(QLineEdit, 'editNum2')
        self.result = self._find(QLabel, 'lblResult')

        for name, function in OPERATIONS.items():
            button = self._find(QPushButton, name)
            # `f=function` freezes the current value; without it every button
            # would use the LAST operation of the loop.
            button.clicked.connect(lambda checked=False, f=function:
                                   self.calculate(f))

        self._find(QPushButton, 'btnClear').clicked.connect(self.clear)

    def _find(self, widget_type: type, name: str):
        widget = self.window.findChild(widget_type, name)
        if widget is None:
            raise RuntimeError(f'calc.ui has no {widget_type.__name__} '
                               f'called {name!r}')
        return widget

    def read_numbers(self) -> tuple[float, float] | None:
        '''Read both fields, or show why they cannot be read.'''
        try:
            first = float(self.edit1.text().strip())
            second = float(self.edit2.text().strip())
        except ValueError:
            # Empty field, a letter, two dots... one message for all of them.
            self.show_error('Please type two numbers.')
            return None
        return first, second

    def calculate(self, function: Callable[[float, float], float]) -> None:
        numbers = self.read_numbers()
        if numbers is None:
            return
        try:
            answer = function(*numbers)
        except ZeroDivisionError:
            self.show_error('Cannot divide by zero.')
            return
        self.result.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.result.setText(f'{answer:.2f}')

    def show_error(self, message: str) -> None:
        self.result.setStyleSheet('font-size: 13px; color: red;')
        self.result.setText(message)

    def clear(self) -> None:
        self.edit1.clear()
        self.edit2.clear()
        self.result.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.result.setText('0')
        self.edit1.setFocus()

    def show(self) -> None:
        self.window.show()


def main() -> None:
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
