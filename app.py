from flask import Flask, render_template

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run()
