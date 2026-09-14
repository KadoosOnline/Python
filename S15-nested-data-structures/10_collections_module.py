# The standard module 'collections' offers ready-made containers.
from collections import Counter, defaultdict, namedtuple

def main() -> None:
    # Counter counts everything for us.
    text = 'kadoos institute rasht'
    counter = Counter(text.replace(' ', ''))
    print(counter)
    print(counter.most_common(3))     # the three most frequent letters

    words = ['python', 'linux', 'python', 'sql', 'python']
    print(Counter(words))

    # defaultdict creates the missing value automatically.
    groups = defaultdict(list)
    students = [('python', 'Ali'), ('linux', 'Reza'), ('python', 'Sara')]
    for course, name in students:
        groups[course].append(name)   # no need to test whether the key exists
    print(dict(groups))

    # namedtuple: a tuple whose fields have names.
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(p, p.x, p.y)

if __name__ == '__main__':
    main()
