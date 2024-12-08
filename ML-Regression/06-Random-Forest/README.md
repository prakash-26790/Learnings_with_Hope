## Assessment

### Multiple Linear Regression
- **R² Value**: 0.93587

### Support Vector Machine(R² value)

| S.No | hyper param | linear | poly | rbf | sigmoid |
|------|-------------|--------|------|-----|---------|
| 1 | 0.01 | -0.05747 | -0.05748 | -0.05749 | -0.05748 | 
| 2 | 0.1 | -0.05731 | -0.05745 | -0.05748 | -0.05746 | 
| 3 | 1 | -0.05569 | -0.05710 | -0.05742 | -0.05721 | 
| 4 | 10 | -0.03964 | -0.05367 | -0.05681 | -0.05472 | 
| 5 | 100 | 0.10647 | -0.01980 | -0.05073 | -0.03045 | 
| 6 | 1000 | 0.78028 | 0.26616 | 0.00677 | 0.18507 | 
| 7 | 5000 | 0.90038 | 0.79366 | 0.21243 | 0.73066 |


### Decision Tree(R² value)

| S.No | criterion | splitter | R2 Value |
|------|------------|----------|----------|
| 1 | squared_error | best | 0.9329619149785955 |
| 2	| squared_error | random | 0.7275543084642946 |
| 3	| friedman_mse | best | 0.8930106646150924 |
| 4	| friedman_mse | random | 0.6594027108860068 |
| 5	| absolute_error | best | 0.9329619149785955 |
| 6	| absolute_error | random | 0.7275543084642946 |
| 7	| poisson | best | 0.9134158431589564 |
| 8	| poisson | random | 0.6594027108860068 |


### Random Forest (R² value)

| S.No | criterion | n_estimators | R2 Value |
|------|------------|----------|----------|
| 1 | squared_error | 10 | 0.92528 |
| 2 | squared_error | 50 | 0.94463 |
| 3 | squared_error | 100 | 0.94600 |
| 4 | absolute_error | 10 | 0.92818 |
| 5 | absolute_error | 50 | 0.94019 |
| 6 | absolute_error | 100 | 0.94591 |
| 7 | friedman_mse | 10 | 0.92067 |
| 8 | friedman_mse | 50 | 0.93890 |
| 9 | friedman_mse | 100 | 0.94127 |
| 10 | poisson | 10 | 0.93049 |
| 11 | poisson | 50 | 0.94635 |
| 12 | poisson | 100 | 0.94139 |
