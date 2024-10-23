```markdown
# Phone Price Prediction App

This is a Flask web application that predicts the price of mobile phones based on user inputs, such as company, features, details, rating, and reviews. The app leverages machine learning models and stores user data in a MongoDB database.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)


## Features

- Predicts mobile phone prices based on user input.
- Saves user predictions and information in a MongoDB database.
- Provides a user-friendly interface using Bootstrap.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computing.
- **Scikit-learn**: For machine learning algorithms and preprocessing.
- **Pickle**: For serializing and deserializing Python objects.
- **MongoDB**: For storing user data.
- **Bootstrap**: For responsive web design.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/nagannaCtI064/Phone-Price-Predcition.git 
   cd phone-price-prediction
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

   Ensure you have the following packages in `requirements.txt`:

   ```
   Flask
   numpy
   pandas
   scikit-learn
   pymongo
   ```

4. Create a MongoDB Atlas account and set up a cluster. Replace the MongoDB connection string in the `app.py` file with your connection details.

5. Load the model and encoders. Make sure you have `model.pkl`, `Company_encoder1.pkl`, `Detail_encoder2.pkl`, `feature_encoder3.pkl`, and `data.json` in the project directory.

## Usage

1. Run the application:

   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Fill out the form with the required information and click the **Predict** button.

4. The predicted price will be displayed on the page after the form submission.

## API Endpoints

- `GET /`: Displays the home page with the prediction form.
- `POST /predict`: Accepts form submissions for price predictions and returns the predicted price.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-BranchName`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-BranchName`).
5. Open a pull request.

