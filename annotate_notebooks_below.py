import nbformat as nbf

# Function to insert markdown explanations BELOW the corresponding code cells.
def annotate_notebook_below(path, annotation_map):
    ntbk = nbf.read(path, nbf.NO_CONVERT)
    new_cells = []
    
    for cell in ntbk.cells:
        # Append the current cell first
        new_cells.append(cell)
        
        # If it's a code cell, check if we need to explain it below
        if cell.cell_type == "code":
            for signature, explanation in annotation_map.items():
                if signature in cell.source:
                    md_content = f"**📝 Explanation:**\n{explanation}"
                    md_cell = nbf.v4.new_markdown_cell(md_content)
                    new_cells.append(md_cell)
                    break 
            
    ntbk.cells = new_cells
    nbf.write(ntbk, path)
    print(f"Annotated {path} with explanations BELOW code cells.")

# --- EDA Annotations (Robot Context) ---
eda_map = {
    "import pandas as pd": "We check the environment imports. Key libraries include `pandas` for handling the robot CSV data and `matplotlib` for visualizing the current waveforms.",
    "pd.read_csv": "We load the raw maintenance data. We also parse the `Time` column to datetime objects to enable time-series analysis and filter specifically for `current` traits, as current spikes are key indicators of load.",
    "plt.plot": "We visualize `Axis #1` current over time. This helps us see the duty cycle of the robot and identify any obvious outliers or periods of inactivity.",
    "df_current[axis_cols].corr()": "We generate a correlation matrix between all axes. High correlation suggests axes moving together (synergy), which is useful for selecting features for our regression model."
}

# --- Linear Regression Annotations (Robot Context) ---
lr_map = {
    "import pandas as pd": "We load the pre-processed robot data. We use `train_test_split` to create a training set for the model to learn from and a test set to validate its predictions on unseen robot cycles.",
    "X = df[['Axis #1']].values": "We select our variables. We treat `Axis #1` (Base) as the independent variable X, and `Axis #6` (Wrist) as the dependent variable y, assuming a mechanical coupling or coordinated task relationship.",
    "class LinearRegressionScratch": "We build the Linear Regression logic from scratch. The `fit` method uses Gradient Descent to find the optimal line $y = wx + b$ that best describes the relationship between the two axes' currents.",
    "plt.plot(model_scratch.cost_history)": "We inspect the learning process. The Cost History graph shows us how the error decreased over 2000 iterations, confirming the model converged to a solution.",
    "LinearRegression()": "We train a reference `Scikit-Learn` model. This allows us to verify that our `scratch` calculation is performing correctly and yielding accurate weights.",
    "plt.scatter(X_test": "We visualize the predictions. The scatter plot shows the actual current readings (Blue) vs our model predictions (Red/Green lines). The tight alignment confirms a linear relationship exists.",
    "results.to_csv": "We save the Root Mean Squared Error (RMSE) to a persistent CSV file in the `experiments` folder for reporting and tracking model performance."
}

annotate_notebook_below("notebooks/EDA.ipynb", eda_map)
annotate_notebook_below("notebooks/linear_regression.ipynb", lr_map)
