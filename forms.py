from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddItemForm(FlaskForm):
	ebay_item = StringField(
		'Ebay Link',
		validators=[DataRequired()]

	)
	submit = SubmitField('Submit')
