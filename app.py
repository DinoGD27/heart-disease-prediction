from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("cardio_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final = np.array([data])

    prediction = model.predict(final)

    if prediction[0] == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return render_template("index.html", prediction_text=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)