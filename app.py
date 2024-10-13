from flask import Flask, render_template, request
import json
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
from pymongo import MongoClient

warnings.filterwarnings('ignore') 
app = Flask(__name__)

client=MongoClient("mongodb+srv://Naganna:Naganna890@cluster0.qhaksm0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client["Phone_Price"]
data=db["user_Data"]

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("Company_encoder1.pkl", "rb") as f:
    company_encoder = pickle.load(f)
with open("Detail_encoder2.pkl", "rb") as f:
    detail_encoder = pickle.load(f)
with open("feature_encoder3.pkl", "rb") as f:
    feature_encoder = pickle.load(f)
with open("data.json", "r") as f:
    validation_data = pd.read_json(f)
all_data = validation_data.to_dict('records')

def safe_transform(encoder, value):
    try:
        return encoder.transform([value])[0]
    except ValueError:
        new_classes = np.append(encoder.classes_, value)
        encoder.classes_ = new_classes
        return len(encoder.classes_) - 1

@app.route("/")
def home():
    return render_template("index.html", all_data=all_data)

@app.route("/predict", methods=["POST"])
def predict():
    company = request.form.get("Company")
    features = request.form.get("features")
    details = request.form.get("details")
    rating = float(request.form.get("rating"))
    reviews = int(request.form.get("reviews"))
    name = request.form.get("name")
    email = request.form.get("email")
    
    company_en = safe_transform(company_encoder, company)
    features_en = safe_transform(feature_encoder, features)
    details_en = safe_transform(detail_encoder, details)
    input_data = np.array([rating, reviews, features_en, company_en, details_en]).reshape(1, -1)
    
    output = model.predict(input_data)
    predicted_price = str(output[0].round())
    
    data1 = {
        "name": name,
        "email": email,
        "Intrested phone": company,
        "Estimated Price": predicted_price
    }
    data.insert_one(data1)
    
    return render_template("index.html", all_data=all_data, output=predicted_price)

if __name__ == "__main__":
    app.run(debug=True)