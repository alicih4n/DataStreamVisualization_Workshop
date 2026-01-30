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
│   ├── raw/                 # Original immutable data (California Housing)
│   ├── processed/           # Cleaned data ready for modeling
│── notebooks/
│   ├── EDA.ipynb            # Exploratory Data Analysis & Data Sourcing
│   ├── linear_regression.ipynb # Model training & comparison (Scratch vs Scikit-Learn)
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
Ensure you have Python 3.9+ installed.

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Experiment
Edit `configs/experiment_config.yaml` to change hyperparameters:
- `learning_rate`: Step size for Gradient Descent.
- `iterations`: Number of training loops.
- `feature_column`: The feature to use for univariate regression (e.g., `MedInc`).

### 3. Run Notebooks
Start Jupyter Lab or Notebook:
```bash
jupyter lab
```

1.  Open **`notebooks/EDA.ipynb`** to explore the dataset.
2.  Open **`notebooks/linear_regression.ipynb`** to train the model and see the validation visualization.

---

## 🧪 Experiment Results
We compare our **"From Scratch"** implementation against `scikit-learn` to validate correctness.

*   **Metric**: Root Mean Squared Error (RMSE) on Test Set (20% split).
*   **Target**: Median House Value (`MedHouseVal`).
*   **Feature**: Median Income (`MedInc`).

*(Results will be populated in `experiments/results.csv` after running the notebook.)*
