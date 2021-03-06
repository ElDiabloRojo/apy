from api import app
from flask import render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from api.forms.forms import LoginForm


mongo = PyMongo(app)
Bootstrap(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('bootstrap'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/bootstrap', methods=['GET'])
def bootstrap():
    return render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)