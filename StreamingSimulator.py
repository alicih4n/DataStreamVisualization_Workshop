import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import time

class StreamingSimulator:
    def __init__(self, csv_paths, db_connection_string='sqlite:///robot_maintenance.db'):
        """
        Initialize the StreamingSimulator.
        
        :param csv_paths: Path to the CSV file or list of paths.
        :param db_connection_string: SQLAlchemy connection string. Defaults to local SQLite.
        """
        if isinstance(csv_paths, str):
            self.csv_paths = [csv_paths]
        else:
            self.csv_paths = csv_paths
            
        self.db_engine = create_engine(db_connection_string)
        self.data_frame = self._load_data()
        self.current_index = 0
        
        # Initialize Database
        self._init_db()

    def _load_data(self):
        """Loads data from CSV files into a single DataFrame."""
        dfs = []
        for path in self.csv_paths:
            try:
                # Read CSV, assuming standard format from workshop
                df = pd.read_csv(path)
                dfs.append(df)
            except Exception as e:
                print(f"Error reading {path}: {e}")
        
        if not dfs:
            raise ValueError("No data could be loaded.")
            
        combined_df = pd.concat(dfs, ignore_index=True)
        # Sort by time if 'Time' column exists
        if 'Time' in combined_df.columns:
            combined_df['Time'] = pd.to_datetime(combined_df['Time'])
            combined_df = combined_df.sort_values('Time')
            
        return combined_df

    def _init_db(self):
        """Initializes the database table."""
        # Simple schema based on the CSV structure: Trait, axes, Time
        # We'll infer types or use a generic structure. 
        # For simplicity in this workshop, we can let to_sql create the table, 
        # but defining a schema is better practice.
        # However, to be dynamic to the CSV, we'll let pandas notify us.
        pass

    def nextDataPoint(self):
        """
        Generator that yields the next record from the dataframe.
        Simulates streaming by returning one record at a time.
        """
        total_records = len(self.data_frame)
        
        while self.current_index < total_records:
            record = self.data_frame.iloc[self.current_index]
            self.current_index += 1
            yield record

    def save_to_db(self, record, table_name='robot_data'):
        """
        Saves a single record to the database.
        
        :param record: A pandas Series or dictionary representing the row.
        :param table_name: The table to insert into.
        """
        # Convert Series to DataFrame to use to_sql
        df = pd.DataFrame([record])
        df.to_sql(table_name, self.db_engine, if_exists='append', index=False)
        return True

    def get_data_from_db(self, query="SELECT * FROM robot_data"):
        """Retrieves data from the database."""
        return pd.read_sql(query, self.db_engine)
