'''Building an XML document with ElementTree.

    ET.Element(tag)              -> the root
    ET.SubElement(parent, tag)   -> a child
    element.text = '...'         -> its text (must be a STRING)
    element.set('name', value)   -> an attribute
'''

import xml.dom.minidom
import xml.etree.ElementTree as ET


def create_sample_news() -> list[dict]:
    'Build the data we want to save (same data as session 27).'
    return [
        {
            'news_id': 1001,
            'title': 'New GPU Generation Released',
            'content': 'Manufacturers announce next-gen graphics cards.',
            'tags': ['hardware', 'GPU', 'gaming'],
            'comments': [
                {'user': 'TechFan42', 'text': "Can't wait to upgrade!", 'likes': 12},
                {'user': 'SkepticOne', 'text': 'Prices will be high.', 'likes': 5},
            ],
        },
        {
            'news_id': 1002,
            'title': 'AI Breakthrough in Chip Design',
            'content': 'Researchers use AI to speed up processor layout.',
            'tags': ['AI', 'chips', 'research'],
            'comments': [
                {'user': 'FutureVision', 'text': 'This is the future.', 'likes': 18},
            ],
        },
    ]


def news_list_to_xml(news_list: list[dict]) -> ET.ElementTree:
    'Turn the list of articles into an XML tree.'
    root = ET.Element('news')

    for article in news_list:
        article_elem = ET.SubElement(root, 'article')

        # The id fits better as an attribute than as a child element.
        article_elem.set('id', str(article['news_id']))

        # .text must always be a string - that is why we call str().
        ET.SubElement(article_elem, 'title').text = article['title']
        ET.SubElement(article_elem, 'content').text = article['content']

        tags_elem = ET.SubElement(article_elem, 'tags')
        for tag in article['tags']:
            ET.SubElement(tags_elem, 'tag').text = tag

        comments_elem = ET.SubElement(article_elem, 'comments')
        for comment in article['comments']:
            comment_elem = ET.SubElement(comments_elem, 'comment')
            ET.SubElement(comment_elem, 'user').text = comment['user']
            ET.SubElement(comment_elem, 'text').text = comment['text']
            ET.SubElement(comment_elem, 'likes').text = str(comment['likes'])

    return ET.ElementTree(root)


def pretty_print_xml(tree: ET.ElementTree) -> bytes:
    '''Return the tree as nicely indented bytes.

    ElementTree writes everything on one line; minidom re-formats it.
    (From Python 3.9 on, ET.indent(tree) does the same job.)
    '''
    rough_string = ET.tostring(tree.getroot(), encoding='utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='  ', encoding='utf-8')


def main() -> None:
    news = create_sample_news()
    tree = news_list_to_xml(news)

    # Written in BINARY mode ('wb') because toprettyxml() returned bytes.
    with open('news.xml', 'wb') as f:
        f.write(pretty_print_xml(tree))

    print('News saved to news.xml')

    # The simpler modern way:
    ET.indent(tree, space='  ')
    tree.write('news_simple.xml', encoding='utf-8', xml_declaration=True)
    print('The same file written with ET.indent(): news_simple.xml')


if __name__ == '__main__':
    main()
