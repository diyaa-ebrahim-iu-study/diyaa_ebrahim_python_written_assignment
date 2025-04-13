from data_loader import DataLoader
from model_finder import ModelFinder
from matcher import Matcher
from database import DatabaseManager
from visualizer import Visualizer
from exceptions import DataFileMissingError

def main():

    print("[INF] Starting")
    try:
        # Load and store data
        loader = DataLoader()
        training_df, ideal_df, test_df = loader.load_all_data()
        # Find best match ideal functions
        model_finder = ModelFinder(training_df, ideal_df)
        match_map = model_finder.find_best_matches()

        # Match test data to ideal functions
        matcher = Matcher(test_df, ideal_df, match_map, training_df)
        matched_df = matcher.match_test_points()

        # Save matched test data to DB
        db = DatabaseManager()
        db.save_to_table(matched_df, "test_results")

        # Generate visualizations
        viz = Visualizer()
        viz.plot_training_vs_ideal(training_df, ideal_df, match_map)
        viz.plot_test_matches(matched_df)

        print("[INF] Finished. All results saved in [outputs] and the [database]")

        print_summary(match_map, matched_df)
    except DataFileMissingError as ex:
        print(f"[ERR] {ex}")
    except Exception as ex:
        print(f"[ERR] An unexpected error occurred: {ex}")

def print_summary(match_map, matched_df):
    print(f"\n[INT] Best Matches: {match_map}")
    print(f"[INT] Matched Test Data: \n{matched_df.head()}")
if __name__ == "__main__":
    main()
