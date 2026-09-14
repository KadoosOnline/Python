'''ADAPTER - structural pattern.

Problem:  an existing class does the right job but has the wrong method names,
          and we cannot (or must not) change it: it is a library, or old code
          used everywhere else.
Solution: a small class that wraps it and offers the interface we expect.

Real-life picture: a power plug adapter. It changes nothing electrically, it
only makes the two shapes fit.
'''


class LegacyPrinter:
    'The old class. We are not allowed to modify it.'

    def old_print(self, text: str) -> None:
        print(f'Legacy printer: {text}')


class PrinterInterface:
    'What the new system expects from a printer.'

    def print_message(self, text: str) -> None:
        raise NotImplementedError


class ModernPrinter(PrinterInterface):
    'A class written for the new interface.'

    def print_message(self, text: str) -> None:
        print(f'Modern printer: {text}')


class PrinterAdapter(PrinterInterface):
    'Makes a LegacyPrinter usable wherever a PrinterInterface is expected.'

    def __init__(self, legacy_printer: LegacyPrinter) -> None:
        self.legacy_printer = legacy_printer

    def print_message(self, text: str) -> None:
        # The only job of the adapter: translate the call.
        self.legacy_printer.old_print(text)


def print_report(printer: PrinterInterface) -> None:
    'This function only knows the new interface.'
    printer.print_message('Hello from the new system')


if __name__ == '__main__':
    print_report(ModernPrinter())

    legacy = LegacyPrinter()
    print_report(PrinterAdapter(legacy))    # the old class fits in
