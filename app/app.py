from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and encoder
model = joblib.load("../model/best_model.pkl")
encoder = joblib.load("../model/label_encoder.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    features = [[
        float(request.form["LOC"]),
        float(request.form["CyclomaticComplexity"]),
        float(request.form["Methods"]),
        float(request.form["Classes"]),
        float(request.form["CBO"]),
        float(request.form["LCOM"]),
        float(request.form["DIT"]),
        float(request.form["RFC"]),
        float(request.form["NOC"]),
        float(request.form["WMC"]),
        float(request.form["CommentRatio"]),
        float(request.form["MaintainabilityIndex"])
    ]]

    prediction = model.predict(features)

    result = encoder.inverse_transform(prediction)

    return render_template(
        "index.html",
        prediction=result[0]
    )


if __name__ == "__main__":
    app.run(debug=True)