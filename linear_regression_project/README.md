# Linear Regression Architecture Workshop

## Student Project Submission
This repository contains my implementation of the **Linear Regression Architecture Workshop**. The project structures univariate linear regression analysis into a modular, production-ready MLOps pipeline.

## 📂 Project Structure
```
LinearRegression_Submission/
│── data/
│   ├── raw/                  # Data sourced from sklearn/synthetic generation
│   ├── housing.db            # SQLite database
│── notebooks/
│   ├── Data_Sourcing.ipynb            # Data extraction & EDA
│   ├── Linear_Regression_Training.ipynb # Model experiments (Scratch vs Scikit-Learn)
│── src/
│   ├── data_loader.py        # CSV/DB loading logic
│   ├── preprocessing.py      # Feature scaling & splitting
│   ├── model.py              # Regression model classes
│   ├── evaluation.py         # Metrics calculation
│── configs/
│   ├── experiment_config.yaml # Run configuration
│── experiments/
│   ├── results.csv           # Automatic experiment logging
│── main.py                   # Pipeline entry point
│── requirements.txt          # Dependencies
│── README.md
```

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the MLOps Pipeline
This will load data, train the model defined in `configs/experiment_config.yaml`, and log results.
```bash
python main.py
```

## 🔍 Implementation Details
*   **Data**: California Housing (Real) + Ontario Housing (Synthetic/Simulated).
*   **Models**: Implemented Gradient Descent from scratch to verify understanding, benchmarked against Scikit-Learn.
*   **Architecture**: Fully modularized code in `src/` to ensure reproducibility.
