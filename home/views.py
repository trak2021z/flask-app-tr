from flask import Blueprint, render_template

home_view = Blueprint('home_view', __name__)

posts = [
    {
        'author': "Janusz",
        'age': "15"
    },
    {
        'author': "Maria",
        'age': "23"
    }
]


@home_view.route('/')
def display_home_page():
    return 'Hello, World!'


@home_view.route('/data')
def api_polls():
    return render_template('home.html', posts=posts)
