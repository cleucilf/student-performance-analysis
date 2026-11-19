from statistical_analysis import analyze_studytime
from visualizations import boxplot, stackedBarPlot
from pathlib import Path
from data_preparation import load_data

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "student-mat.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    # Check if the dataset exists
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
    
    # Load and prepare the data
    df = load_data(DATA_PATH)
    analysis_df = df[["studytime", "G3"]]
    results = analyze_studytime(analysis_df)
    print(results)

    # Generate visualizations
    boxplot(
        analysis_df,
        CHARTS_DIR / "student_studytime_boxplot.png"
    )

    stackedBarPlot(
        analysis_df,
        CHARTS_DIR / "student_studytime_grade_distribution_stacked_bar.png"
    )

if __name__ == "__main__":
    main()