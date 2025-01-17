from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["DEBUG"] = True 
app.config["SECRET_KEY"] = "secret"

class Nameform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
# @app.route('/')
# def hello_world():
#     return '<h1>Hello World! from nikhil</h1>'

@app.route('/')
def index():
    Languages = ["Python", "Java", "C++", "C", "JavaScript", "HTML", "CSS", "PHP", "SQL", "MySQL", "MongoDB", "Flask"]
    stuff = "Hello World! from <b>nikhil</b>"
    Books = ["Animal Farm","Rich Dad Poor Dad","Monk who sold the ferrari","The Great Gatsby","The Hitchhiker's Guide to the Galaxy","Harry Potter and the Philosopher's Stone","The Lord of the Rings","The Hobbit","Lord of the Rings","Harry Potter and the Deathly Hallows"]
    return render_template('index.html', stuff = stuff, languages = Languages, Books = Books)



@app.route('/user/<name>')
def hello_name(name):
 
    return render_template("user.html", user_name = name)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)

@app.route('/print')
def print_stuff():
    return "<h1>Hello World! from nikhil</h1>" 

# creating custom error pages

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# internal server error 500
@app.errorhandler(500)
def internal_server(e):
    return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = Nameform()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = None 
    return render_template("name.html",name=name, form = form)

