import pandas as pd

class ModelFinder:
    def __init__(self, training_df: pd.DataFrame, ideal_df: pd.DataFrame):
        self.training_df = training_df
        self.ideal_df = ideal_df
        self.match_result = {}

    def find_best_matches(self):
        training_ys = self.training_df.drop(columns='x')
        ideal_ys = self.ideal_df.drop(columns='x')

        for train_col in training_ys.columns:
            best_match = None
            lowest_error = float('inf')

            for ideal_col in ideal_ys.columns:
                error = ((training_ys[train_col] - ideal_ys[ideal_col]) ** 2).sum()

                if error < lowest_error:
                    lowest_error = error
                    best_match = ideal_col

            self.match_result[train_col] = best_match
            print(f"[INF] Best match for {train_col}: {best_match} (Error: {lowest_error:.2f})")

        return self.match_result
