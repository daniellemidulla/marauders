from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class EventForm(Form):
    event = StringField('event', default="")
    hasField = BooleanField('hasField', default=False)
