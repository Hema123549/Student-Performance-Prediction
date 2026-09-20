import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ---------------------------------------------------------
# Step 1: Load or Generate Dataset
# ---------------------------------------------------------
csv_path = "student_data.csv"

if os.path.exists(csv_path):
    print(f"Loading existing dataset from {csv_path}...")
    df = pd.read_csv(csv_path)
else:
    print("Dataset file not found. Generating sample student data...")
    np.random.seed(42)
    n_samples = 100
    
    study_hours = np.random.uniform(1.0, 10.0, n_samples)
    attendance = np.random.uniform(50.0, 100.0, n_samples)
    assignment_score = np.random.uniform(40.0, 100.0, n_samples)
    internal_marks = np.random.uniform(8.0, 30.0, n_samples)
    
    final_score = (
        (study_hours * 4.5) +
        (attendance * 0.25) +
        (assignment_score * 0.20) +
        (internal_marks * 0.80) +
        np.random.normal(0, 3, n_samples)
    )
    final_score = np.clip(final_score, 0, 100)
    
    df = pd.DataFrame({
        'Study_Hours': np.round(study_hours, 1),
        'Attendance': np.round(attendance, 1),
        'Assignment_Score': np.round(assignment_score, 1),
        'Internal_Marks': np.round(internal_marks, 1),
        'Final_Exam_Score': np.round(final_score, 1)
    })
    df.to_csv(csv_path, index=False)
    print(f"Dataset generated and saved to {csv_path}.")

# ---------------------------------------------------------
# Step 2: Data Preprocessing & Cleaning
# ---------------------------------------------------------
df = df.dropna().drop_duplicates()

# ---------------------------------------------------------
# Step 3: Feature Engineering
# ---------------------------------------------------------
# Feature 1: Study Consistency Index
df['Study_Consistency'] = np.round((df['Study_Hours'] * df['Attendance']) / 100.0, 2)

# Feature 2: Academic Base Score
df['Academic_Base'] = np.round(((df['Internal_Marks'] / 30.0) * 50.0) + ((df['Assignment_Score'] / 100.0) * 50.0), 2)

# ---------------------------------------------------------
# Step 4: Model Training & Evaluation
# ---------------------------------------------------------
X = df[['Study_Hours', 'Attendance', 'Assignment_Score', 'Internal_Marks', 'Study_Consistency', 'Academic_Base']]
y = df['Final_Exam_Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_preds = lr_model.predict(X_test)
lr_r2 = r2_score(y_test, lr_preds)

# Model 2: Decision Tree Regressor
dt_model = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)
dt_r2 = r2_score(y_test, dt_preds)

# Select best model
selected_model = lr_model if lr_r2 >= dt_r2 else dt_model

# ---------------------------------------------------------
# Step 5: Save Trained Model
# ---------------------------------------------------------
joblib.dump(selected_model, "model.pkl")
print("✅ Machine Learning Model successfully trained and saved as 'model.pkl'!")