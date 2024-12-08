import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score

"""
Summary:
1. Load the dataset.
2. Convert categorical columns into numeric representations (one-hot encoding).
3. Identify input (independent) and output (dependent) variables.
4. Split the dataset into training and testing subsets.
5. Standardize the input features.
6. Train an SVR model.
7. Make predictions.
8. Evaluate the predictions using the R² score.
"""

# Step 1: Load the dataset
dataset = pd.read_csv("./../../50_Startups.csv")

# Step 2: Convert categorical columns to numeric values (one-hot encoding)
dataset = pd.get_dummies(dataset, drop_first=True)

# Step 3: Define input (independent) and output (dependent) variables
X = dataset[['R&D Spend', 'Administration', 'Marketing Spend', 'State_Florida', 'State_New York']]
y = dataset['Profit']

# Step 4: Split the dataset into training and testing subsets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Step 5: Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

kernel_arguments = ["linear", "poly", "rbf", "sigmoid"]
hyper_params = [0.01, 0.1, 1, 10, 100, 1000, 5000]

for index in range(len(hyper_params)):
    all_value = ""
    for kernel in kernel_arguments:
        # Step 6: Train an SVR model with an RBF kernel
        svr_model = SVR(kernel=kernel, C=hyper_params[index])
        svr_model.fit(X_train, y_train)

        y_pred = svr_model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        # print(f"===> R² Score for {kernel} : {r2:.5f}")
        all_value += f"{r2:.5f}" + " | "
    print("| " + str(index + 1) + " | " + str(hyper_params[index]) + " | " + all_value)