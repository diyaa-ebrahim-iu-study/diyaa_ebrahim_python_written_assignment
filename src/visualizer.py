from bokeh.plotting import figure, output_file, save
from bokeh.models import Legend
import pandas as pd
import os

class Visualizer:
    def __init__(self, output_dir="outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def plot_training_vs_ideal(self, training_df, ideal_df, match_map):
        p = figure(title="Training vs Ideal Functions", x_axis_label='x', y_axis_label='y', width=900, height=400)
        colors = ["blue", "green", "orange", "purple"]
        legend_items = []

        for i, (train_col, ideal_col) in enumerate(match_map.items()):
            # Plot training data
            p.scatter(training_df['x'], training_df[train_col], size=5, color=colors[i], alpha=0.6)
            # Plot matching ideal function
            p.line(ideal_df['x'], ideal_df[ideal_col], line_width=2, color=colors[i])
            legend_items.append((f"{train_col} vs {ideal_col}",))

        output_file(os.path.join(self.output_dir, "training_vs_ideal.html"))
        save(p)
        print("[INF] training_vs_ideal.html saved.")

    def plot_test_matches(self, test_matches_df):
        p = figure(title="Test Points Mapped to Ideal Functions", x_axis_label='x', y_axis_label='y', width=900, height=400)

        colors = ["blue", "green", "orange", "purple", "red", "pink", "brown", "teal"]
        unique_funcs = test_matches_df['ideal_func'].unique()
        color_map = {func: colors[i % len(colors)] for i, func in enumerate(unique_funcs)}

        for func in unique_funcs:
            df = test_matches_df[test_matches_df['ideal_func'] == func]
            p.scatter(df['x'], df['y'], size=6, color=color_map[func], alpha=0.7, legend_label=func)

        p.legend.title = "Ideal Function"
        output_file(os.path.join(self.output_dir, "test_matches.html"))
        save(p)
        print("[INF] test_matches.html saved.")