from flask import Flask, render_template, g
import requests
from home.views import home_view
import sqlite3


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


def get_csv_data():
    data_url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
    req = requests.get(data_url)
    url_content = req.content
    print("Siema, odczytalem")


def create_app(config_file: str):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(home_view)
    return app


if __name__ == '__main__':
    get_csv_data()
    app = create_app('settings.py')
    app.run()
