 import pandas as pd
import random

data = []

for i in range(1, 10001):

    Area = random.randint(1, 10000)
    Bedrooms = random.randint(1, 5)
    Bathrooms = random.randint(1, 4)
    House_Age = random.randint(1, 50)
    Location_Score = random.uniform(1, 10)

    price = (
        Area * 500 +
        Bedrooms * 10000 +
        Bathrooms * 1500 +
        House_Age * 5000 +
        Location_Score * 10000
    )

    data.append([Area, Bedrooms, Bathrooms, House_Age, Location_Score, price])

df = pd.DataFrame(data, columns=[
    "Area", "Bedrooms", "Bathrooms", "House_Age", "Location_Score", "Price"
])

df.to_csv("house_data.csv", index=False)

print("Rows generated:", len(df))
