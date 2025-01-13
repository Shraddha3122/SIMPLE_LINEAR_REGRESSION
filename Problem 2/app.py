from flask import Flask, request, render_template, jsonify
from salary_model import predict_salary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('D:/WebiSoftTech/SIMPLE LINEAR REGRESSION/Problem 2/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        experience = float(request.form['experience'])
        salary = predict_salary(experience)
        return jsonify({'predicted_salary': salary})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
