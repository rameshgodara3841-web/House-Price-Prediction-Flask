# from pyexpat import model

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# df =pd.read_csv("data\house_price_dataset.csv")
df = pd.read_csv("house_data.csv" )
print(df.isnull().sum())

print(df.duplicated().sum())
print(df.head())
  
print(df.columns)
X= df.drop("Price", axis=1)
Y= df["Price"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

 
print("Training Data :", X_train.shape)
print("Testing Data :", X_test.shape)

model  = LinearRegression()

model.fit(X_train, Y_train)

print("model is trained")
Y_pred = model.predict(X_test)

print(Y_pred[:10])

print(Y_test.head(10))
 
mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
rmse = mse ** 0.5
 
score = r2_score(Y_test, Y_pred)

print("r2_score is :",score)
print("model is predicted successfully ")

joblib.dump(model, "model.pkl")

print("model is saved successfully")