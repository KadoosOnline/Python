'''`after()`: doing something later WITHOUT freezing the window.

This is the single most important rule of GUI programming:

    NEVER call time.sleep() -- and never run a long loop -- inside a callback.

While your function runs, the event loop (`mainloop`) is blocked: the window
stops redrawing, the buttons stop answering, and the operating system says the
program "is not responding".

The Tk answer is `widget.after(milliseconds, function)`: it asks the event loop
to call `function` later and returns IMMEDIATELY. A function that schedules
ITSELF again at the end is how you build a clock, a timer or an animation.

`after_cancel(job_id)` cancels a job that has not run yet -- always cancel
before you schedule a second one, otherwise you end up with two timers running
at the same time and a counter that jumps by two.

(Real background work -- a download, a long computation -- needs threads:
that is session 37.)
'''

import time
import tkinter as tk
from datetime import datetime


class ClockAndTimer:
    '''A live clock, a countdown, and the "frozen window" demonstration.'''

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title('after()')
        root.geometry('460x360')

        # The id of the pending countdown job, or None when it is stopped.
        self.countdown_job: str | None = None
        self.remaining = 0

        self.clock_label = tk.Label(root, font=('Arial', 24))
        self.clock_label.pack(pady=15)

        self.timer_label = tk.Label(root, text='00:10', font=('Arial', 32),
                                    fg='darkgreen')
        self.timer_label.pack(pady=5)

        buttons = tk.Frame(root)
        buttons.pack(pady=10)
        tk.Button(buttons, text='Start 10 s', width=10,
                  command=self.start_countdown).pack(side='left', padx=4)
        tk.Button(buttons, text='Stop', width=10,
                  command=self.stop_countdown).pack(side='left', padx=4)

        tk.Label(root, text='--- the wrong way ---').pack(pady=(20, 4))
        tk.Button(root, text='Freeze the window for 3 seconds',
                  command=self.freeze).pack()

        self.tick_clock()               # start the clock

    def tick_clock(self) -> None:
        '''Show the time, then ask to be called again in one second.'''
        self.clock_label.config(text=datetime.now().strftime('%H:%M:%S'))
        self.root.after(1000, self.tick_clock)

    def start_countdown(self) -> None:
        self.stop_countdown()           # never leave an old job running
        self.remaining = 10
        self.tick_countdown()

    def tick_countdown(self) -> None:
        minutes, seconds = divmod(self.remaining, 60)
        self.timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
        if self.remaining == 0:
            self.timer_label.config(fg='red')
            self.countdown_job = None
            return
        self.remaining -= 1
        self.timer_label.config(fg='darkgreen')
        # Keep the id so that Stop can cancel this job.
        self.countdown_job = self.root.after(1000, self.tick_countdown)

    def stop_countdown(self) -> None:
        if self.countdown_job is not None:
            self.root.after_cancel(self.countdown_job)
            self.countdown_job = None

    def freeze(self) -> None:
        '''What NOT to do: the clock above stops for three whole seconds.'''
        time.sleep(3)


def main() -> None:
    root = tk.Tk()
    ClockAndTimer(root)
    root.mainloop()


if __name__ == '__main__':
    main()
