import os
import pandas as pd
from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, db_name='assignment.db', db_dir='data'):
        self.db_path = os.path.join(db_dir, db_name)
        self.engine = create_engine(f"sqlite:///{self.db_path}")

    def save_to_table(self, df: pd.DataFrame, table_name: str):
        """Save DataFrame to a table (replaces existing if exists)"""
        df.to_sql(table_name, self.engine, index=False, if_exists='replace')
        print(f"[INF] Data saved to table: {table_name}")

    def load_table(self, table_name: str) -> pd.DataFrame:
        """Load a table from the database"""
        return pd.read_sql_table(table_name, self.engine)
