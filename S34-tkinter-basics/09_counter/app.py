'''Control variables: the clean way to keep a widget and a value in agreement.

With `textvariable=`, the label updates ITSELF whenever the variable changes:
we never call label.config() again.
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Counter')
    root.geometry('400x300')

    counter_var = tk.IntVar(value=0)

    def increment() -> None:
        counter_var.set(counter_var.get() + 1)

    def decrement() -> None:
        counter_var.set(counter_var.get() - 1)

    def reset() -> None:
        counter_var.set(0)

    tk.Label(root, textvariable=counter_var,
             font=('Arial', 24)).pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame, text='+', command=increment,
              width=5).pack(side='left', padx=5)
    tk.Button(button_frame, text='-', command=decrement,
              width=5).pack(side='left', padx=5)
    tk.Button(button_frame, text='Reset', command=reset,
              width=6).pack(side='left', padx=5)

    root.mainloop()


if __name__ == '__main__':
    main()
