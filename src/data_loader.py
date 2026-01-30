
import pandas as pd
import sqlite3
import os

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_csv(self, filename):
        """Loads data from a CSV file."""
        file_path = os.path.join(self.data_path, 'raw', filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return pd.read_csv(file_path)

    def load_db(self, db_name, table_name):
        """Loads data from a SQLite database table."""
        db_path = os.path.join(self.data_path, db_name)
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database not found: {db_path}")
        
        conn = sqlite3.connect(db_path)
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, conn)
        conn.close()
        return df

if __name__ == "__main__":
    # Test
    loader = DataLoader('data')
    try:
        df = loader.load_csv('california_housing.csv')
        print(f"Loaded CSV: {df.shape}")
    except Exception as e:
        print(e)
