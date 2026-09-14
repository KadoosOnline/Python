'''The second way to use Qt Designer: COMPILE the .ui into Python.

    pyside6-uic window.ui -o ui_window.py       (PyQt6: pyuic6)

The command turns the XML into `ui_window.py`, which holds a plain Python
class `Ui_Form` with one method, `setupUi(self, form)`, that builds every
widget in code. Look inside it -- there is no magic, it is exactly the kind of
code we wrote by hand in examples 01-04.

Then your window inherits from BOTH the Qt widget and the generated class:

    class TodoWindow(QWidget, Ui_Form):
        def __init__(self):
            super().__init__()
            self.setupUi(self)      # now self.editTask, self.btnAdd... exist

Compare with `QUiLoader` (examples 05-07):

| QUiLoader (run time)              | pyside6-uic (compiled)                |
|-----------------------------------|---------------------------------------|
| nothing to regenerate             | re-run uic after every design change  |
| widgets found by name at run time | widgets are real attributes           |
| no auto-completion, typos at run  | the editor completes and checks them  |
| the .ui must ship with the app    | only .py files ship (easier to freeze)|

For PyInstaller (the next examples) the compiled way is clearly easier: there
is no data file to carry around.

NEVER edit `ui_window.py` by hand -- the next `pyside6-uic` run overwrites it.
Your own code goes in this file.
'''

import sys

from PySide6.QtWidgets import QApplication, QWidget

from ui_window import Ui_Form


class TodoWindow(QWidget, Ui_Form):
    '''A to-do list. The widgets come from the generated Ui_Form.'''

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)          # builds every widget on `self`

        self.btnAdd.clicked.connect(self.add_task)
        self.editTask.returnPressed.connect(self.add_task)
        self.btnRemove.clicked.connect(self.remove_task)
        self.btnClear.clicked.connect(self.clear_tasks)

        self.update_count()

    def add_task(self) -> None:
        text = self.editTask.text().strip()
        if not text:
            return
        self.listTasks.addItem(text)
        self.editTask.clear()
        self.update_count()

    def remove_task(self) -> None:
        row = self.listTasks.currentRow()    # -1 when nothing is selected
        if row < 0:
            return
        # takeItem removes the row and gives the item back; we drop it.
        self.listTasks.takeItem(row)
        self.update_count()

    def clear_tasks(self) -> None:
        self.listTasks.clear()
        self.update_count()

    def update_count(self) -> None:
        count = self.listTasks.count()
        self.labelCount.setText(f'{count} task{"s" if count != 1 else ""}')


def main() -> None:
    app = QApplication(sys.argv)
    window = TodoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
