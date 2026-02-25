from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "coffee_database"

app = Flask(__name__)


def connect_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print("error has occurred while connecting to the database")
    return


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu')
def render_menu_page():
    con = connect_database(DATABASE)
    query = "SELECT name, description, volume, image, price FROM product_db"
    cur = con.cursor()
    cur.execute(query)
    return render_template('menu.html')


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')



app.run(host='0.0.0.0', debug=True)
