from flask import render_template
from miniFig_app import app, cache

@app.route('/')
@cache.cached(timeout=300)
def index():
    return render_template('index.html')



