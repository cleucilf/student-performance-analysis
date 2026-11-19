from statistical_analysis import analyze_studytime
from pathlib import Path
from data_preparation import load_data

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "student-mat.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
    
    df = load_data(DATA_PATH)
    analysis_df = df[["studytime", "G3"]]
    results = analyze_studytime(analysis_df)
    print(results)
    # Generate visualizations


if __name__ == "__main__":
    main()