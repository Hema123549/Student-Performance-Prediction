import os
import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    print("Warning: 'model.pkl' not found. Please run 'python train_model.py' first.")
    model = None
else:
    model = joblib.load(MODEL_PATH)

def get_performance_grade(score):
    """Categorize score into performance tiers."""
    if score >= 85:
        return "Grade A (Outstanding Performance)", "success", "Excellent work! Keep maintaining your study schedule and active learning habits."
    elif score >= 70:
        return "Grade B (Good Performance)", "info", "Solid performance! A slight increase in study hours could push you into the top tier."
    elif score >= 50:
        return "Grade C (Average Performance)", "warning", "Passing grade, but improvement is recommended. Focus on attendance and internal tests."
    else:
        return "Grade D (Needs Improvement)", "danger", "Action required! Consider increasing daily study time and seeking academic support."

@app.route("/")
def home():
    """Render main input form page."""
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Handle form submission, perform validation, calculation, and prediction."""
    if model is None:
        return render_template("index.html", error_message="Model is not trained yet. Please run train_model.py first.")

    try:
        # Retrieve input values from form
        study_hours = float(request.form.get("study_hours", 0))
        attendance = float(request.form.get("attendance", 0))
        assignment_score = float(request.form.get("assignment_score", 0))
        internal_marks = float(request.form.get("internal_marks", 0))

        # Backend Input Validation
        errors = []
        if not (0 <= study_hours <= 24):
            errors.append("Study Hours must be between 0 and 24 hours.")
        if not (0 <= attendance <= 100):
            errors.append("Attendance must be between 0% and 100%.")
        if not (0 <= assignment_score <= 100):
            errors.append("Assignment Score must be between 0 and 100.")
        if not (0 <= internal_marks <= 30):
            errors.append("Internal Marks must be between 0 and 30.")

        if errors:
            return render_template("index.html", error_message=" ".join(errors))

        # Feature Engineering (Matching train_model.py logic)
        study_consistency = round((study_hours * attendance) / 100.0, 2)
        academic_base = round(((internal_marks / 30.0) * 50.0) + ((assignment_score / 100.0) * 50.0), 2)

        # Prepare feature vector: [Study_Hours, Attendance, Assignment_Score, Internal_Marks, Study_Consistency, Academic_Base]
        features = np.array([[study_hours, attendance, assignment_score, internal_marks, study_consistency, academic_base]])

        # Model Prediction
        prediction_raw = model.predict(features)[0]
        predicted_score = round(float(np.clip(prediction_raw, 0, 100)), 2)

        # Performance categorization
        grade_label, status_class, recommendation = get_performance_grade(predicted_score)

        return render_template(
            "result.html",
            study_hours=study_hours,
            attendance=attendance,
            assignment_score=assignment_score,
            internal_marks=internal_marks,
            study_consistency=study_consistency,
            academic_base=academic_base,
            predicted_score=predicted_score,
            grade_label=grade_label,
            status_class=status_class,
            recommendation=recommendation
        )

    except ValueError:
        return render_template("index.html", error_message="Invalid input values detected. Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
