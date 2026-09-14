'''`Spinbox`: choose a number with the little up/down arrows.

`spinbox.get()` returns a STRING, and the user can also type in the box --
including something that is not a number at all. So we validate before
converting, exactly as we do with `input()`.
'''

import tkinter as tk


class SpinboxDemo:
    '''Pick a quantity and compute a price.'''

    PRICE = 25_000     # price of one item, in toman

    def __init__(self, root: tk.Tk) -> None:
        root.title('Order')
        root.geometry('420x300')

        tk.Label(root, text='How many items?').pack(pady=10)

        self.spinbox = tk.Spinbox(root, from_=1, to=20, width=5)
        self.spinbox.pack()

        tk.Button(root, text='Compute the total',
                  command=self.show_total).pack(pady=10)

        self.result = tk.Label(root, text='')
        self.result.pack(pady=10)

    def show_total(self) -> None:
        raw = self.spinbox.get()
        # The user may have typed anything inside the box.
        if not raw.isdigit():
            self.result.config(text='Please choose a whole number.', fg='red')
            return
        count = int(raw)
        total = count * self.PRICE
        self.result.config(text=f'{count} x {self.PRICE:,} = {total:,} toman',
                           fg='black')


def main() -> None:
    root = tk.Tk()
    SpinboxDemo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
