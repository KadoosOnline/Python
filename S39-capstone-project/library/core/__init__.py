'''The core of the application: paths, database, models, services.

Nothing in this package imports PySide6. That is the whole point: the rules of
the library ("a book that is out cannot be lent again") live here, and the
windows of `gui/` only display them. Swap the Qt interface for a Flask site
(session 38) and this package does not change by one line.
'''
