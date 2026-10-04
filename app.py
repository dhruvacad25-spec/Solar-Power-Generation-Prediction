from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("tuned_random_forest_model.pkl")


# ==========================
# Home / About Page
# ==========================

@app.route("/")
def home():
    return render_template("home.html")


# ==========================
# Prediction Page
# ==========================

@app.route("/predict")
def prediction_page():
    return render_template("index.html")


# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    campus_key = float(request.form["campus_key"])
    site_key = float(request.form["site_key"])
    apparent_temperature = float(request.form["apparent_temperature"])
    air_temperature = float(request.form["air_temperature"])
    dew_point_temperature = float(request.form["dew_point_temperature"])
    relative_humidity = float(request.form["relative_humidity"])
    year = float(request.form["year"])
    month = float(request.form["month"])
    day = float(request.form["day"])
    hour = float(request.form["hour"])
    day_of_week = float(request.form["day_of_week"])

    # Arrange inputs in the same order used during training
    features = [[
        campus_key,
        site_key,
        apparent_temperature,
        air_temperature,
        dew_point_temperature,
        relative_humidity,
        year,
        month,
        day,
        hour,
        day_of_week
    ]]

    # Make prediction
    prediction = model.predict(features)[0]
    prediction = round(float(prediction), 2)

    return render_template(
        "result.html",
        prediction=prediction
    )


# ==========================
# Run Flask
# ==========================

if __name__ == "__main__":
    app.run(debug=True)