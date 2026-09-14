'''Backing up a database.

conn.backup() copies a database safely, even while it is being used -
much better than copying the file with the operating system.
'''

import sqlite3


def main() -> None:
    source = sqlite3.connect('database.db')
    backup = sqlite3.connect('backup.db')

    try:
        source.backup(backup)
        print('backup.db was written.')
    finally:
        # The connections are closed even if the backup failed.
        backup.close()
        source.close()


if __name__ == '__main__':
    main()
