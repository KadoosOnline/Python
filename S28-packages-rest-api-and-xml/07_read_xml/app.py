'''Turning an XML file into ordinary Python objects.

The useful methods of ElementTree:
    ET.parse(file)      -> a tree
    tree.getroot()      -> the root element
    element.find(tag)   -> the FIRST child with that tag (None when missing)
    element.findall(tag)-> a list of every child with that tag
    element.get(name)   -> the value of an ATTRIBUTE (None when missing)
    element.text        -> the text between the tags
'''

import json
import xml.etree.ElementTree as ET


def parse_xml_to_list(filename: str) -> list[dict]:
    'Read products.xml and return a list of dictionaries.'
    tree = ET.parse(filename)
    root = tree.getroot()

    products: list[dict] = []

    for product_elem in root.findall('product'):
        product: dict = {}

        # The attributes of <product ...>
        product['id'] = int(product_elem.get('id'))
        product['name'] = product_elem.get('name')
        product['serial'] = product_elem.get('serial')
        product['manufacturer'] = product_elem.get('manufacturer')
        product['production_date'] = product_elem.get('production_date')

        # The nested <tags><tag>...</tag></tags>
        # find() returns None when the element is missing, so we must test it.
        tags_elem = product_elem.find('tags')
        tag_list: list[str] = []
        if tags_elem is not None:
            for tag in tags_elem.findall('tag'):
                tag_list.append(tag.text)
        product['tags'] = tag_list

        categories_elem = product_elem.find('categories')
        category_list: list[str] = []
        if categories_elem is not None:
            for category in categories_elem.findall('category'):
                category_list.append(category.text)
        product['categories'] = category_list

        products.append(product)

    return products


def main() -> None:
    products = parse_xml_to_list('products.xml')

    # Once the data is in Python containers, everything we know works.
    print(f'{len(products)} products read.\n')

    print('Products tagged "GPU":')
    for product in products:
        if 'GPU' in product['tags']:
            print('  -', product['name'])

    # And exporting it as JSON is one line (session 27).
    print('\nThe same data as JSON:')
    print(json.dumps(products[:2], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
