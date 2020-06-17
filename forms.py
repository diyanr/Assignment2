from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    website = StringField('Website', validators=[DataRequired()])
    records = StringField('Records', validators=[DataRequired()])
    submit = SubmitField('Get Data')


class ResultForm(FlaskForm):
    submit = SubmitField('Download Data')
