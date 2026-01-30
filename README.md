# Linear Regression Architecture Workshop
### Foundations of Machine Learning Frameworks - Workshop

## 👥 Team
*   Group 2

---

## 🏗 Project Structure
This repository is organized to ensure modularity, reproducibility, and ease of evaluation:

```
.
│── data/
│   ├── raw/                 # Original immutable data (California Housing, Ontario Synthetic)
│   ├── processed/           # Cleaned data ready for modeling
│── notebooks/
│   ├── EDA.ipynb            # Data Sourcing & Exploratory Data Analysis (Run this FIRST)
│   ├── linear_regression.ipynb # Model training, evaluation & comparison (Scratch vs Scikit-Learn)
│   ├── RobotPM_MLOps.ipynb  # MLOps architecture & Orchestration Design
│── src/                     # Source code for reproducibility
│   ├── data_loader.py       # Functions to load data
│   ├── preprocessing.py     # Scaling and feature selection
│   ├── model.py             # Linear Regression class (Gradient Descent)
│   ├── evaluation.py        # Metrics calculation (RMSE, R2)
│── configs/
│   ├── experiment_config.yaml # Hyperparameters (learning rate, iterations)
│── experiments/
│   ├── results.csv          # Logged metrics from runs
│── requirements.txt         # Dependencies
│── README.md                # This file
```

---

## 🚀 How to Run

### 1. Setup Environment
Ensure you have Python 3.9+ installed and a virtual environment active (recommended).

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Data Pipeline (Critical)
You **must** run the EDA notebook first to generate the raw datasets.

1.  Start Jupyter:
    ```bash
    jupyter lab
    ```
2.  Open **`notebooks/EDA.ipynb`**.
    *   Run all cells.
    *   This will download California Housing data and generate synthetic Ontario data in `data/raw/`.

### 3. Run Experiments
Open **`notebooks/linear_regression.ipynb`**.
*   Run all cells.
*   This will:
    1.  Load the data generated in Step 2.
    2.  Train a Linear Regression model from scratch (Gradient Descent).
    3.  Train a Scikit-Learn baseline.
    4.  Compare the results and plot the regression line.
    5.  Save metrics to `experiments/results.csv`.

### 4. Explore MLOps Architecture
Open **`notebooks/RobotPM_MLOps.ipynb`**.
*   This notebook demonstrates the object-oriented architecture for a robust ML pipeline.

---

## 🧪 Verified Results
After running `linear_regression.ipynb`, check `experiments/results.csv`. You should see results similar to:

```csv
Model,RMSE
Linear Regression (Scratch),0.8421
Linear Regression (Sklearn),0.8421
```

*   **Target**: Median House Value (`MedHouseVal`)
*   **Feature**: Median Income (`MedInc`)
