'''A first third-party package: the Dilami (Gilaki) calendar.

Before running:
    python -m venv .venv
    (activate it)
    pip install -r requirements.txt
'''

from datetime import datetime

# A package that is not installed raises ModuleNotFoundError, so we give a
# clear message instead of a traceback.
try:
    from dilami_calendar import DilamiDatetime
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')


def main() -> None:
    print('The Dilami date of today:')
    print(DilamiDatetime.now())

    print()

    print('Converting a Gregorian date to Dilami:')
    gregorian_datetime = datetime(2026, 7, 19)
    dilami_datetime = DilamiDatetime(gregorian_datetime)

    print(f'    Year:  {dilami_datetime.year}')
    print(f'    Month: {dilami_datetime.month}')
    print(f'    Day:   {dilami_datetime.day}')


if __name__ == '__main__':
    main()
