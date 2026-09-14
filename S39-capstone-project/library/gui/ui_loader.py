'''Loading the Qt Designer files -- written once, used by every dialog.

The first version of this course repeated the same fifteen lines of
`QUiLoader` code at the top of nine files. It is one function.

`find(window, QLineEdit, 'editTitle')` looks a widget up and raises straight
away if the objectName does not match the `.ui` file, instead of returning
`None` that explodes in a callback ten minutes later.
'''

from typing import TypeVar

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget

from core.paths import ui_path


WidgetType = TypeVar('WidgetType', bound=QWidget)


def load_ui(file_name: str) -> QWidget:
    '''Load one of the files of `ui/` and return the widget it describes.'''
    path = ui_path(file_name)
    if not path.exists():
        raise FileNotFoundError(
            f'{path} is missing.\n'
            'When the program is frozen, the ui/ folder must be shipped with '
            'it:  pyinstaller --add-data "ui;ui" ...')

    widget = QUiLoader().load(str(path))
    if widget is None:
        raise RuntimeError(f'Qt could not read {path} (invalid XML?)')
    return widget


def find(parent: QWidget, widget_type: type[WidgetType],
         name: str) -> WidgetType:
    '''findChild that complains at once instead of returning None.'''
    widget = parent.findChild(widget_type, name)
    if widget is None:
        raise RuntimeError(f'No {widget_type.__name__} named {name!r} in the '
                           'ui file -- check the objectName in Qt Designer.')
    return widget
