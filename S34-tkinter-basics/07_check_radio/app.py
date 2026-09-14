'''Checkbutton (several independent choices) and Radiobutton (one choice).

Both need a CONTROL VARIABLE - IntVar, StringVar, BooleanVar - which holds the
current value and is read with get().

Every radio button of a group shares the SAME variable; what tells them apart
is their `value`.
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Options')
    root.geometry('400x300')

    label_status = tk.Label(root, text='')
    label_color = tk.Label(root, text='')

    var_check = tk.IntVar()                    # 0 or 1
    var_radio = tk.StringVar(value='red')      # the selected value

    def show_selection() -> None:
        'Called every time one of the widgets changes.'
        if var_check.get():
            label_status.config(text='Enabled')
        else:
            label_status.config(text='Disabled')

        label_color.config(text='Selected colour: ' + var_radio.get())

    tk.Checkbutton(root, text='Enable', variable=var_check,
                   command=show_selection).pack(pady=(10, 5))

    for colour in ('red', 'blue', 'green'):
        tk.Radiobutton(root, text=colour, variable=var_radio, value=colour,
                       command=show_selection).pack(anchor='w', padx=140)

    label_status.pack(pady=(15, 0))
    label_color.pack()

    show_selection()          # show the initial state

    root.mainloop()


if __name__ == '__main__':
    main()
