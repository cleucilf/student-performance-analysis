from statistical_analysis import analyze_studytime
from visualizations import boxplot, stackedBarPlot
from pathlib import Path
from data_preparation import load_data
from statistical_analysis import analyze_studytime, pearson, spearman

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "student-mat.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    # Check if the dataset exists
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    # Print the header and research question
    print("=" * 60)
    print("STUDENT ACADEMIC PERFORMANCE ANALYSIS")
    print("=" * 60)
    print("\nResearch Question:")
    print("Is weekly study time associated with final mathematics grades?")
    print("\n[1/4] Loading and preparing student data...")
    
    # Load and prepare the data
    df = load_data(DATA_PATH)
    print("Dataset loaded successfully!")
    print(f"Students: {df.shape[0]}")
    print(f"Features: {df.shape[1]}")

    # Display the first few rows of the dataset
    print("\n[2/4] Analyzing student performance by study time...")
    analysis_df = df[["studytime", "G3"]]
    results = analyze_studytime(analysis_df)
    print("\nDescriptive Statistics:")
    print(results.round(2))

    # Display the correlation results
    print("\n[3/4] Measuring the association between study time and grades...")
    print(f"Pearson correlation:  {pearson(analysis_df):.4f}")
    print(f"Spearman correlation: {spearman(analysis_df):.4f}")
    print("\nInterpretation:")
    print("The results suggest a very weak positive association.")
    print("This does not establish that studying more causes higher grades.")

    # Generate visualizations
    print("\n[4/4] Generating visualizations...")
    boxplot(
        analysis_df,
        CHARTS_DIR / "student_studytime_boxplot.png"
    )

    stackedBarPlot(
        analysis_df,
        CHARTS_DIR / "student_studytime_grade_distribution_stacked_bar.png"
    )

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()