import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/Problem 2/Salary_Data.csv')
X = data[['YearsExperience']]
y = data['Salary']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

def predict_salary(years_of_experience):
    """Predict salary based on years of experience."""
    return model.predict([[years_of_experience]])[0]
