from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    website = StringField('Website', validators=[DataRequired()])
    submit = SubmitField('Get Data')
