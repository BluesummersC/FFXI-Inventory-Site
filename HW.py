# HW.py

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/inventory')
def hello_inv():
    return 'Hello Inventroy!'
	
if __name__ == "__main__":
    app.run(debug=True)