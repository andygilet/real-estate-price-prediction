from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField

class property_entry_form(FlaskForm):
    area = IntegerField('area')
    property_type = SelectField('property_type', choices=["test1", "test2"]) #Remettre les valeurs des types de propriété
    rooms_number = IntegerField('rooms_number')
    zip_code = IntegerField('zip_code')
    land_area = IntegerField('land_area')
    garden = BooleanField('garden', default=False)
    garden_area = IntegerField('garden_area')
    equipped_kitchen = BooleanField('equipped_kitchen', default=False)
    full_address = StringField('full_address')
    swimming_pool = BooleanField('swimming_pool', default=False)
    furnished = BooleanField('furnished', default=False)
    open_fire = BooleanField('open_fire', default=False)
    terrace = BooleanField('terrace', default=False)
    terrace_area = IntegerField('terrace_area')
    facade_number = IntegerField('facade_number')
    building_state = StringField('building_state')
    submit = SubmitField('submit')