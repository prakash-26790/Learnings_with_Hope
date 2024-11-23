import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

salary_data = pd.read_csv("./../Salary_Data.csv")

X = salary_data[["YearsExperience"]]  # Feature: Years of Experience
y = salary_data["Salary"]  # Target: Salary

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R-squared score:", r2)

# Save the model if performance is good
if r2 > 0.8:
    model_filename = "salary_model.sav"
    pickle.dump(regressor, open(model_filename, "wb"))
    print(f"Model saved to {model_filename}")
else:
    print("Skipping., Model is not good. Skipping saving the model")
