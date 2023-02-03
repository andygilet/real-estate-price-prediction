from flask import Flask, render_template, redirect, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from forms import property_entry_form
from werkzeug.datastructures import MultiDict
import pandas as pd
import pickle

def model_prediction(result : dict) -> str:
    model = pickle.load(open("API/model.pickle", "rb"))
    df = pd.DataFrame([result])
    price_range = model.predict(df)
    return f"{price_range * 10000}-{(price_range + 1) * 10000}"

def data_verification(data : MultiDict):
    list_keys_value = [False * 16]
    clean_data = {}
    
    for key in data.keys():
        if key == "area":
            list_keys_value[0] = True
        elif key == "property_type":
            list_keys_value[1] = True
        elif key == "rooms_number":
            list_keys_value[2] = True
        elif key == "zip_code":
            list_keys_value[3] = True
        elif key == "land_area":
            list_keys_value[4] = True
        elif key == "garden":
            list_keys_value[5] = True
        elif key == "garden_area":
            list_keys_value[6] = True
        elif key == "equipped_kitchen":
            list_keys_value[7] = True
        elif key == "full_address":
            list_keys_value[8] = True
        elif key == "swimming_pool":
            list_keys_value[9] = True
        elif key == "furnished":
            list_keys_value[10] = True
        elif key == "open_fire":
            list_keys_value[11] = True
        elif key == "terrace":
            list_keys_value[12] = True
        elif key == "terrace_area":
            list_keys_value[13] = True
        elif key == "facade_number":
            list_keys_value[14] = True
        elif key == "building_state":
            list_keys_value[15] = True
            
        if list_keys_value[0] == False:
            return {}, False
        else :
            if data["area"] != "":
                clean_data["area"] = int(data["area"])
            else:
                return {}, False
        
        #place le chiffre correspondant au type de propriété
               
        if list_keys_value[2] == False:
            return {}, False
        else:
            if data["rooms_number"] != "":
                clean_data["area"] = int(data["area"])
            else:
                return {}, False
            
        if list_keys_value[3] == False:
            return {}, False
        else:
            if data["zip_code"] != "":
                clean_data["zip_code"] = int(data["zip_code"])
            else:
                return {}, False
            
        if list_keys_value[4] == False:
            clean_data["land_area"] = 0
        else:
            clean_data["land_area"] = int(data["land_area"])
            
        if list_keys_value[5] == False:
            clean_data["garden"] = 0
            clean_data["garden_area"] = 0
        else:
            if data["garden"] == "y":
                clean_data["garden"] = 1
                if list_keys_value[6] == False:
                    clean_data["garden_area"] = 0
                else:
                    clean_data["garden_area"] = int(data["garden_area"])
            else:
                clean_data["garden"] = 0
                clean_data["garden_area"] = 0
            
                
        if list_keys_value[7] == False:
            clean_data["equipped_kitchen"] = 0
        else:
            
        if list_keys_value[8] == False:
        if list_keys_value[9] == False:
        if list_keys_value[10] == False:
        if list_keys_value[11] == False:
        if list_keys_value[12] == False:
        if list_keys_value[13] == False:
        if list_keys_value[14] == False:
        
        #place le chiffre correspondant à l'état de la propriété
            
    return clean_data, True
    
    
app = Flask(__name__, template_folder='templates', static_folder='templates/assets')
app.config['SECRET_KEY'] = 'ValeureuxLiegeois'
api = Api(app)

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = property_entry_form()
    if form.is_submitted():
        result = request.form
        result, return_status = data_verification(result)
        if return_status == False:
            result = "The area, property_type, rooms_number, and zip_code fields are required !"
        else:
            result = "This property is estimated " + model_prediction(result) + " euros"
        return render_template('index.html', form=form, result=result)
    return render_template('index.html', form=form)

property_put_args = reqparse.RequestParser()
property_put_args.add_argument("area", type= int, help="Area of the property is required !", required=True)
property_put_args.add_argument("property-type", type=str, help="The type of property is required !", required=True)
property_put_args.add_argument("rooms-number", type=int, help="The number of rooms is required !", required=True)
property_put_args.add_argument("zip-code", type=int, help="The zip code is required", required=True)
property_put_args.add_argument("land-area", type=int, help="the size of the land", required=False)
property_put_args.add_argument("garden", type=bool, help="Is there a garden ?", required=False)
property_put_args.add_argument("garden-area", type=int, help="the size of the garden", required=False)
property_put_args.add_argument("equipped-kitchen", type=bool, help="Is there a fully-equipped kitchen ?", required=False)
property_put_args.add_argument("full-address", type=str, help="the complete address of the property", required=False)
property_put_args.add_argument("swimming-pool", type=bool, help="Is there at least one swimming pool ?", required=False)
property_put_args.add_argument("furnished", type=bool, help="Is the property already furnished ?", required=False)
property_put_args.add_argument("open-fire", type=bool, help="Is there at least one open-fire ?", required=False)
property_put_args.add_argument("terrace", type=bool, help="Is there a terrace ?", required=False)
property_put_args.add_argument("terrace-area", type=int, help="what is the size of the terrace", required=False)
property_put_args.add_argument("facade-number", type=int, help="Number of facade of the property", required=False)
property_put_args.add_argument("building-state", type=str, help="The state of the property", required=False)

class Property(Resource):
    def get(self):
        args = property_put_args.parse_args()
        new_property = {"area" : args["area"],
                        "property-type" : args["property-type"],
                        "rooms-number" : args["rooms-number"],
                        "zip-code" : args["zip-code"],
                        "land-area" : args["land-area"],
                        "garden" : args["garden"],
                        "garden-area" : args["garden-area"],
                        "equipped-kitchen" : args["equipped-kitchen"],
                        "full-address" : args["full-address"],
                        "swimming-pool" : args["swimming-pool"],
                        "furnished" : args["furnished"],
                        "open-fire" : args["open-fire"],
                        "terrace" : args["terrace"],
                        "terrace-area" : args["terrace-area"],
                        "facade-number" : args["facade-number"],
                        "building-state" : args["building-state"]}
        #verifier les données avant de les passer au model
        result = model_prediction(new_property)
        return {"estimation" : result}, 201
            
api.add_resource(Property, "/Property")

if __name__ == '__main__':
    app.run(debug=True, port=5000)