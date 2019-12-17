from api import app
from flask import render_template
from flask_pymongo import PyMongo
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
import logging
from types import *

mongo = PyMongo(app)

@app.route('/bokeh', methods=['GET'])
def bokeh():
    star = mongo.db.stars
    names = []
    distances = []

    for s in star.find():
        names.append(s['name'])
        distances.append(s['distance'])

    names_list = list(map(int, names))
    distances_list = list(map(int, distances))

    app.logger.info(names)

    fig = figure(plot_width=800, plot_height=400)
    fig.vbar(x=names_list, width=0.8, bottom=0,
             top=distances_list, color="#CAB2D6")

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'bokeh.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(debug=True)

