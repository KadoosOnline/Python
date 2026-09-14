'''Templates: HTML in a file, Python in the program.

Returning HTML from inside a Python string does not scale past three lines.
Flask uses **Jinja2**: an HTML file with holes in it.

    render_template('students.html', students=names, title='Our students')

Everything you pass by keyword becomes a variable inside the template.
Templates live in a folder called `templates/`, next to `app.py`. That name is
fixed.

The Jinja syntax:

    {{ value }}                     print a value
    {% if ... %} ... {% endif %}    a condition
    {% for x in items %} ... {% endfor %}   a loop
    {{ value | upper }}             a FILTER
    {# a comment #}

Filters worth knowing: `length`, `upper`, `lower`, `title`, `round`,
`default('-')`, `join(', ')`, `tojson`.
Inside a `for` loop, `loop.index` (1, 2, 3...), `loop.index0`, `loop.first`,
`loop.last`, and `{% else %}` for the empty case.

AUTO-ESCAPING -- the reason Jinja is also a security tool:
`{{ name }}` turns `<script>` into harmless text. If you switch that off with
`| safe` on something a visitor typed, you have just built an XSS hole. The
rule: never put `| safe` on data that came from a user.
'''

from flask import Flask, render_template


app = Flask(__name__)

STUDENTS = [
    {'name': 'Sara Ahmadi', 'city': 'Rasht', 'score': 18.5},
    {'name': 'Ali Rezaei', 'city': 'Lahijan', 'score': 15.0},
    {'name': 'Mina Karimi', 'city': 'Rasht', 'score': 19.75},
    {'name': 'Reza Nouri', 'city': 'Anzali', 'score': 9.5},
]


@app.route('/')
def home():
    return render_template('index.html', name='Kadoos',
                           student_count=len(STUDENTS))


@app.route('/students')
def students():
    return render_template('students.html', students=STUDENTS,
                           passing_mark=10)


@app.route('/empty')
def empty():
    '''The same template with an empty list: see the {% else %} of the loop.'''
    return render_template('students.html', students=[], passing_mark=10)


@app.route('/escaping')
def escaping():
    '''What auto-escaping protects you from.'''
    dangerous = '<script>alert("your site is mine")</script>'
    return render_template('escaping.html', text=dangerous)


if __name__ == '__main__':
    app.run(debug=True)
