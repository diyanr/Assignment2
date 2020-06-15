from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    website = StringField('Website', validators=[DataRequired()])
    records = SelectField('Number of records', choices=[25, 50, 75, 100], default=2)
    submit = SubmitField('Get Data')
