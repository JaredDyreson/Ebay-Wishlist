from flask import Flask, render_template, url_for, flash, redirect, request, session
from flask_oauthlib.client import OAuth, OAuthException
from forms import AddItemForm
from flask_wtf import FlaskForm
import EbayItem

application = Flask(__name__)
application.config['SECRET_KEY'] = '84c1c81be6f347629bf01b97fbbe883c'

# ROUTES #

@application.route("/", methods=['GET', 'POST'])
def index():
	form = AddItemForm(request.form)
	if(form.validate_on_submit()):
		url = form.ebay_item.data
		item = EbayItem.EbayItem(url)
		print(item.convert_to_dict())
	form = AddItemForm(fromdata=None)
	return render_template('home.html', form=form)

if __name__ == '__main__': application.run()
