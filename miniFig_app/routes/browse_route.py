from flask import render_template
from miniFig_app import app
from miniFig_app.models.figure import Figure

all_themes = [
    "General", "Basic Set", "Disney Princess", "Duplo", "Super Heros", "City", "Star Wars", "Harry Potter"
]


@app.route('/browse_fig')
def browse_all():
    # query data and pass to the html
    data = Figure.browse_all()
    return render_template('browse_all.html', data=data)


@app.route('/browse_fig/year/<year>')
def browse_all_by_year(year=2021):
    data = Figure.browse_all_by_year(year)
    return render_template('year.html', data=data)


@app.route('/browse_fig/theme/<theme>')
def browse_all_by_theme(theme="General"):
    themes = Figure.browse_all_by_theme(theme)
    return render_template('theme.html', themes=themes, all_themes=all_themes)