import numpy as np
import pandas as pd

class Matcher:
    def __init__(self, test_df: pd.DataFrame, ideal_df: pd.DataFrame, best_matches: dict, training_df: pd.DataFrame):
        self.test_df = test_df
        self.ideal_df = ideal_df.set_index('x')
        self.best_matches = best_matches
        self.training_df = training_df.set_index('x')
        self.matched_results = []

    def get_max_training_deviations(self):
        """Calculate max deviation for each training vs ideal pair"""
        max_devs = {}
        for train_col, ideal_col in self.best_matches.items():
            devs = abs(self.training_df[train_col] - self.ideal_df[ideal_col])
            max_devs[train_col] = devs.max()
        return max_devs

    def match_test_points(self):
        max_devs = self.get_max_training_deviations()

        for _, row in self.test_df.iterrows():
            x, y_test = row['x'], row['y']
            best_match = None
            min_delta = float('inf')

            for train_col, ideal_col in self.best_matches.items():
                try:
                    y_ideal = self.ideal_df.loc[x, ideal_col]
                    deviation = abs(y_test - y_ideal)
                    threshold = max_devs[train_col] * np.sqrt(2)

                    if deviation <= threshold and deviation < min_delta:
                        best_match = ideal_col
                        min_delta = deviation
                except KeyError:
                    continue  # x not found in ideal_df

            if best_match:
                self.matched_results.append({
                    "x": x,
                    "y": y_test,
                    "delta_y": round(min_delta, 6),
                    "ideal_func": best_match
                })

        return pd.DataFrame(self.matched_results)
