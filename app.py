from flask import Flask, render_template, request
import numpy as np
import pickle
import os
import gdown

app = Flask(__name__)

# 🔽 Google Drive direct download link (unga link replace pannunga)
url = "url = "https://drive.google.com/uc?export=download&id=12Obba6uTFVmkKxZkAI7Bb6hPzD60T2Ii""
output = "cardio_model.pkl"

# 🔽 Model file illana download pannum
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# 🔽 Model load
model = pickle.load(open(output, "rb"))

# 🔽 Home page
@app.route('/')
def home():
    return render_template("index.html")

# 🔽 Prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        final_input = np.array([data])

        prediction = model.predict(final_input)

        if prediction[0] == 1:
            result = "⚠️ Heart Disease Detected"
        else:
            result = "✅ No Heart Disease"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="Error in input ❌")

# 🔽 Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
