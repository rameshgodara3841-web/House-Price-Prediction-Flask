# from flask import Flask, app
# import joblib

# from flast import Flast ,requesst rede
# data = joblib.load('model.pkl')

# data = joblib.load('model.pkl')

# app = Flask(__name__)

# @app.route("/")
# def predict():
#     prediction = data.predict([[1, 2, 3, 4]]) 
#     result = prediction[0]
#     if(result>100):
#         prediction = 100
#         print ("prediction ")


from flask import Flask, render_template, request
import joblib

# Flask App
app = Flask(__name__)

# Load Trained Model
model = joblib.load("model.pkl")


# Home Page
@app.route("/")
def home():
    return render_template("index.html", prediction_text=None)


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get Form Data
        area = float(request.form["Area"])
        bedrooms = int(request.form["Bedrooms"])
        bathrooms = int(request.form["Bathrooms"])
        house_age = int(request.form["House_Age"])
        location_score = float(request.form["Location_Score"])

        # Prediction
        prediction = model.predict([
            [area, bedrooms, bathrooms, house_age, location_score]
        ])

        predicted_price = prediction[0]

        return render_template(
            "index.html",
            prediction_text=f"🏠 Estimated House Price: ₹ {predicted_price:,.2f}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"❌ Error: {str(e)}"
        )


# Run Flask App
if __name__ == "__main__":
    # app.run(debug=True)
  app.run(host="0.0.0.0", port=5000, debug=True)