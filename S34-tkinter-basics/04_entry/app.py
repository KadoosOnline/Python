'''An Entry is a one-line text field.

    entry.get()              -> what the user typed (always a str)
    entry.delete(0, tk.END)  -> empty it
    entry.insert(0, 'text')  -> write into it
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Text input')
    root.geometry('400x300')

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)
    entry.focus()                 # the cursor starts in this field

    label = tk.Label(root, text='')
    label.pack(pady=10)

    def show_text() -> None:
        user_input = entry.get().strip()

        if not user_input:
            label.config(text='Please type something first.')
            return

        label.config(text='You wrote: ' + user_input)

    tk.Button(root, text='Show', command=show_text).pack()
    tk.Button(root, text='Clear',
              command=lambda: entry.delete(0, tk.END)).pack(pady=5)

    # bind() connects a keyboard or mouse event to a function.
    # '<Return>' is the Enter key.
    entry.bind('<Return>', lambda event: show_text())

    root.mainloop()


if __name__ == '__main__':
    main()
