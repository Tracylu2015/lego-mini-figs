from flask import render_template
from miniFig_app import app, cache

@app.route('/')
def index():
    return render_template('index.html')
