# Employee Resignation Prediction System

## Assignment  
A company works with a number of employees, and all the work depends on them. If even one of the employees resigns immediately, the assigned work will not be finished on time, leading to delays in project delivery to clients. To address this, the company wants to predict which employee may resign this month or next. If they know this in advance, they can arrange alternatives to avoid such problems. As an AI Engineer, you must provide a solution.

---

### A) How will you achieve this in AI?
- This problem involves both prediction and call-to-action. Predicting employee resignation is the main task, while the call-to-action involves alerting management to take alternative actions if an employee is predicted to resign.
- To predict resignation, we need to collect relevant employee data, such as past and current technical performance, historical resignation records, feedback from performance reviews, job-related details, attendance, salary information, and more.
- This data will be fed into a machine learning model. The model will analyze the data and predict whether an employee is likely to resign or not.
- Based on the model's predictions, a call-to-action can trigger alerts for management to take necessary steps, such as arranging replacements or addressing employee concerns.

---

### B) Find out the 3-Stage of Problem Identification
1. **Stage 1**: Mostly the datasets contain numerical data, so **Machine Learning** is the model type that we can approach.  
2. **Stage 2**: It is a **Supervision learning** type because input and label are structured.  
3. **Stage 3**: **Classification**: The output is a Categorical Value—either the employee will resign or will not resign.

---

### C) Name the project
**Employee Resignation Prediction System**

---

### D) Create the dummy Dataset
| Emp ID | Department | Role          | Experience (current) | Total Exp | Job satisfaction Feedback (10) | Performance Rating (10) | Salary (month) | Last Hike (%) | Age | Resigned? |
|--------|------------|---------------|-----------------------|-----------|----------------------------------|--------------------------|----------------|---------------|-----|-----------|
| 1      | IT         | Developer     | 2                     | 5         | 4                                | 5                        | 90k            | 4             | 28  |           |
| 2      | IT         | QA            | 2                     | 9         | 8                                | 9                        | 120k           | 20            | 33  |           |
| 3      | Sales      | Sales Lead    | 5                     | 13        | 6                                | 8                        | 110k           | 12            | 36  |           |
| 4      | HR         | Recruiter     | 1                     | 4         | 5                                | 4                        | 50k            | 6             | 27  |           |
| 5      | Sales      | Executive     | 6                     | 8         | 4                                | 5                        | 95k            | 15            | 31  |           |
| 6      | IT         | Manager       | 15                    | 15        | 6                                | 5                        | 250k           | 3             | 40  |           |

This dataset will serve as input for the ML model to predict which employees are at risk of resigning, based on factors such as job satisfaction feedback, performance, age, and more.
