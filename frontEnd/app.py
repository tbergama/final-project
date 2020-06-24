from flask import Flask, render_template, redirect, request, jsonify
from flask_pymongo import PyMongo
import os
import pymongo
from bson.json_util import dumps
import json
import pickle
import numpy as np
import pandas as pd

# Load the model and scaler
from tensorflow.keras.models import load_model
model = load_model('../tom/keras_model.h5')
scaler = pickle.load(open("../tom/min_max_scaler.pkl", "rb"))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/model-predict', methods=['POST'])
def predict_rent_price():
    feature_dict = request.get_json()

    # Define rent columns and medians
    rent_cols = ['city_Antelope', 'city_Carmichael', 'city_Citrus Heights', 'city_Elk Grove', 
        'city_Fair Oaks', 'city_Folsom', 'city_Gold River', 'city_North Highlands', 'city_Orangevale', 
        'city_Rancho Cordova', 'city_Rio Linda', 'city_Sacramento', 'city_West Sacramento', 'city_Wilton', 
        'neighborhood_Alkali Flat', 'neighborhood_American River Canyon', 
        'neighborhood_American River Canyon North', 'neighborhood_Arcade Creek', 
        'neighborhood_Birdcage Heights', 'neighborhood_Boulevard Park', 'neighborhood_Broderrick/Bryte', 
        'neighborhood_Campus Commons', 'neighborhood_Cannon Industrial Park', 'neighborhood_Capital Village', 
        'neighborhood_Carelton Tract', 'neighborhood_Central Oak Park', 'neighborhood_Chase', 
        'neighborhood_College-Glen', 'neighborhood_Colonial Heights', 'neighborhood_Colonial Manor', 
        'neighborhood_Colonial Village', 'neighborhood_Cordova Lane', 'neighborhood_Cordova Meadows', 
        'neighborhood_Cordova Vineyards', 'neighborhood_Creekside', 'neighborhood_Curtis Park', 
        'neighborhood_Del Paso Heights', 'neighborhood_Del Paso Park', 'neighborhood_Downtown', 
        'neighborhood_East Del Paso Heights', 'neighborhood_East Sacramento', 'neighborhood_Elmhurst', 
        'neighborhood_Fairgrounds', 'neighborhood_Foothill Farms', 'neighborhood_Fruitridge Manor', 
        'neighborhood_Gateway Center', 'neighborhood_Gateway West', 'neighborhood_Glenwood Meadows', 
        'neighborhood_Golf Course Terrace', 'neighborhood_Greenhaven', 'neighborhood_Hagginwood', 
        'neighborhood_Land Park', 'neighborhood_Lighthouse', 'neighborhood_Little Pocket', 
        'neighborhood_Mangan Park', 'neighborhood_Mansion Flats', 'neighborhood_Marshall School', 
        'neighborhood_Meadowview', 'neighborhood_Medical Center', 'neighborhood_Metro Center', 
        'neighborhood_Michigan-Glide-Sutter', 'neighborhood_Midtown - Winn Park Capital Avenue', 
        'neighborhood_Mills Ranch', 'neighborhood_Natomas Creek', 'neighborhood_Natomas Crossing', 
        'neighborhood_Natomas Park', 'neighborhood_New Era Park', 'neighborhood_Newton Booth', 
        'neighborhood_Noralto', 'neighborhood_North City Farms', 'neighborhood_North Highlands', 
        'neighborhood_North Oak Park', 'neighborhood_Northeast Village', 'neighborhood_Northgate', 
        'neighborhood_Northwest', 'neighborhood_Northwest Village', 'neighborhood_Oak Knoll', 
        'neighborhood_Old North Sacramento', 'neighborhood_Old West Sacramento', 'neighborhood_Park Oaks', 
        'neighborhood_Parkway', 'neighborhood_Pocket', 'neighborhood_Port North', 
        'neighborhood_RP Sports Complex', 'neighborhood_Richmond Grove', 'neighborhood_Rio del Oro', 
        'neighborhood_River Gardens', 'neighborhood_River Park', 'neighborhood_Robla', 
        'neighborhood_Rusch Park', 'neighborhood_Sierra Oaks', 'neighborhood_South City Farms', 
        'neighborhood_South Hagginwood', 'neighborhood_South Land Park', 'neighborhood_South Natomas', 
        'neighborhood_South Oak Park', 'neighborhood_South White Rock', 'neighborhood_Southside Park', 
        'neighborhood_Southwest Village', 'neighborhood_Sun River', 'neighborhood_Sunridge Anatolia', 
        'neighborhood_Sunridge Park', 'neighborhood_Sunrise Oaks', 'neighborhood_Sunrise Ranch', 
        'neighborhood_Swanston Estates', 'neighborhood_Sylvan Old Auburn Road', 'neighborhood_Tahoe Park', 
        'neighborhood_Tahoe Park East', 'neighborhood_Tahoe Park South', 'neighborhood_Tallac Village', 
        'neighborhood_Triangle', 'neighborhood_Upper Land Park', 'neighborhood_Valley High-North Laguna', 
        'neighborhood_Village 11', 'neighborhood_Village 12', 'neighborhood_Village 2', 
        'neighborhood_Village 5', 'neighborhood_Village 7', 'neighborhood_Village 9', 
        'neighborhood_Vineyard', 'neighborhood_Walnut Wood', 'neighborhood_West Tahoe Park', 
        'neighborhood_Westlake', 'neighborhood_White Rock', 'neighborhood_Willowcreek', 
        'neighborhood_Wills Acres', 'neighborhood_Woodlake', 'home_type_Apartment', 'home_type_Multi Family', 
        'home_type_Single Family Home', 'home_type_Townhouse', 'smoking', 
        'living_room', 'dishwasher', 'microwave', 
        'refrigerator', 'on_site_maint', 
        'on_site_mng', 'laundry_Hookups', 'laundry_In Unit', 'laundry_Laundry Facilities', 
        'laundry_OnSiteLaundry', 'laundry_Shared', 'air_con', 
        'disposal', 'dryer', 'patio', 'pool', 'balcony', 'washer_Washer', 
        'washer_Washer Dryer Hookup', 'basketball', 'ceiling_fan', 
        'fireplace', 'fitness', 'playground', 'floor_types_Concrete', 
        'floor_types_Hardwood', 'floor_types_Laminate', 'floor_types_Linoleum Vinyl', 'floor_types_Tile', 
        'bbq', 'vaulted_ceiling', 'rparking_On Street', 
        'rparking_Off Street', 'rparking_Garage Detached', 
        'rparking_Garage Attached', 'pets_No pets allowed', 
        'pets_Cats allowed', 'pets_Small dogs allowed', 
        'pets_Large dogs allowed', 'util_Sewage', 'util_Garbage', 
        'util_Water', 'util_Hot Water', 'util_Internet', 'util_Cable', 
        'util_Electricity', 'util_Gas', 'util_Heat', 'util_Phone', 
        'zipcode_95605', 'zipcode_95608', 'zipcode_95610', 'zipcode_95621', 'zipcode_95624', 'zipcode_95628', 
        'zipcode_95630', 'zipcode_95660', 'zipcode_95662', 'zipcode_95670', 'zipcode_95673', 'zipcode_95691', 
        'zipcode_95693', 'zipcode_95742', 'zipcode_95758', 'zipcode_95811', 'zipcode_95814', 'zipcode_95815', 
        'zipcode_95816', 'zipcode_95817', 'zipcode_95818', 'zipcode_95819', 'zipcode_95820', 'zipcode_95821', 
        'zipcode_95822', 'zipcode_95823', 'zipcode_95824', 'zipcode_95825', 'zipcode_95826', 'zipcode_95827', 
        'zipcode_95828', 'zipcode_95829', 'zipcode_95831', 'zipcode_95832', 'zipcode_95833', 'zipcode_95834', 
        'zipcode_95835', 'zipcode_95838', 'zipcode_95841', 'zipcode_95842', 'zipcode_95843', 'zipcode_95864', 
        'beds', 'baths', 'square_footage', 'year_built']
    rent_medians = {'beds': 2.0,
        'baths': 2.0,
        'square_footage': 1100.0,
        'year_built': 1972.0}
    
    # Initialize encoded list for input with all 0s (and median numeric values)
    encoded_list = [0 for i in rent_cols[:-4]]
    for val in rent_medians.values():
        encoded_list.append(val)
    
    
    # Read through request data and update the encoded list
    for feature in feature_dict:
        # print(feature)
        if feature['value'] == '':
            continue
        elif feature['value'] == 'No':
            continue
        elif feature['value'] == 'Yes':
            encoded_list[rent_cols.index(feature['name'])] = 1
        else:
            try:
                if feature['name'] in rent_medians.keys():
                    encoded_list[rent_cols.index(feature['name'])] = feature['value']
                else:                
                    encoded_list[rent_cols.index(f"{feature['name']}_{feature['value']}")] = 1
            except Exception as e:
                continue
    
    # print(encoded_list)
    
    # Scale data
    print('Scaling data...')
    scaled_features = scaler.transform(pd.DataFrame([encoded_list]))
    
    # Return prediction
    print('Returning prediction...')
    prediction =  model.predict(scaled_features)
    print(str(prediction[0][0]))
    return str(round(prediction[0][0]))


# Run app
if __name__ == '__main__':
    app.run(debug=True)