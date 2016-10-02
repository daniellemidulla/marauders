from flask import render_template, flash, redirect, request
from app import app
from .forms import EventForm

@app.route('/')
@app.route('/index')


def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = EventForm()
	if form.validate_on_submit():
		flash('Event Submitted="%s"' %(form.event.data))
	return render_template('login.html',
							title='Sign Up',
							form=form)

@app.route('/my-link/', methods=['POST', 'GET'])
def my_link():
	text = request.form['event']
 #   	processed_text = text.upper()
 	print 'clicked'
	return 'Click.'

@app.route('/result', methods=['POST', 'GET'])
def my_form_post():

    text = request.form['event']
    processed_text = text.upper()
    result = request.form
    return render_template("result.html", result=result)
