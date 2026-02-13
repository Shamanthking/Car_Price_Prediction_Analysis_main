<<<<<<< HEAD
# USED_CAR_PRICE_PREDICTION

## Overview
This project aims to predict the price of used cars based on various features such as brand, model, year, fuel type, transmission, mileage, and more. The project leverages **Machine Learning** techniques and uses algorithms like **Random Forest, XGBoost, and Linear Regression** to make accurate price predictions. A **Flask-based web application** is developed to provide an interactive user interface for predictions.

## Project Structure
```
USED_CAR_PRICE_PREDICTION/
│── static/                 # Contains CSS, JS, and images for the web UI
│── templates/              # HTML templates for Flask app
│── model/                  # Trained model and related files
│── app.py                  # Main Flask application
│── requirements.txt        # Required Python packages
│── dataset.csv             # Dataset used for training
│── preprocessing.py        # Data preprocessing script
│── model_training.py       # Model training script
│── model.pkl               # Saved trained model
│── README.md               # Project documentation
```

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning Libraries**: Pandas, NumPy, scikit-learn, XGBoost
- **Visualization Libraries**: Matplotlib, Seaborn
- **Model Deployment**: Flask (latest stable version)

## Dataset
The dataset contains the following features:
- **Car Name**: Brand and Model
- **Year**: Year of Manufacture
- **Selling Price**: Target variable (Price of the used car)
- **Present Price**: Showroom price of the car
- **Kms Driven**: Total kilometers driven
- **Fuel Type**: Petrol, Diesel, or CNG
- **Transmission**: Manual or Automatic
- **Owner**: Number of previous owners

## Data Preprocessing
1. Handling missing values (if any).
2. Encoding categorical variables (Fuel Type, Transmission, Owner).
3. Feature Scaling using **StandardScaler**.
4. Splitting data into training and testing sets.

## Model Training
The following models are trained and evaluated:
1. **Linear Regression**: Simple and interpretable but may not capture complex relationships.
2. **Random Forest**: A powerful ensemble model that performs well for structured data.
3. **XGBoost**: Gradient boosting algorithm that provides better accuracy and generalization.

**Evaluation Metrics Used:**
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score (Coefficient of Determination)

## Flask Web Application
The Flask-based web application provides an interactive interface where users can input car details and get price predictions. The web app includes:
- **User-friendly interface** using HTML, CSS.
- **Input form** to enter car details.
- **Prediction display** showing the estimated price.

## How to Run the Project
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Deekshithshaiva05/USED_CAR_PRICE_PREDICTION.git
   cd USED_CAR_PRICE_PREDICTION
   ```
2. **Create a virtual environment (Optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. **Install required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask application**:
   ```sh
   python app.py
   ```
5. **Open the web app in a browser**:
   ```
   http://127.0.0.1:5000/
   ```

## Future Enhancements
- Add more features like car condition, insurance details, etc.
- Use Deep Learning models for better accuracy.
- Deploy the model using **Docker and Cloud Services**.

## Conclusion
This project successfully predicts the price of used cars using machine learning models. It demonstrates data preprocessing, model training, evaluation, and web-based deployment using Flask.

## Contributors
- **Deekshith N** (GitHub: [Deekshithshaiva05](https://github.com/Deekshithshaiva05))

## License
This project is open-source and available under the **MIT License**.


![Screenshot 2025-02-21 215328](https://github.com/user-attachments/assets/9ae4e791-e394-4c10-afc9-dfec5f18ccd5)
=======
# Car_Price_Prediction_Analysis_main
>>>>>>> eeb6c43ee9a666919a5177e700ccc9b182c0bd02
