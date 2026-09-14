'''matplotlib: the standard plotting library of Python.

    pip install -r requirements.txt
'''

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    raise SystemExit('Run "pip install -r requirements.txt" first.')


def line_chart() -> None:
    'A line chart with a title, axis labels and a legend.'
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [230, 310, 290, 420, 390]

    plt.plot(months, sales, marker='o', linestyle='--', color='blue', label='Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales (million $)')
    plt.title('Sales in the first five months')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()          # opens a window; close it to continue the program


def bar_chart() -> None:
    'A bar chart.'
    categories = ['Books', 'Movies', 'Music']
    counts = [45, 30, 25]

    plt.bar(categories, counts, color=['#FF9999', '#66B2FF', '#99FF99'])
    plt.title('Products by category')
    plt.ylabel('Count')
    plt.show()


def pie_and_save() -> None:
    'A pie chart, saved as an image instead of being shown.'
    labels = ['Python', 'SQL', 'Linux']
    values = [50, 30, 20]

    plt.pie(values, labels=labels, autopct='%1.0f%%')
    plt.title('Course registrations')
    plt.savefig('courses.png', dpi=120, bbox_inches='tight')
    plt.close()
    print('courses.png was written.')


def main() -> None:
    line_chart()
    bar_chart()
    pie_and_save()


if __name__ == '__main__':
    main()
