# Overview

This Project solves the Python assignment for the course. It:
    - Loads trainging, test and ideal function data from CSV files.
    - Finds the best matching ideal functions for each training functiona using least squares. 
    - Maps test data points to those ideal functions if the deviation condition is met.
    - Saves results into a SQLite database.
    - Visaulizes the results using Bokeh plots.
    - Includes unit tests to verify functionality.


## How to Run

1. Clone or download the project.
2. Navigate to the project folder.
3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv 
    source venv/bin/activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the program:
    ```bash
    python src/main.py
    ```
6. Run Tests
    ```bash
    PYTHONPATH=.pytest tests/
    ```

## Output Files
    Output Files
    - training_vs_ideal.html -> Plots training vs. ideal functions
    - test_matches.html -> Shows which test points were assigned to ideal functions
    - assignment.db -> SQLite database with 3 tables
    
## Author

Diyaa Ebrahim  

