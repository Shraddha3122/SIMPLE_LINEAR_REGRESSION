from sklearn.linear_model import LinearRegression
import pickle

# Train and save the model (only needs to be done once)
def train_and_save_model():
    import pandas as pd
    data = pd.read_csv('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/homeprices.csv')
    X = data[['area']]
    y = data['price']
    model = LinearRegression()
    model.fit(X, y)
    with open('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/model.pkl', 'wb') as file:
        pickle.dump(model, file)

# Load the trained model
def load_model():
    with open('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/model.pkl', 'rb') as file:
        return pickle.load(file)


# Predict price
def predict_price(area):
    model = load_model()
    return round(model.predict([[area]])[0], 2)

# Uncomment to train and save the model
# train_and_save_model()
