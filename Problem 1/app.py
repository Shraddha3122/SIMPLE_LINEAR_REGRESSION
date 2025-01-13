from flask import Flask, request, render_template
from model import predict_price  # Ensure this function exists in model.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    price = None  # Default value
    if request.method == 'POST':
        try:
            # Get the input value (house area) from the form
            area = float(request.form['area'])
            # Use the model to predict the price
            price = predict_price(area)

            # Debug: Print input and output
            print(f"Area: {area}, Predicted Price: {price}")
        except Exception as e:
            price = f"Error: {e}"
            print(f"Error occurred: {e}")  # Debug error log

    # Render the template with the predicted price
    return render_template('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/template/index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
