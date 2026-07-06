 
from flask import Flask, render_template, request
import joblib

 
app = Flask(__name__)

 
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html", prediction_text=None)

@app.route("/predict", methods=["POST"])
def predict():
     
        area = float(request.form["Area"])
        bedrooms = int(request.form["Bedrooms"])
        bathrooms = int(request.form["Bathrooms"])
        house_age = int(request.form["House_Age"])
        location_score = float(request.form["Location_Score"])

 
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
     app.run(debug=True) # apne laptop me ruk krne ke liye 
  # app.run(host="0.0.0.0", port=5000, debug=True)  #dusare ip me run krne ke liye
