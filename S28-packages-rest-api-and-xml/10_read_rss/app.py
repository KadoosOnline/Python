'''Reading an RSS feed: XML downloaded from the web.

    pip install -r requirements.txt

Almost every blog and news site publishes an RSS feed at <site>/feed/.
It is XML, so it puts together everything of this session:
    requests (download) + ElementTree (parse) + json (save).
'''

import json
import xml.etree.ElementTree as ET

try:
    import requests
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')

SITE_URL = 'https://kadoosedu.ir'
OUTPUT_FILE = 'rss_posts.json'


def text_of(parent: ET.Element, tag: str) -> str:
    'Return the text of a child element, or an empty string when it is missing.'
    element = parent.find(tag)
    if element is None or element.text is None:
        return ''
    return element.text.strip()


def parse_rss(xml_content: bytes) -> list[dict]:
    '''Parse the XML of an RSS feed.

    The structure is always:  rss > channel > item*
    '''
    # fromstring() parses a string/bytes; parse() parses a file.
    root = ET.fromstring(xml_content)

    channel = root.find('channel')
    if channel is None:
        raise ValueError('this document is not an RSS feed')

    posts: list[dict] = []

    for item in channel.findall('item'):
        posts.append({
            'title': text_of(item, 'title'),
            'link': text_of(item, 'link'),
            'description': text_of(item, 'description'),
            'pubDate': text_of(item, 'pubDate'),
        })

    return posts


def main() -> None:
    feed_url = f'{SITE_URL}/feed/'

    try:
        response = requests.get(feed_url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching the RSS feed: {e}')
        return

    try:
        posts = parse_rss(response.content)
    except (ET.ParseError, ValueError) as e:
        print(f'The feed could not be parsed: {e}')
        return

    print(f'{len(posts)} posts found:')
    for post in posts[:5]:
        print(f"  - {post['title']}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    print(f'RSS posts saved to {OUTPUT_FILE}')


if __name__ == '__main__':
    main()
