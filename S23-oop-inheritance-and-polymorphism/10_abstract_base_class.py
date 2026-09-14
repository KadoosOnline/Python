# An abstract base class defines WHAT the children must provide,
# without providing it itself. It cannot be instantiated.
from abc import ABC, abstractmethod


class Notifier(ABC):
    def __init__(self, target: str) -> None:
        self.target = target

    @abstractmethod
    def send(self, message: str) -> None:
        'Every real notifier has to implement this.'

    def send_all(self, messages: list[str]) -> None:
        'A normal method that the children inherit for free.'
        for message in messages:
            self.send(message)


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'Email to {self.target}: {message}')


class SmsNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'SMS to {self.target}: {message}')


if __name__ == '__main__':
    notifiers: list[Notifier] = [
        EmailNotifier('ali@kadoosedu.ir'),
        SmsNotifier('09121234567'),
    ]

    for notifier in notifiers:
        notifier.send_all(['Welcome!', 'Your class starts at 17:00'])

    # Creating the abstract class itself is refused:
    try:
        Notifier('nobody')
    except TypeError as e:
        print('Refused:', e)

    # A child that forgets send() is refused as well:
    class BrokenNotifier(Notifier):
        pass

    try:
        BrokenNotifier('x')
    except TypeError as e:
        print('Refused:', e)
