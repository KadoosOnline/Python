'''grid() places the widgets in a table of rows and columns.

It is the right manager for a form. Never use pack() and grid() on widgets
that share the same parent: the program then freezes.
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Login form')
    root.geometry('400x300')

    # sticky='e' pushes the label to the East (the right) of its cell.
    tk.Label(root, text='Username:').grid(row=0, column=0,
                                          padx=10, pady=5, sticky='e')
    entry_user = tk.Entry(root, width=25)
    entry_user.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text='Password:').grid(row=1, column=0,
                                          padx=10, pady=5, sticky='e')
    # show='*' hides what is typed.
    entry_pass = tk.Entry(root, width=25, show='*')
    entry_pass.grid(row=1, column=1, padx=10, pady=5)

    label_result = tk.Label(root, text='')
    label_result.grid(row=3, column=0, columnspan=2)

    def login() -> None:
        username = entry_user.get().strip()
        password = entry_pass.get()

        if not username or not password:
            label_result.config(text='Both fields are required.', fg='red')
            return

        if username == 'admin' and password == '1234':
            label_result.config(text=f'Welcome, {username}!', fg='green')
        else:
            label_result.config(text='Wrong username or password.', fg='red')

    # columnspan=2 makes the button as wide as the two columns.
    tk.Button(root, text='Login', command=login).grid(row=2, column=0,
                                                      columnspan=2, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
