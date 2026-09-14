'''Opening a file from a GUI: `filedialog` + a scrollable `Text` widget.

Three new ideas here:

1. `filedialog.askopenfilename()` shows the operating-system "Open" dialog and
   returns the chosen path as a string, or an EMPTY string if the user pressed
   Cancel -- so we must always check the result before using it.
2. The `Text` widget holds many lines. Its positions are strings that look like
   'line.column', and lines are counted from 1: the very beginning is '1.0'.
3. A `Scrollbar` and the widget it scrolls have to be connected in BOTH
   directions (widget -> scrollbar with `yscrollcommand`,
   scrollbar -> widget with `command`).

Everything lives inside a class so that the callback can reach the widgets
without a single `global`.
'''

import tkinter as tk
from tkinter import filedialog, messagebox


class FileViewer:
    '''A tiny read-only viewer for text files.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title('File viewer')
        self.root.geometry('600x500')

        tk.Button(root, text='Open a file...',
                  command=self.open_file).pack(pady=5)

        # A frame keeps the text area and its scrollbar side by side.
        frame = tk.Frame(root)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')

        # wrap='none' = do not break long lines; that is what a code viewer wants.
        self.text_area = tk.Text(frame, wrap='none',
                                 yscrollcommand=scrollbar.set)
        self.text_area.pack(side='left', fill='both', expand=True)

        # Second half of the connection: moving the bar scrolls the text.
        scrollbar.config(command=self.text_area.yview)

    def open_file(self) -> None:
        '''Ask for a file and show its content in the text area.'''
        # Each filter is a (label, pattern) pair.
        file_path = filedialog.askopenfilename(
            title='Open',
            filetypes=[('Python files', '*.py'),
                       ('Text files', '*.txt'),
                       ('All files', '*.*')],
        )

        # Cancel gives back an empty string.
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except OSError as error:
            # A missing file, a folder, or no permission: never crash the GUI.
            messagebox.showerror('Cannot open the file', str(error))
            return
        except UnicodeDecodeError:
            messagebox.showerror('Cannot open the file',
                                 'This file is not UTF-8 text (a picture?).')
            return

        # '1.0' is the start, tk.END is the end: clear, then insert.
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert('1.0', content)
        self.root.title(f'File viewer - {file_path}')


def main() -> None:
    root = tk.Tk()
    FileViewer(root)
    root.mainloop()


if __name__ == '__main__':
    main()
