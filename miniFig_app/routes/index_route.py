from flask import render_template
from miniFig_app import app

@app.route('/')
def index():
    return render_template('index.html')



