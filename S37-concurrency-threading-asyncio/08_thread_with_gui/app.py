'''Threads and a graphical interface -- the real reason you will need threads.

Session 35 taught the rule: a long job inside a callback freezes the window.
`after()` solved it for a TIMER, but not for real work -- a download or a big
computation cannot be cut into 100 ms slices.

The answer is a worker thread. And with it comes THE golden rule:

    *** never touch a widget from another thread ***

Tkinter (like Qt, like almost every GUI toolkit) is not thread-safe. Calling
`label.config(...)` from a worker gives you random crashes, frozen windows,
or nothing at all -- and only on some machines.

The safe pattern, used below:

    worker thread  --put-->  queue.Queue  --get-->  main thread (after())

The worker only puts messages in a queue. The main thread polls that queue
every 100 ms with `after()` and is the only one that touches the widgets.

The Qt version of the same idea: the worker emits a SIGNAL, and Qt delivers it
to the GUI thread for you.
'''

import queue
import threading
import time
import tkinter as tk
from tkinter import ttk


class DownloadWindow:
    '''A fake download that keeps the window alive while it runs.'''

    POLL_MS = 100          # how often the GUI looks into the queue

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title('Threads and tkinter')
        root.geometry('460x300')

        # The only channel between the worker and the interface.
        self.messages: queue.Queue = queue.Queue()
        self.worker: threading.Thread | None = None
        self.stop_event = threading.Event()

        self.status = tk.Label(root, text='ready', font=('Arial', 12))
        self.status.pack(pady=15)

        self.bar = ttk.Progressbar(root, length=320, maximum=100)
        self.bar.pack(pady=5)

        self.start_button = tk.Button(root, text='Start the download',
                                      width=22, command=self.start)
        self.start_button.pack(pady=6)

        self.cancel_button = tk.Button(root, text='Cancel', width=22,
                                       state='disabled', command=self.cancel)
        self.cancel_button.pack()

        tk.Label(root, text='(the clock keeps ticking: the window is alive)',
                 fg='gray').pack(pady=10)
        self.clock = tk.Label(root, font=('Arial', 16))
        self.clock.pack()
        self.tick_clock()

        # Read the queue for ever, every POLL_MS milliseconds.
        self.root.after(self.POLL_MS, self.poll_queue)
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

    # -- the worker thread -------------------------------------------------
    def download(self) -> None:
        '''Runs in a THREAD. It must not touch a single widget.'''
        for percent in range(0, 101, 5):
            if self.stop_event.is_set():
                self.messages.put(('done', 'cancelled'))
                return
            time.sleep(0.2)                     # the waiting work
            self.messages.put(('progress', percent))
        self.messages.put(('done', 'finished'))

    # -- the GUI thread ----------------------------------------------------
    def poll_queue(self) -> None:
        '''Runs in the MAIN thread: here, and only here, we touch widgets.'''
        try:
            while True:
                # get_nowait raises Empty instead of blocking the interface.
                kind, value = self.messages.get_nowait()
                if kind == 'progress':
                    self.bar['value'] = value
                    self.status.config(text=f'downloading... {value} %')
                elif kind == 'done':
                    self.status.config(text=str(value))
                    self.start_button.config(state='normal')
                    self.cancel_button.config(state='disabled')
        except queue.Empty:
            pass
        # Ask to be called again. This line must never be skipped.
        self.root.after(self.POLL_MS, self.poll_queue)

    def start(self) -> None:
        if self.worker is not None and self.worker.is_alive():
            return
        self.stop_event.clear()
        self.bar['value'] = 0
        self.start_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        # daemon=True so a forgotten worker cannot keep the program alive.
        self.worker = threading.Thread(target=self.download, daemon=True)
        self.worker.start()

    def cancel(self) -> None:
        '''You cannot kill a thread; you ASK it to stop.'''
        self.stop_event.set()
        self.status.config(text='cancelling...')

    def tick_clock(self) -> None:
        self.clock.config(text=time.strftime('%H:%M:%S'))
        self.root.after(1000, self.tick_clock)

    def on_close(self) -> None:
        self.stop_event.set()
        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    DownloadWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
