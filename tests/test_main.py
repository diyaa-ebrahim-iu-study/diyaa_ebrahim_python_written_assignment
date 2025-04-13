from src.data_loader import DataLoader
from src.model_finder import ModelFinder
from src.matcher import Matcher

# Load CSV files into DataFrames
def test_data_loader_success():
    loader = DataLoader()
    training_df, ideal_df, test_df = loader.load_all_data()

    assert not training_df.empty, "Training data should not be empty"
    assert not ideal_df.empty, "Ideal function data should not be empty"
    assert not test_df.empty, "Test data should not be empty"

# Ensure 4 matches are returned by model finder
def test_model_finder_matches_count():
    loader = DataLoader()
    training_df, ideal_df, _ = loader.load_all_data()

    finder = ModelFinder(training_df, ideal_df)
    matches = finder.find_best_matches()

    assert isinstance(matches, dict)
    assert len(matches) == 4, "Should match exactly 4 training functions"

# Ensure test points get matched
def test_matcher_results():
    loader = DataLoader()
    training_df, ideal_df, test_df = loader.load_all_data()

    finder = ModelFinder(training_df, ideal_df)
    matches = finder.find_best_matches()

    matcher = Matcher(test_df, ideal_df, matches, training_df)
    matched_df = matcher.match_test_points()

    assert not matched_df.empty, "Matched DataFrame should not be empty"
    assert "x" in matched_df.columns
    assert "y" in matched_df.columns
    assert "delta_y" in matched_df.columns
    assert "ideal_func" in matched_df.columns
