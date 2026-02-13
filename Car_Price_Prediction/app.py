from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
from column_transformer import preprocessor

app = Flask(__name__)
CORS(app)

# Load the machine learning model
models = pickle.load(open('CatBoosting_Regressor.pkl', 'rb'))  # Renamed variable to avoid conflicts
car = pd.read_csv('cardekho_dataset.csv')



@app.route('/About')
def About():
    return render_template('about.html')

# Route for rendering the main HTML page
@app.route('/', methods=['GET', 'POST'])
def index():
    # Prepare dropdown options
    brand = sorted(car['brand'].unique())
    vehicle_age = sorted(car['vehicle_age'].unique(), reverse=True)
    seller_type = sorted(car['seller_type'].unique())
    fuel_type = car['fuel_type'].unique()
    transmission_type = car['transmission_type'].unique()
    seats = sorted(car['seats'].unique())

    # Add a placeholder option
    brand.insert(0, 'Select brand')

    return render_template(
        'index.html', 
        brand=brand, 
        vehicle_age=vehicle_age,
        seller_type=seller_type, 
        fuel_type=fuel_type, 
        transmission_type=transmission_type, 
        seats=seats
    )

# Route to get car models based on the selected brand
@app.route('/get_models', methods=['GET'])
def get_models():
    brand = request.args.get('brand')
    if not brand or brand == "Select brand":
        return jsonify({"models": []})  # Return empty if no valid brand

    # Filter models based on the selected brand
    models = car[car['brand'] == brand]['model'].unique().tolist()
    models.sort()
    return jsonify({"models": models})

# Route to handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input data from form
        brand = request.form.get('brand')
        car_model = request.form.get('model')
        vehicle_age = request.form.get('vehicle_age')
        km_driven = request.form.get('km_driven')
        seller_type = request.form.get('seller_type')
        fuel_type = request.form.get('fuel_type')
        transmission_type = request.form.get('transmission_type')
        mileage = request.form.get('mileage')
        engine = request.form.get('engine')
        max_power = request.form.get('max_power')
        seats = request.form.get('seats')

        # Validate and preprocess input
        if not all([brand, car_model, vehicle_age, km_driven, seller_type, 
                    fuel_type, transmission_type, mileage, engine, max_power, seats]):
            return jsonify({"success": False, "error": "Missing required fields."})

        try:
            vehicle_age = int(vehicle_age)
            km_driven = float(km_driven)
            mileage = float(mileage)
            engine = float(engine)
            max_power = float(max_power)
            seats = int(seats)
        except ValueError as ve:
            return jsonify({"success": False, "error": f"Invalid input format: {str(ve)}"})

        # Prepare input data for the preprocessor
        input_data = pd.DataFrame(
            columns=[
                'brand', 'model', 'vehicle_age', 'km_driven', 'seller_type', 
                'fuel_type', 'transmission_type', 'mileage', 'engine', 'max_power', 'seats'
            ],
            data=[[brand, car_model, vehicle_age, km_driven, seller_type, 
                   fuel_type, transmission_type, mileage, engine, max_power, seats]]
        )

        # Apply preprocessor
        transformed_data = preprocessor.transform(input_data)

        # Perform prediction
        prediction = models.predict(transformed_data)
        predicted_price = np.round(prediction[0], 2)

        return jsonify({"success":True,"price": predicted_price})

    except Exception as e:
        return jsonify({"success": False, "error": f"Error during prediction: {str(e)}"})
    
if __name__ == "__main__":
    app.run(debug=True)