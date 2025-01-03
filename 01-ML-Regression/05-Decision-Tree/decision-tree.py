import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor

"""
Summary:
1. Load the dataset.
2. Convert categorical columns into numeric representations (one-hot encoding).
3. Define input (independent) and output (dependent) variables.
4. Split the dataset into training and testing subsets (70% training, 30% testing).
5. Train a Decision Tree Regressor model.
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

# Step 5: Train the Decision Tree Regressor
regressor = DecisionTreeRegressor(criterion='poisson', splitter='random', random_state=0)
regressor.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = regressor.predict(X_test)

# Step 7: Evaluate the model using the R² score
r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2}")
