from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('C:\\Users\\Suresh\\projects\\customer-churn-prediction\\models\\best_model.pkl', 'rb'))
scaler = pickle.load(open('C:\\Users\\Suresh\\projects\\customer-churn-prediction\\models\\scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        tenure = float(request.form['tenure'])
        monthly = float(request.form['monthly'])
        total = float(request.form['total'])
        contract = float(request.form['contract'])  
        internet = float(request.form['internet'])  

        features = np.array([[tenure, monthly, total, contract, internet]])
        features = scaler.transform(features)

        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        if prob > 0.7:
            risk = "🔴 High Flight Risk"
            risk_class = "bg-red-50 border-red-200 text-red-800"
        elif prob > 0.4:
            risk = "🟡 Medium Risk"
            risk_class = "bg-yellow-50 border-yellow-200 text-yellow-800"
        else:
            risk = "🟢 Safe (Low Risk)"
            risk_class = "bg-green-50 border-green-200 text-green-800"

        churn_status = "Likely to Churn" if prediction == 1 else "Likely to Stay"
        prediction_text = f"Status: {churn_status} ({prob * 100:.1f}% Probability)"

        return render_template('index.html', 
                               prediction_text=prediction_text, 
                               risk=risk, 
                               risk_class=risk_class)

    except Exception as e:
        return render_template('index.html', error_text=str(e))


if __name__ == "__main__":
    app.run(debug=True)