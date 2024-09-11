import sys
import json
from flask import Flask, url_for, render_template, jsonify
from flask_mysqldb import MySQLdb
#from dbconnect import connection
app = Flask(__name__)

db = MySQLdb.connect("localhost",
"webviewer",
"webview",
"ffxi_findall"
)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/inventory')
def inventory():
	return render_template("inventory.html")

@app.route('/get_json_data')
def json_data():
	cur = db.cursor()
	return_str = "SELECT * FROM aeliya"
	cur.execute(return_str)
	rv = cur.fetchall()
	row_headers=[desc[0] for desc in cur.description]
	json_data = []
	new_json = []
	for result in rv:
		result = dict(zip(row_headers, result))
		json_data.append(result)
	new_json = {"data": json_data}
	return jsonify(new_json)

@app.route('/dbtest')
def dbtest():
	cur = db.cursor()
	return_str = "SELECT * FROM aeliya WHERE id LIKE '28612'"
	cur.execute(return_str)
	rv = cur.fetchall()
	row_headers=[desc[0] for desc in cur.description]
	json_data = []
	new_json = []
	for result in rv:
		result = dict(zip(row_headers, result))
		json_data.append(result)
	new_json = {'data': json_data}
	print(new_json)
	return jsonify(new_json)


if __name__ == "__main__":
    app.run(debug=True)