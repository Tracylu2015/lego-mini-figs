from flask import render_template,redirect
from miniFig_app import app
from miniFig_app.models.sell_fig import Sell_fig

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blindbox')
def blindbox():
    id = Sell_fig.get_blindbox()
    return redirect(f'/display_minifig/{id}')
