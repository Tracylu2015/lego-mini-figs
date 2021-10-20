from flask import render_template, jsonify, request
from miniFig_app import app
from miniFig_app.models.sell_fig import Sell_fig
from miniFig_app.models.figure import Figure
from miniFig_app.form import AddToCartForm

all_themes = [
    "General", "Basic Set", "Disney Princess", "Duplo, Town", "Castle", "City", "Star Wars", "Harry Potter"
]


@app.route('/browse_fig')
def browse_all():
    # query data and pass to the html
    data = Figure.browse_all()
    return render_template('browse_all.html', data=data)

@app.route('/browse_fig/by_selection')
def fetch_all():
    selection = request.args.get('selection', 'most_popular')
    # query data and pass to the html
    if selection == 'on_sale':
        data = [data.figure for data in Sell_fig.get_all_sell_by_selection()]
    else:
        data = Figure.browse_all()
    return jsonify({'html': render_template('by_all_sell.html', data=data)})

@app.route('/browse_fig/year/<year>')
def browse_all_by_year(year=2021):
    data = Figure.browse_all_by_year(year)
    return render_template('year.html', data=data)


@app.route('/browse_fig/by_year/<year>')
def fetch_by_year(year=2021):
    # Return partial html as json response to jquery request
    data = Figure.browse_all_by_year(year)
    return jsonify({'html': render_template('by_year.html', data=data)})


@app.route('/browse_fig/theme/<theme>')
def browse_all_by_theme(theme="General"):
    themes = Figure.browse_all_by_theme(theme)
    return render_template('theme.html', themes=themes, all_themes=all_themes)


@app.route('/browse_fig/by_theme/<theme>')
def fetch_by_theme(theme="General"):
    data = Figure.browse_all_by_theme(theme)
    return jsonify({'html': render_template('by_theme.html', data=data)})


@app.route('/display_minifig/<id>')
def get_one_detailed_fig(id):
    form = AddToCartForm()
    detailed_fig = Figure.get_one_by_fig_id(id)
    sell_info = Sell_fig.get_all_sell_info_by_fig_id(id)
    blindbox = Sell_fig.get_blindbox()
    return render_template('display_minifig.html', detailed_fig=detailed_fig, sell_info=sell_info, form=form, blindbox=blindbox)
