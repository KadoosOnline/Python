'''A small notepad: open, save, save as, and "are you sure?" on exit.

New ideas:

* `filedialog.asksaveasfilename()` asks WHERE to save and already warns the
  user when the file exists.
* `text.edit_modified()` tells us whether the content changed since the last
  time we reset the flag -- that is how a real editor knows when to ask
  "Do you want to save your changes?".
* `root.protocol('WM_DELETE_WINDOW', func)` runs OUR function when the user
  clicks the window's X button, so we can stop the program from closing.
'''

import tkinter as tk
from tkinter import filedialog, messagebox


class Notepad:
    '''A minimal text editor.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.geometry('700x500')

        # The file we are editing; None means "never saved yet".
        self.current_path: str | None = None

        self.text = tk.Text(root, wrap='word', undo=True)
        self.text.pack(fill='both', expand=True)

        self._build_menu()
        self._update_title()

        # Intercept the window's close button.
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

    def _build_menu(self) -> None:
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='New', command=self.new_file)
        file_menu.add_command(label='Open...', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save as...', command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.on_close)
        menubar.add_cascade(label='File', menu=file_menu)
        self.root.config(menu=menubar)

    def _update_title(self) -> None:
        name = self.current_path if self.current_path else 'untitled'
        self.root.title(f'Notepad - {name}')

    def _is_modified(self) -> bool:
        '''True when the text changed since the last save.'''
        return bool(self.text.edit_modified())

    def _mark_saved(self) -> None:
        '''Tell Tk "the current content is the saved content".'''
        self.text.edit_modified(False)

    def _confirm_discard(self) -> bool:
        '''Ask before losing unsaved work. True = it is safe to continue.'''
        if not self._is_modified():
            return True
        answer = messagebox.askyesnocancel(
            'Unsaved changes',
            'Save the changes before continuing?')
        if answer is None:          # Cancel
            return False
        if answer:                  # Yes -> save first
            return self.save_file()
        return True                 # No -> throw the changes away

    def new_file(self) -> None:
        if not self._confirm_discard():
            return
        self.text.delete('1.0', tk.END)
        self.current_path = None
        self._mark_saved()
        self._update_title()

    def open_file(self) -> None:
        if not self._confirm_discard():
            return
        path = filedialog.askopenfilename(
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not path:
            return
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
        except (OSError, UnicodeDecodeError) as error:
            messagebox.showerror('Cannot open the file', str(error))
            return
        self.text.delete('1.0', tk.END)
        self.text.insert('1.0', content)
        self.current_path = path
        self._mark_saved()
        self._update_title()

    def save_file(self) -> bool:
        '''Save to the known path, or ask for one. True when it worked.'''
        if self.current_path is None:
            return self.save_file_as()
        return self._write_to(self.current_path)

    def save_file_as(self) -> bool:
        path = filedialog.asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not path:
            return False
        if self._write_to(path):
            self.current_path = path
            self._update_title()
            return True
        return False

    def _write_to(self, path: str) -> bool:
        # 'end-1c' = everything except the newline Tk always keeps at the end.
        content = self.text.get('1.0', 'end-1c')
        try:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
        except OSError as error:
            messagebox.showerror('Cannot save the file', str(error))
            return False
        self._mark_saved()
        return True

    def on_close(self) -> None:
        if self._confirm_discard():
            self.root.destroy()


def main() -> None:
    root = tk.Tk()
    Notepad(root)
    root.mainloop()


if __name__ == '__main__':
    main()
