## Assignment-Regression Algorithm

### 1. Identify your problem statement

Stage 1: The majority of datasets contain numerical data, so **Machine Learning**.  
Stage 2: the features and labels are structured, so it falls under **Supervision learning**.  
Stage 3: The output is based on continuous numerical value so **Regression**.

### 2. Tell basic info about the dataset (Total number of rows, columns)

Total number of rows: 1338<br>
Total number of columns: 6<br>
Feature(input) fields: age,sex,bmi,children,smoker<br>
Label(output): charges<br>


### 3. Mention the pre-processing method if you’re doing any (like converting string to number – nominal data)

Pre-processing step is needed for convert the fields sex and smoker columns.


### 4. Develop a good model with r2_score. You can use any machine learning algorithm; you can create many models. Finally, you have to come up with final model.

All model codes are stored in this directory

### 5. All the research values (r2_score of the models) should be documented. (You can make tabulation or screenshot of the results.)

#### Multiple Linear Regression
- **R² Value**: 0.78948

#### Support Vector Machine(R² value)

| S.No | hyper param | linear | poly | rbf | sigmoid |
|------|-------------|--------|------|-----|---------|
| 1 | 0.01 | -0.08883 | -0.08957 | -0.08965 | -0.08957 | 
| 2 | 0.1 | -0.08096 | -0.08830 | -0.08907 | -0.08827 | 
| 3 | 1 | -0.01010 | -0.07570 | -0.08338 | -0.07543 | 
| 4 | 10 | 0.46247 | 0.03872 | -0.03227 | 0.03931 | 
| 5 | 100 | 0.62888 | 0.61796 | 0.32003 | 0.52761 | 
| 6 | 1000 | 0.76493 | 0.85665 | 0.81021 | 0.28747 | 
| 7 | 5000 | 0.74142 | 0.85957 | **0.87478** | -7.53004 | 

#### Decision Tree(R² value)

| S.No | criterion | splitter | R2 Value |
|------|------------|----------|----------|
| 1 | squared_error | best | 0.69572 | 
| 2	| squared_error | random | 0.72102 | 
| 3	| friedman_mse | best | 0.71152 | 
| 4	| friedman_mse | random | 0.71408 | 
| 5	| absolute_error | best | 0.66807 | 
| 6	| absolute_error | random | **0.75063** | 
| 7	| poisson | best | 0.72882 | 
| 8	| poisson | random | 0.70195 | 

#### Random Forest (R² value)

| S.No | criterion | n_estimators | R2 Value |
|------|------------|----------|----------|
| 1 | squared_error | 10 | 0.83303 | 
| 2 | squared_error | 50 | 0.84983 | 
| 3 | squared_error | 100 | 0.85383 | 
| 4 | absolute_error | 10 | 0.83506 | 
| 5 | absolute_error | 50 | 0.85267 | 
| 6 | absolute_error | 100 | 0.85201 | 
| 7 | friedman_mse | 10 | 0.83317 | 
| 8 | friedman_mse | 50 | 0.85007 | 
| 9 | friedman_mse | 100 | **0.85405** | 
| 10 | poisson | 10 | 0.83140 | 
| 11 | poisson | 50 | 0.84911 | 
| 12 | poisson | 100 | 0.85263 |


### 6. Mention your final model, justify why u have chosen the same.

Based on the above analysis, the Support Vector Machine with a hyperparameter value of 5000 and the RBF kernel provides the best model prediction.
