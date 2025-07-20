# Crop_Yield_Predictions
 🔍 Purpose of the Project
The app predicts crop yield (in tonnes per hectare) based on several agricultural parameters such as:

Year

Rainfall

Pesticide usage

Average temperature

Area (region/state)

Crop type



📁 Key Files in the Project
1. app.py
This is the main Streamlit application that provides a web interface for users to enter agricultural data and get predictions.

Uses a trained model (dtr.pkl) and a preprocessing pipeline (preprocessor.pkl) loaded via pickle.

Collects user input through a form.

Transforms the input using the preprocessor.

Makes predictions using the decision tree regressor (dtr) model.

Displays the result on the web page.

2. crop_yield_prediction.ipynb
This is likely a Jupyter Notebook used for:

Data cleaning

Exploratory Data Analysis (EDA)

Preprocessing (label encoding, scaling, etc.)

Training the model (probably a Decision Tree Regressor)

Saving the model (dtr.pkl) and preprocessor (preprocessor.pkl)

3. yield_df.csv
This CSV file is probably the dataset used to train and evaluate the model. It contains:

Historical data with features like year, rainfall, pesticides, temperature, area, crop type, and yield.



🔧 Workflow
Data Preparation

yield_df.csv is loaded and cleaned.

Categorical columns (like area and item) are encoded.

Features are scaled or normalized.

Model Training

A machine learning model (Decision Tree Regressor) is trained to predict yield.

The model and preprocessor are saved using pickle.

Web App

Users provide new input data in the web UI.

The app uses the preprocessor and model to predict the crop yield.

The result is shown interactively.



🖥️ How to Run the App
pip install streamlit numpy scikit-learn
streamlit run app.py



✅ Use Cases
Helps farmers and agricultural planners forecast crop yields.

Useful for agricultural research and policy-making.

Can guide decisions on crop selection based on environmental parameters.
