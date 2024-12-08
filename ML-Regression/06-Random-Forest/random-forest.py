import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import pickle

"""
Summary:
1. Load the dataset.
2. Convert categorical columns into numeric representations (one-hot encoding).
3. Define input (independent) and output (dependent) variables.
4. Split the dataset into training and testing subsets (70% training, 30% testing).
5. Train a Random Forest Regressor model.
6. Make predictions on the test data.
7. Evaluate the model using the R² score.
"""

# Step 1: Load the dataset
dataset = pd.read_csv("./../50_Startups.csv")

# Step 2: Convert categorical columns to numeric values (one-hot encoding)
dataset = pd.get_dummies(dataset, drop_first=True)

# Step 3: Define input (independent) and output (dependent) variables
independent = dataset[['R&D Spend', 'Administration', 'Marketing Spend', 'State_Florida', 'State_New York']]
dependent = dataset[['Profit']]

# Step 4: Split the dataset into training and testing subsets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(independent, dependent, test_size=0.3, random_state=0)

# Use ravel to flatten the dependent variable (y_train and y_test)
y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

criterions = ["squared_error", "absolute_error", "friedman_mse", "poisson"]
n_estimators = [10, 50, 100]

for index in range(len(criterions)):
    for n_estimator in n_estimators:
        # Step 5: Train the Random Forest Regressor
        regressor = RandomForestRegressor(n_estimators=n_estimator, criterion=criterions[index], random_state=0)
        regressor.fit(X_train, y_train)

        # Step 6: Make predictions
        y_pred = regressor.predict(X_test)

        # Step 7: Evaluate the model using the R² score
        r2 = r2_score(y_test, y_pred)
        # Print the result for each combination
        print(" | " + criterions[index] + " | " + str(n_estimator) + " | " + f"{r2:.5f}")
        
        threshold = 0.946
        if r2 > threshold:
            filename = f"random-forest-{r2:.5f}.sav"
            pickle.dump(regressor, open(filename, "wb"))
            print(f"Model saved: {filename}")
