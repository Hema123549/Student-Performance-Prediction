# Student Performance Prediction Using Machine Learning

## 📌 Project Overview

Student Performance Prediction Using Machine Learning is a web-based application developed to predict student academic performance based on important academic factors such as Study Hours, Attendance, Assignment Score, and Internal Test Marks.

The project combines Web Development, Data Preprocessing, Feature Engineering, Data Visualization, and Machine Learning to provide an interactive platform for analyzing and predicting student performance.

## 🎯 Objectives

- To analyze student academic performance data.
- To preprocess and clean the dataset.
- To perform Exploratory Data Analysis (EDA).
- To create meaningful features using feature engineering.
- To train machine learning regression models.
- To evaluate and compare the trained models.
- To predict student final exam performance.
- To integrate the machine learning model with a Flask web application.
- To provide an interactive and user-friendly web interface.

## ✨ Features

- Student performance prediction
- Student academic input form
- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Linear Regression
- Decision Tree Regression
- Model evaluation
- Model comparison
- Interactive data visualization
- Flask-based web application
- Prediction result display

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML5
- Tailwind CSS
- JavaScript
- Chart.js

## 📊 Dataset

The project uses a student academic performance dataset containing the following attributes:

- Study Hours
- Attendance Percentage
- Assignment Score
- Internal Test Marks
- Final Exam Score

The dataset was inspected and prepared before using it for machine learning.

## 🔄 Project Workflow

Student / User
        ↓
Frontend HTML Form
        ↓
Flask Controller
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Prediction
        ↓
Web Interface / Dashboard

## 🧹 Data Preprocessing

The dataset was examined and prepared before model training.

The preprocessing stage included:

- Inspecting the dataset
- Checking the data structure
- Checking for missing values
- Preparing input features
- Preparing the target variable
- Splitting the data into training and testing sets

## 🔧 Feature Engineering

Feature engineering was performed to create meaningful features from the existing academic attributes.

### Study Consistency Index

Study Consistency Index = (Study Hours × Attendance) / 100

### Academic Base Score

Academic Base Score =
((Internal Test Marks / 30) × 50)
+
((Assignment Score / 100) × 50)

These engineered features provide additional information about the student's academic consistency and performance.

## 📈 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the relationships between student academic factors and final exam performance.

The project includes:

- Study Hours vs Final Exam Score
- Attendance vs Final Exam Score
- Correlation Heatmap
- Dataset inspection
- Performance analysis charts

Chart.js was used to display interactive visualizations in the web interface.

## 🤖 Machine Learning Models

Two regression models were implemented in the project.

### 1. Linear Regression

Linear Regression was used to identify the relationship between academic input features and the Final Exam Score.

### 2. Decision Tree Regression

Decision Tree Regression was implemented to model relationships between the input features and student performance.

## 📏 Model Evaluation

The models were evaluated using:

- R² Score
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)

### Model Results

| Model | R² Score | RMSE | MAE |
|---|---:|---:|---:|
| Linear Regression | 0.9650 | 2.15 | 1.82 |
| Decision Tree Regression | 0.8920 | 3.84 | 3.10 |

## 🌐 Web Application

The web application was developed using Flask.

The user can enter:

- Daily Study Hours
- Attendance Percentage
- Assignment Score
- Internal Test Marks

The Flask application receives the input, processes the data, and uses the trained machine learning model to generate a prediction.

The result is displayed through the web interface.

## 🏗️ System Architecture

The system follows a Client-Server Architecture.

Client Browser
       ↕
 HTTP Request / Response
       ↕
 Flask Server
       ↕
 Scikit-learn Model
       ↓
 Prediction Result

## 📁 Project Structure

Student-Performance-Prediction/
│
├── README.md
├── requirements.txt
├── student_data.csv
├── train_model.py
├── model.pkl
├── app.py
├── index.html
└── result.html

## 📂 File Description

### train_model.py

Contains the code for:

- Loading the dataset
- Data preprocessing
- Feature engineering
- Splitting the dataset
- Training machine learning models
- Evaluating the models
- Saving the trained model

### app.py

Contains the Flask backend application.

It handles:

- Web requests
- Form inputs
- Prediction processing
- Loading the trained model
- Returning prediction results

### student_data.csv

Contains the student academic dataset used for analysis and machine learning.

### index.html

Provides the main user interface where academic information is entered.

### result.html

Displays the prediction result to the user.

### requirements.txt

Contains the Python libraries required to run the project.

## ▶️ How to Run the Project

### Step 1: Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL

### Step 2: Open the Project Folder

cd Student-Performance-Prediction

### Step 3: Create a Virtual Environment

python -m venv venv

### Step 4: Activate the Virtual Environment

For Windows:

venv\Scripts\activate

### Step 5: Install Required Libraries

pip install -r requirements.txt

### Step 6: Run the Flask Application

python app.py

### Step 7: Open the Application

Open the local Flask URL displayed in the terminal in a web browser.

## 📷 Project Screenshots

### Student Performance Predictor

The application provides an input form for entering student academic details and generating a performance prediction.

### Data Visualization

The application displays charts for analyzing relationships between academic factors and student performance.

### Correlation Heatmap

The correlation heatmap shows the relationship between the features in the dataset.

### Model Evaluation

The application displays R² Score, RMSE, and MAE values for evaluating the machine learning models.

### Model Comparison

The trained Linear Regression and Decision Tree Regression models are compared using evaluation metrics.

## 📋 Sample Prediction

Sample student inputs used in the application include:

- Study Hours: 2.6
- Attendance: 85%
- Assignment Score: 78
- Internal Test Marks: 22

The application processes these values and displays the predicted performance through the web interface.

## 📊 Project Results

The project demonstrates how student academic factors can be analyzed using machine learning techniques and presented through an interactive web application.

The system provides:

- Academic data analysis
- Interactive visualizations
- Feature engineering
- Machine learning model evaluation
- Student performance prediction
- Web-based result presentation

## 🔮 Future Enhancements

- Use a larger real-world student dataset.
- Add additional machine learning algorithms.
- Improve the prediction model using more academic features.
- Add student login and authentication.
- Store prediction history using a database.
- Add personalized performance recommendations.
- Deploy the application on a cloud platform.
- Develop a mobile-friendly version.

## 🎓 Internship Project

This project was developed as part of a 15-Day Internship at Ether Infotech.

The internship provided practical exposure to:

- Web Development
- Python
- Data Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning
- Flask
- Data Visualization

## 👩‍💻 Author

Hema M

Computer Science Undergraduate
Jeppiaar University

---

⭐ Student Performance Prediction Using Machine Learning
