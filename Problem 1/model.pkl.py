import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
data = pd.read_csv('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/homeprices.csv') 

# Prepare the data
X = data[['area']]  # Feature: area
y = data['price']   # Target: price

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a file
with open('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model has been trained and saved as 'model.pkl'.")
