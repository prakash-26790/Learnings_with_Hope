import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataset = pd.read_csv("./insurance_pre.csv")
dataset = pd.get_dummies(dataset, drop_first=True)

# print(dataset.columns)

independent = dataset[['age', 'bmi', 'children', 'sex_male', 'smoker_yes']]
dependent = dataset['charges']

X_train, X_test, y_train, y_test = train_test_split(independent, dependent, test_size=0.30, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R-squared score:", r2)

# Save the model if performance is good
if r2 > 0.95:
    model_filename = "insurance_model.sav"
    pickle.dump(regressor, open(model_filename, "wb"))
    print(f"Model saved to {model_filename}")
else:
    print("Skipping., Model is not good. Skipping saving the model")
