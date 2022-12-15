from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Tytuł książki', validators=[DataRequired()])
    author = TextAreaField('Autor', validators=[DataRequired()])
    read = BooleanField('Przeczytana tak/nie ?')