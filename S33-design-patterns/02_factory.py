'''FACTORY - creational pattern.

Problem:  the class to build is only known at run time (from a setting, from
          the answer of a user, from a configuration file).
Solution: one place - the factory - decides which class to instantiate, and the
          rest of the program only knows the common interface.
'''

from abc import ABC, abstractmethod


class Notifier(ABC):
    'The common interface. Every notifier can send a message.'

    @abstractmethod
    def send(self, message: str) -> None:
        ...


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'Sending email: {message}')


class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'Sending SMS: {message}')


class BotNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'Sending bot message: {message}')


class NotifierFactory:
    'The only place in the program that knows the concrete classes.'

    # A dictionary is cleaner than a chain of elif: adding a channel is
    # one line, and no existing code has to be touched.
    _channels = {
        'email': EmailNotifier,
        'sms': SMSNotifier,
        'bot': BotNotifier,
    }

    @staticmethod
    def create_notifier(channel: str) -> Notifier:
        'Return the notifier matching the given channel name.'
        notifier_class = NotifierFactory._channels.get(channel)

        if notifier_class is None:
            raise ValueError(f'Unknown channel: {channel!r}')

        return notifier_class()


if __name__ == '__main__':
    notifier = NotifierFactory.create_notifier('email')
    notifier.send('Welcome to Kadoos!')

    # The rest of the program never mentions EmailNotifier or SMSNotifier.
    for channel in ('sms', 'bot'):
        NotifierFactory.create_notifier(channel).send('Your class starts soon')

    try:
        NotifierFactory.create_notifier('pigeon')
    except ValueError as e:
        print('Refused:', e)
