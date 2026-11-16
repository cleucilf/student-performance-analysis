from pathlib import Path
from data_preparation import load_data

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "student-mat.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    # Load data
    # Run statistical analysis
    # Generate visualizations


if __name__ == "__main__":
    main()