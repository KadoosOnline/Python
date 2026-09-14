'''Writing JSON data into a file.

json.dump() writes to a FILE, json.dumps() returns a STRING.
'''

import json


def create_sample_news() -> list[dict]:
    '''Build a list of news articles.

    Notice the nesting: a list of dictionaries, each holding a list of tags
    and a list of comment dictionaries. JSON handles that naturally.
    '''
    news_list = []

    article1 = {
        'news_id': 1001,
        'title': 'New GPU Generation Released',
        'content': 'Manufacturers announce next-gen graphics cards.',
        'tags': ['hardware', 'GPU', 'gaming'],
        'comments': [
            {'user': 'TechFan42', 'text': "Can't wait to upgrade!", 'likes': 12},
            {'user': 'SkepticOne', 'text': 'Prices will probably be high.', 'likes': 5},
        ],
    }
    news_list.append(article1)

    article2 = {
        'news_id': 1002,
        'title': 'AI Breakthrough in Chip Design',
        'content': 'Researchers use AI to speed up processor layout.',
        'tags': ['AI', 'chips', 'research'],
        'comments': [
            {'user': 'FutureVision', 'text': 'This is the future.', 'likes': 18},
            {'user': 'CodeMaster', 'text': 'Open source the models!', 'likes': 9},
        ],
    }
    news_list.append(article2)

    article3 = {
        'news_id': 1003,
        'title': 'DDR5 RAM Prices Drop',
        'content': 'Memory manufacturers cut prices by 15%.',
        'tags': ['RAM', 'DDR5', 'prices'],
        'comments': [
            {'user': 'BuilderBob', 'text': 'Finally, time to build my PC.', 'likes': 7},
        ],
        'note': 'یک خبر فارسی',        # Persian text, to show ensure_ascii
    }
    news_list.append(article3)

    return news_list


def save_news_to_json(news: list[dict], filename: str) -> None:
    '''Write the articles into a JSON file.

    indent=2          -> a readable, indented file
    ensure_ascii=False-> keep the Persian letters instead of \\u06cc escapes
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(news, f, indent=2, ensure_ascii=False)

    print(f'{len(news)} news articles saved to {filename}')


def read_back(filename: str) -> None:
    '''Read the file again to prove that nothing was lost.'''
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    for article in data:
        print(f"- {article['title']} ({len(article['comments'])} comments)")


def main() -> None:
    news_data = create_sample_news()
    save_news_to_json(news_data, 'news.json')
    read_back('news.json')
    print('JSON writing completed.')


if __name__ == '__main__':
    main()
