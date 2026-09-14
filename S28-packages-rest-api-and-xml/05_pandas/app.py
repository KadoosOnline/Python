'''pandas: the library used everywhere for tabular data.

    pip install -r requirements.txt

A DataFrame is a table: named columns, numbered rows.
'''

try:
    import pandas as pd
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')


def main() -> None:
    # 1. Build a DataFrame from a dictionary of columns.
    data = {
        'Product': ['Notebook', 'Pencil', 'Eraser', 'Pen', 'Ruler'],
        'Price': [15000, 5000, 3000, 12000, 8000],
        'Stock': [120, 340, 80, 210, 55],
    }
    df = pd.DataFrame(data)
    print('First rows:\n', df.head())

    # 2. Structure and statistics.
    print('\nColumn info:')
    df.info()
    print('\nDescriptive statistics:\n', df.describe())

    # 3. Filtering: the condition produces a mask of True/False.
    expensive = df[df['Price'] > 10_000]
    print('\nProducts above 10,000:\n', expensive)

    # 4. A computed column.
    df['Inventory Value'] = df['Price'] * df['Stock']
    print('\nWith the inventory value:\n', df)

    # 5. Aggregations.
    print('\nAverage price:', df['Price'].mean())
    print('Total inventory value:', df['Inventory Value'].sum())

    # 6. Sorting.
    print('\nSorted by price:\n', df.sort_values('Price', ascending=False))

    # 7. Reading and writing a CSV file in one line - compare with session 27!
    df.to_csv('products.csv', index=False)
    again = pd.read_csv('products.csv')
    print('\nRead back from the CSV file:\n', again.head(2))


if __name__ == '__main__':
    main()
