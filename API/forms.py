from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, SubmitField

class property_entry_form(FlaskForm):
    area = IntegerField('area')
    property_type = SelectField('property_type', choices=["house",
                                                          "apartment",
                                                          "villa",
                                                          "apartment-block",
                                                          "duplex",
                                                          "ground-floor",
                                                          "mixed-use-building",
                                                          "penthouse",
                                                          "exceptional-property",
                                                          "flat-studio",
                                                          "mansion",
                                                          "service-flat",
                                                          "town-house",
                                                          "loft",
                                                          "bungalow",
                                                          "country-cottage",
                                                          "triplex",
                                                          "chalet",
                                                          "manor-house",
                                                          "kot",
                                                          "other-property",
                                                          "farmhouse",
                                                          "castle",
                                                          "pavilion"]) #Remettre les valeurs des types de propriété
    rooms_number = IntegerField('rooms_number')
    zip_code = IntegerField('zip_code')
    land_area = IntegerField('land_area')
    garden = BooleanField('garden')
    garden_area = IntegerField('garden_area')
    equipped_kitchen = BooleanField('equipped_kitchen')
    full_address = StringField('full_address')
    swimming_pool = BooleanField('swimming_pool')
    furnished = BooleanField('furnished')
    open_fire = BooleanField('open_fire')
    terrace = BooleanField('terrace')
    terrace_area = IntegerField('terrace_area')
    facade_number = IntegerField('facade_number')
    building_state = SelectField('building_state', choices=["Good",
                                                            "As new",
                                                            "To renovate",
                                                            "To be done up",
                                                            "Just renovated",
                                                            "To restore"])
    submit = SubmitField('submit')