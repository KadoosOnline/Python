'''OBSERVER - behavioural pattern.

Problem:  when something changes, several other objects have to react - and the
          object that changes must not have to know them.
Solution: the "subject" keeps a list of subscribers and notifies them.

You already met it without knowing: the GUI buttons of sessions 34-36
(`command=my_function`) are exactly this pattern.
'''


class NewsPublisher:
    'The subject: it holds the state and notifies the subscribers.'

    def __init__(self) -> None:
        self.subscribers: list = []
        self.latest_news: str | None = None

    def subscribe(self, subscriber) -> None:
        'Add a subscriber (only once).'
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber) -> None:
        'Remove a subscriber, quietly when it is not there.'
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify(self) -> None:
        'Tell every subscriber about the latest news.'
        # A copy of the list, so a subscriber may unsubscribe during notify().
        for subscriber in list(self.subscribers):
            subscriber.update(self.latest_news)

    def add_news(self, news: str) -> None:
        'Change the state and notify - the two always go together.'
        self.latest_news = news
        self.notify()


class NewsReader:
    'An observer. It only has to offer an update() method (duck typing).'

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, news: str) -> None:
        print(f'{self.name} received news: {news}')


class NewsArchive:
    'Another observer, doing something completely different.'

    def __init__(self) -> None:
        self.history: list[str] = []

    def update(self, news: str) -> None:
        self.history.append(news)
        print(f'[archive] {len(self.history)} news stored')


if __name__ == '__main__':
    publisher = NewsPublisher()

    reader1 = NewsReader('Ali')
    reader2 = NewsReader('Sara')
    archive = NewsArchive()

    publisher.subscribe(reader1)
    publisher.subscribe(reader2)
    publisher.subscribe(archive)

    publisher.add_news('Python 3.14 is released')

    print('---')
    publisher.unsubscribe(reader2)
    publisher.add_news('Kadoos opens a new Python class')

    print('---')
    print('archive:', archive.history)
