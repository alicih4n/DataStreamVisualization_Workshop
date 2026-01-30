# Robot Maintenance Analysis
### Foundations of Machine Learning Frameworks - Workshop

## 👥 Team
*   **Ali Cihan Ozdemir** (ID: 9091405)
*   **Lohith Reddy** (ID: 9054470)

---

## 🏗 Project Structure
This repository analyzes robot axis currents for predictive maintenance:

```
.
│── data/
│   ├── raw/                 # Raw Robot Maintenance Data
│   ├── processed/           # Cleaned current data (Axis 1-14)
│── notebooks/
│   ├── EDA.ipynb            # Data Cleaning, Time Series & Correlation Analysis
│   ├── linear_regression.ipynb # Modeling Axis relationships (Scratch vs Sklearn)
│── src/                     # Source code modules
│── experiments/
│   ├── results.csv          # RSME Validation results
│── requirements.txt         # Dependencies
│── README.md                # This file
```

---

## 🚀 How to Run

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Run Data Pipeline (EDA)
Open **`notebooks/EDA.ipynb`**.
*   This notebook ingests `robot_maintenance_data.csv`.
*   It filters for "current" traits and handles timestamps.
*   It generates visualizations for axis behavior.

### 3. Run Modeling
Open **`notebooks/linear_regression.ipynb`**.
*   This notebook trains a Linear Regression model.
*   **Objective**: Predict Axis #6 (Wrist) current based on Axis #1 (Base).
*   It compares a "From Scratch" Gradient Descent implementation against Scikit-Learn.

---

## 🧪 Experiments
We check if the current of one axis linearly correlates with another, implying coordinated movement patterns.
Deviations from this linear relationship in real-time could indicate mechanical wear or anomalies.
