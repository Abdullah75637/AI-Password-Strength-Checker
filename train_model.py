import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("passwords.csv")

X = data[["length","upper","lower","digit","special"]]
y = data["strength"]

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"password_model.pkl")

print("Model Trained Successfully")