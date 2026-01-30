import nbformat as nbf

# Function to insert markdown before code cells containing specific signatures
def annotate_notebook(path, annotation_map):
    ntbk = nbf.read(path, nbf.NO_CONVERT)
    new_cells = []
    
    for cell in ntbk.cells:
        if cell.cell_type == "code":
            # Check if this cell matches any annotation signature
            inserted = False
            for signature, explanation in annotation_map.items():
                if signature in cell.source:
                    # Create markdown cell
                    md_cell = nbf.v4.new_markdown_cell(explanation)
                    new_cells.append(md_cell)
                    # Remove from map to avoid duplicate insertions if signatures repeat (unlikely here)
                    # annotation_map.pop(signature) 
                    inserted = True
                    break # Only one explanation per cell
            
            new_cells.append(cell)
        else:
            new_cells.append(cell)
    
    ntbk.cells = new_cells
    nbf.write(ntbk, path)
    print(f"Annotated {path}")

# --- EDA Annotations ---
eda_map = {
    "import pandas as pd": "### 🛠 Setup & Imports\nWe import essential libraries: `pandas` for dataframes, `numpy` for math, `matplotlib`/`seaborn` for plotting, and `sqlite3` for database interactions. We also ensure the directory structure exists.",
    "fetch_california_housing": "### 📥 Data Loading (California)\nWe fetch the California Housing dataset directly from `sklearn`. This is a classic dataset used for regression tasks. We convert it to a DataFrame and save the raw version.",
    "sns.histplot": "### 📊 Distribution Analysis\nWe visualize the target variable `MedHouseVal` using a histogram. This helps us understand the data distribution and identify any skewness or outliers.",
    "np.random.normal(1500": "### 🎲 Synthetic Data Generation (Ontario)\nSince a direct clear API for Ontario housing is not available, we generate a synthetic dataset mimicking real-world properties (Size vs Price) to simulate a local dataset.",
    "sns.scatterplot": "### 📈 Relationship Visualization\nWe plot Size vs Price for the Ontario dataset to confirm the linear relationship we simulated.",
    "import requests": "### 🌐 API Data Sourcing\nDemonstration of how to fetch data from a REST API. We retrieve a sample JSON file (users) to showcase real-world data ingestion patterns."
}

# --- Linear Regression Annotations ---
lr_map = {
    "import pandas as pd": "### 🛠 Setup & Data Loading\nWe load the processed California housing data. We split the data into Training (80%) and Test (20%) sets using `train_test_split` to ensure fair evaluation.",
    "X = df[['MedInc']].values": "### 🔍 Feature Selection\nWe select `Median Income` as our independent variable (X) to predict `Median House Value` (y). We verify the shapes of our arrays.",
    "class LinearRegressionScratch": "### 🧠 Custom Linear Regression Implementation\nWe define a class `LinearRegressionScratch` that implements Gradient Descent manually.\n- `fit()`: Iteratively updates weights and bias to minimize error.\n- `predict()`: Computes outputs based on current weights.\n- `compute_cost()`: Calculates Mean Squared Error.",
    "plt.plot(model_scratch.cost_history)": "### 📉 Training Convergence\nWe plot the Cost (Error) vs Iterations. A decreasing curve confirms that Gradient Descent is working correctly and converging to a minimum.",
    "LinearRegression()": "### 📚 Scikit-Learn Implementation\nWe train the standard `LinearRegression` model from `sklearn`. This serves as a ground truth baseline to validate our custom implementation.",
    "plt.scatter(X_test": "### 📊 Model Comparison & Visualization\nWe visually compare the regression lines from both models against the actual test data. Overlapping lines indicate our custom implementation is accurate.",
    "Weights (Scratch)": "### 🔢 Numerical Comparison\nWe compare the learned Weights and Bias of both models. Closer values imply a correct implementation.",
    "results.to_csv": "### 💾 Result Logging\nWe create a DataFrame of our metrics (RMSE) and examine them, saving the final performance report to `experiments/results.csv`."
}

annotate_notebook("notebooks/EDA.ipynb", eda_map)
annotate_notebook("notebooks/linear_regression.ipynb", lr_map)
