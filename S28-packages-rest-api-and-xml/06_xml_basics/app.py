'''First steps with xml.etree.ElementTree.'''

import xml.etree.ElementTree as ET


def show_books() -> None:
    'Read books.xml: elements with text, no attributes.'
    tree = ET.parse('books.xml')
    root = tree.getroot()

    print('root tag:', root.tag)

    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        print(f'  {title} - {author}')


def show_people() -> None:
    'Read fixed.xml: nested elements.'
    root = ET.parse('fixed.xml').getroot()

    for person in root.findall('person'):
        name = person.find('name').text
        age = person.find('age').text
        friends = [f.text for f in person.find('friends').findall('friend')]
        print(f'  {name} ({age}) - friends: {", ".join(friends)}')


def show_broken() -> None:
    'A document with two roots cannot be parsed.'
    try:
        ET.parse('broken.xml')
    except ET.ParseError as e:
        print('  broken.xml is invalid:', e)


def show_rss_shape() -> None:
    'The structure of an RSS feed: rss > channel > item.'
    root = ET.parse('rss_example.xml').getroot()
    channel = root.find('channel')

    print('  feed title:', channel.find('title').text)
    for item in channel.findall('item'):
        print('   -', item.find('title').text, '->', item.find('link').text)


def main() -> None:
    print('=== books.xml ===')
    show_books()
    print('\n=== fixed.xml ===')
    show_people()
    print('\n=== broken.xml ===')
    show_broken()
    print('\n=== rss_example.xml ===')
    show_rss_shape()


if __name__ == '__main__':
    main()
