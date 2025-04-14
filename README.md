# Data Matching and Function Approximation for Health Metrics Using Python

This repository contains the final project submitted for the Programming with Python (DLMDSPWP01) course at IU International University of Applied Sciences. It demonstrates the use of least squares approximation for function matching, supported by Python data processing, database integration, and visualization tools.

## Project Context

This project was developed as part of the M.Sc. Computer Science program. It demonstrates practical application of numerical methods for data matching and visualization, with a focus on modular Python development, testing, and reproducibility. The included datasets were provided as part of the assignment and used without modification.

## Features

- Loads training, test, and ideal function data from CSV files
- Matches training functions to ideal functions using least squares deviation
- Maps test data points to best-matched ideal functions within a deviation threshold
- Saves output data to a SQLite database using SQLAlchemy
- Generates interactive plots using Bokeh for:
  - Training vs. Ideal function comparison
  - Mapped test points and their ideal functions
- Includes automated unit tests using pytest

## Repository Structure

```
├── src/                # Python source code
│   ├── main.py         # Main execution script
│   ├── data_loader.py  # Loads and saves data
│   ├── model_finder.py # Matches training to ideal functions
│   ├── matcher.py      # Maps test data to ideal functions
│   ├── visualizer.py   # Plots results using Bokeh
│   ├── database.py     # Handles SQLite operations
│   └── utils.py        # Optional helper functions
├── data/               # Provided datasets and output database
├── outputs/            # Generated HTML visualizations
├── tests/              # Unit test modules
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:

   - On Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows (CMD):
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

   - On Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the program:
    ```bash
    python src/main.py
    ```

6. Run tests:
    ```bash
    pytest tests/
    ```

## Output Files

- `outputs/training_vs_ideal.html` – Comparison of training and ideal functions
- `outputs/test_matches.html` – Visualization of matched test points
- `data/assignment.db` – SQLite database storing mapped test results

## Report

The final academic report explaining the methodology, theoretical background, and implementation is available as a separate document. 

## Author

Diyaa Ebrahim  
Matriculation Number: 92126545  
IU International University of Applied Sciences