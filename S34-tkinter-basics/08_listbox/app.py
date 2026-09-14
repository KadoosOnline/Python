'''A Listbox shows a list the user can choose from.

    insert(tk.END, item)  -> add at the end
    curselection()        -> a TUPLE of the selected indexes (empty when none)
    get(index)            -> the text of one line
    delete(index)         -> remove a line
'''

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Listbox')
    root.geometry('400x350')

    listbox = tk.Listbox(root, height=6)
    for item in ['Tehran', 'Isfahan', 'Shiraz', 'Tabriz', 'Mashhad', 'Rasht']:
        listbox.insert(tk.END, item)
    listbox.pack(pady=10)

    label = tk.Label(root, text='')
    label.pack()

    def show_selected() -> None:
        selected = listbox.curselection()

        # curselection() gives an empty tuple when nothing is selected -
        # reading selected[0] without this test raises IndexError.
        if selected:
            label.config(text='Your choice: ' + listbox.get(selected[0]))
        else:
            label.config(text='Nothing is selected')

    def delete_selected() -> None:
        selected = listbox.curselection()
        if selected:
            listbox.delete(selected[0])

    tk.Button(root, text='Show the selection', command=show_selected).pack(pady=5)
    tk.Button(root, text='Delete the selection', command=delete_selected).pack()

    # A double click also shows the selection.
    listbox.bind('<Double-Button-1>', lambda event: show_selected())

    root.mainloop()


if __name__ == '__main__':
    main()
