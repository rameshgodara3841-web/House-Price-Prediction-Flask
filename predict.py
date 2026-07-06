import joblib
model = joblib.load("model.pkl")

house_info = [[3000, 2,4 , 1,5]]  

prediction = model.predict(house_info)

result = prediction[0]

print("Prediction is :",result)