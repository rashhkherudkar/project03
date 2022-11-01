import json
import pickle
import numpy as np
import pandas as pd
import config

class HousePrice():
    def __init__ (self,availability,location,size,total_sqft,bath,balcony,area_type):
        self.availability = availability
        self.location = location
        self.size = size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony = balcony
        self.area_type = "area_type_" + area_type


    def load_model(self):
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_dict=json.load(f)

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model=pickle.load(f)

    def get_house_price_prediction(self):
        self.load_model()

        array = np.zeros(len(self.json_dict['column']))

        array[0] = self.json_dict['availability'][self.availability]
        array[1] = self.json_dict['location'][self.location]
        array[2] = self.json_dict['size'][self.size]
        array[3] = self.total_sqft
        array[4] = self.bath
        array[5] = self.balcony

        area_type_index = self.json_dict['column'].index(self.area_type)

        array[area_type_index] = 1

        result = self.model.predict([array])[0]
        return round(result,2)

if __name__ == "__main__":
    availability = 'Ready To Move'
    location = 'Banashankari'
    size = '3 BHK'
    total_sqft = 1500.8
    bath = 3.0
    balcony = 4.0 
    area_type = 'Carpet  Area' 
 



    Obj = HousePrice(availability,location,size,total_sqft,bath,balcony,area_type)
    result = Obj.get_house_price_prediction()
    print(f"Price Prediction of Bengluru house is Rs.{result}/- only")