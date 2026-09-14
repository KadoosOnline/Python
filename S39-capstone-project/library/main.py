'''Kadoos library -- the capstone project.

Run it with:

    python main.py

The first start creates `data/library.db` and fills it with a few books and
members so there is something to look at.

The shape of the project:

    main.py            starts everything -- and nothing else
    core/paths.py      where the files are (works frozen too)
    core/models.py     the tables
    core/database.py   the engine, the session, the transaction helper
    core/services.py   the RULES of the library
    gui/ui_loader.py   loading the Qt Designer files
    gui/dialogs.py     the three forms
    gui/main_window.py the main window
    ui/*.ui            what Qt Designer produced

Read it from the bottom up: `core/` knows nothing about windows, `gui/` knows
nothing about SQL, and `main.py` knows only how to start.
'''

import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from core.database import init_database, session_scope
from core.services import add_sample_data
from gui.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)

    try:
        init_database()
        with session_scope() as session:
            add_sample_data(session)
    except Exception as error:
        # A --windowed build has no console, so a start-up failure must be
        # shown in a box or nobody will ever see it (session 36).
        QMessageBox.critical(None, 'The database could not be opened',
                             f'{type(error).__name__}: {error}')
        return 1

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == '__main__':
    sys.exit(main())
