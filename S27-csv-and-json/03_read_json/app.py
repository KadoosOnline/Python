'''Reading a JSON file with the built-in json module.

JSON is the format of the web: almost every API answers with JSON.
json.load() turns it directly into Python lists and dictionaries.
'''

import json


def load_products(filename: str) -> list[dict]:
    '''Load the product list from a JSON file.'''
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)          # load() reads from a FILE
    return data


def print_summary(products: list[dict]) -> None:
    '''Print the total and the first products.'''
    print(f'Total products: {len(products)}')
    print('\nFirst 2 products:')
    for p in products[:2]:
        print(f"  ID: {p['id']}, Name: {p['name']}, "
              f"Manufacturer: {p['manufacturer']}, Date: {p['production_date']}")


def filter_by_tag(products: list[dict], tag: str) -> list[dict]:
    '''Return the products carrying a given tag.'''
    result = []
    for p in products:
        if tag in p['tags']:         # 'tags' is a nested list
            result.append(p)
    return result


def filter_by_category(products: list[dict], category: str) -> list[dict]:
    '''Return the products of a given category.'''
    result = []
    for p in products:
        if category in p['categories']:
            result.append(p)
    return result


def group_by_manufacturer(products: list[dict]) -> dict[str, list[str]]:
    '''Return {manufacturer: [product names]}.'''
    groups: dict[str, list[str]] = {}
    for p in products:
        groups.setdefault(p['manufacturer'], []).append(p['name'])
    return groups


def main() -> None:
    products = load_products('products.json')

    print_summary(products)

    print('\n--- Products tagged "CPU" ---')
    for p in filter_by_tag(products, 'CPU'):
        print(f"  {p['name']}")

    print('\n--- Products in category "Graphics Card" ---')
    for p in filter_by_category(products, 'Graphics Card'):
        tags = ', '.join(p['tags'])
        print(f"  {p['name']} ({tags})")

    print('\n--- Grouped by manufacturer ---')
    for manufacturer, names in group_by_manufacturer(products).items():
        print(f'  {manufacturer}: {len(names)}')


if __name__ == '__main__':
    main()
