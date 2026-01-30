
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import sqlite3
import os

def bootstrap_data():
    print("Bootstrapping data...")
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

    # 1. California Data
    print("Fetching California housing data...")
    california = fetch_california_housing(as_frame=True)
    df_cal = california.frame
    df_cal.to_csv('data/raw/california_housing.csv', index=False)
    print(f"Saved California data: {df_cal.shape}")

    # 2. Synthetic Ontario Data
    print("Generating synthetic Ontario housing data...")
    np.random.seed(42)
    n_samples = 1000
    sqft = np.random.normal(1500, 500, n_samples).astype(int)
    sqft = sqft[sqft > 300]
    price = 150000 + 400 * sqft + np.random.normal(0, 50000, len(sqft))
    df_on = pd.DataFrame({'Size_sqft': sqft, 'Price_CAD': price})
    df_on.to_csv('data/raw/ontario_housing.csv', index=False)
    print(f"Saved Ontario data: {df_on.shape}")

    # 3. Database
    print("Populating SQLite database...")
    conn = sqlite3.connect('data/housing.db')
    df_cal.to_sql('california_housing', conn, if_exists='replace', index=False)
    df_on.to_sql('ontario_housing', conn, if_exists='replace', index=False)
    conn.close()
    print("Database populated: data/housing.db")

if __name__ == "__main__":
    bootstrap_data()
