import os
import pandas as pd
from sqlalchemy import create_engine
from utils import DataHandler
from exceptions import DataFileMissingError

class DataLoader(DataHandler):
    def __init__(self, data_dir='data', db_name='assignment.db'):
        super().__init__(data_dir)
        self.db_path = os.path.join(self.data_dir, db_name)
        self.engine = create_engine(f"sqlite:///{self.db_path}")

    def load_csv(self, filename):
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise DataFileMissingError(f"Data file {filename} is missing in the directory {self.data_dir}.")
        return pd.read_csv(path)

    def save_dataframe(self, df, table_name):
        df.to_sql(table_name, self.engine, index=False, if_exists='replace')

    def load_all_data(self):
        ideal_file = "ideal.csv"
        test_file = "test.csv"
        
        training_file = self.load_csv("train.csv")
        training_file.columns = ['x', 'y1', 'y2', 'y3', 'y4']

        ideal_df = self.load_csv(ideal_file)
        test_df = self.load_csv(test_file)

        self.save_dataframe(training_file, "training_data")
        self.save_dataframe(ideal_df, "ideal_functions")
        self.save_dataframe(test_df, "test_data")

        print("[INF] All datasets loaded and saved to the database.")
        return training_file, ideal_df, test_df
