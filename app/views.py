from flask import render_template

from . import app

@app.route('/', methods=['GET'])
def index():
    return render_template('entry.html')

@app.route('/arena', methods=['GET'])
def entry():
    return render_template('index.html')