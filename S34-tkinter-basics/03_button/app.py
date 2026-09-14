'''A Button runs a function when it is clicked.

Note how the widgets are created inside main() and the callback is a NESTED
function: that way it sees `label` without needing `global`.
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Button and label')
    root.geometry('400x300')

    label = tk.Label(root, text='I am waiting for a click')
    label.pack(pady=20)

    def change_text() -> None:
        'This function is called by the button.'
        print('Clicked!')
        # config() changes an option of an existing widget.
        label.config(text='The button was clicked')

    # command=change_text  passes the FUNCTION ITSELF.
    # command=change_text()  would CALL it immediately and pass its result -
    # that is the classic beginner mistake.
    button = tk.Button(root, text='Click me', command=change_text)
    button.pack()

    # A counter, to show that the callback keeps its state between clicks.
    clicks = {'count': 0}

    def count_click() -> None:
        clicks['count'] += 1
        counter_label.config(text=f'Clicks: {clicks["count"]}')

    counter_label = tk.Label(root, text='Clicks: 0')
    counter_label.pack(pady=(20, 0))
    tk.Button(root, text='Count', command=count_click).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
