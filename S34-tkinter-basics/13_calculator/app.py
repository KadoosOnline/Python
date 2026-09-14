'''A complete calculator.

Two things worth noticing:

1. The buttons are built in a LOOP from a list. Writing sixteen almost
   identical lines would be a waste.

2. `command=lambda t=text: press(t)` - the `t=text` is essential.
   Without it, every lambda would share the same variable and all the buttons
   would type the LAST character of the loop. This is the classic
   "late binding" trap.

3. The expression is evaluated with eval(), which is dangerous in general:
   it runs ANY Python code. Here we first check that the text contains only
   digits and operators, so nothing else can be executed.
'''

import tkinter as tk

ALLOWED_CHARACTERS = set('0123456789+-*/(). ')

BUTTONS = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


def main() -> None:
    root = tk.Tk()
    root.title('Calculator')
    root.geometry('300x400')

    display = tk.Entry(root, font=('Arial', 18), justify='right')
    display.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=5)

    def press(key: str) -> None:
        'Add one character at the end of the display.'
        display.insert(tk.END, str(key))

    def clear() -> None:
        display.delete(0, tk.END)

    def calculate() -> None:
        expression = display.get()

        # Refuse anything that is not a number or an operator.
        if not expression or not set(expression) <= ALLOWED_CHARACTERS:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')
            return

        try:
            result = eval(expression)
        except (SyntaxError, ZeroDivisionError, ValueError):
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')
            return

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

    for text, row, column in BUTTONS:
        if text == '=':
            button = tk.Button(root, text=text, width=5, height=2,
                               command=calculate)
        else:
            # t=text captures the CURRENT value of text.
            button = tk.Button(root, text=text, width=5, height=2,
                               command=lambda t=text: press(t))
        button.grid(row=row, column=column, padx=2, pady=2)

    tk.Button(root, text='C', width=5, height=2, command=clear).grid(
        row=5, column=0, columnspan=4, sticky='we', padx=5, pady=2)

    # The columns share the extra space when the window is resized.
    for column in range(4):
        root.grid_columnconfigure(column, weight=1)

    root.mainloop()


if __name__ == '__main__':
    main()
