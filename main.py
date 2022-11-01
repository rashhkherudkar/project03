#from distutils.command.config import config
import re
from Models.utils import HousePrice
from flask import Flask, jsonify, request, render_template
import config


app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("We are in Flask API")
    return render_template("index.html")

# @app.route("/Bengluru_House_Price_Prediction",methods=["POST","GET"])
# def get_house_predicted_price():
#     if request.method == "GET":
#         print("We are using GET method")

#         # availability=request.args.get('availability')
#         # location= request.args.get('location')
#         # size= request.args.get('size')
#         # total_sqft=float(request.args.get('total_sqft'))
#         # bath=float(request.args.get('bath'))
#         # balcony=float(request.args.get('balcony'))
#         # area_type=request.args.get('area_type')

#         print("availability,location,size,total_sqft,bath,balcony,area_type",availability,location,size,total_sqft,bath,balcony,area_type)

@app.route("/Testing_price",methods =['POST'])
def get_house_predicted_price():
        

    availability=request.form.get('availability')    
    location= request.form.get('location')
    size= request.form.get('size')
    total_sqft=float(request.form.get('total_sqft'))
    bath=float(request.form.get('bath'))
    balcony=float(request.form.get('balcony'))
    area_type=request.form.get('area_type')

                    


    Obj = HousePrice(availability,location,size,total_sqft,bath,balcony,area_type)
    result = Obj.get_house_price_prediction()
        
    return render_template("index.html",prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port = config.PORT_NUMBER, debug=True)
    