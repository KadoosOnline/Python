'''Widget states: `normal`, `disabled`, `readonly`.

A greyed-out button that the user cannot press is much friendlier than a
button that opens an error message. The rule: disable what makes no sense
right now, and re-enable it as soon as it does.

* `widget.config(state='disabled')` -- greyed out, ignores the mouse
* `state='readonly'` (Entry, Combobox) -- can be read and copied, not changed
* A `Text` widget must be put back to 'normal' before you can insert into it.
'''

import tkinter as tk


class TermsForm:
    '''The classic "I accept the terms" form.'''

    def __init__(self, root: tk.Tk) -> None:
        root.title('Registration')
        root.geometry('460x320')

        tk.Label(root, text='E-mail:').pack(pady=(20, 2))
        self.email = tk.Entry(root, width=32)
        self.email.pack()

        # IntVar holds 0 or 1 for a Checkbutton.
        self.accepted = tk.IntVar(value=0)
        tk.Checkbutton(root, text='I accept the terms',
                       variable=self.accepted,
                       command=self.update_state).pack(pady=15)

        self.submit = tk.Button(root, text='Register',
                                width=15, command=self.register)
        self.submit.pack()

        self.log = tk.Text(root, height=5, width=45, state='disabled')
        self.log.pack(pady=15)

        self.update_state()     # start in the right state

    def update_state(self) -> None:
        '''The button is usable only while the box is ticked.'''
        self.submit.config(state='normal' if self.accepted.get() else 'disabled')

    def register(self) -> None:
        address = self.email.get().strip()
        message = (f'Registered: {address}' if '@' in address
                   else 'That does not look like an e-mail address.')
        self.write_log(message)

    def write_log(self, message: str) -> None:
        '''A read-only Text has to be unlocked before writing.'''
        self.log.config(state='normal')
        self.log.insert(tk.END, message + '\n')
        self.log.see(tk.END)            # scroll down to the new line
        self.log.config(state='disabled')


def main() -> None:
    root = tk.Tk()
    TermsForm(root)
    root.mainloop()


if __name__ == '__main__':
    main()
