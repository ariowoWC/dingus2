from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/22240/OneDrive - Wellington College/Documents/Smile (67)/coffee_database"

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


@app.route('/menu/<cat_id>')
def render_menu_page(cat_id):
    con = connect_database(DATABASE)
    query = "SELECT product_name, product_description, product_volume, product_image, product_price FROM product_db WHERE category_fk=1"
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    print(product_list)
    con.close()
    return render_template('menu.html', coffee_list=product_list)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
