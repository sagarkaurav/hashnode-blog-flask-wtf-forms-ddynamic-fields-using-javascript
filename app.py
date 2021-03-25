from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList
from wtforms.validators import DataRequired


class FavouriteMoviesForm(FlaskForm):
    username = StringField("Your name", validators=[DataRequired()])
    movies = FieldList(StringField('Movie Name'), min_entries=1, max_entries=5)

app = Flask(__name__, template_folder='./templates')
app.config['SECRET_KEY'] = "mysupersecretkey"

@app.route('/', methods=['GET', 'POST'])
def index():
    favouriteMoviesForm  = FavouriteMoviesForm()
    if favouriteMoviesForm.validate_on_submit():
        return render_template('submit.html', username=favouriteMoviesForm.username.data, movies=favouriteMoviesForm.movies.entries)
    return render_template('index.html', form=favouriteMoviesForm)