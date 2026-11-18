from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def boxplot(df, output_path):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    sns.boxplot(
        x="studytime",
        y="G3",
        data=df,
        palette="muted",
        hue="studytime",
        legend=False,
    )

    plt.title("Box Plot of Final Grades (G3) by Study Time", fontsize=14)
    plt.xlabel(
        "Weekly Study Time (1: <2 hrs, 2: 2-5 hrs, 3: 5-10 hrs, 4: >10 hrs)",
        fontsize=12,
    )
    plt.ylabel("Final Grade (G3)", fontsize=12)

    plt.tight_layout()
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file, dpi=200)
    print(f"Plot saved to: {output_file}")
    plt.show()

    return output_path


def stackedBarPlot(df, output_path):
    bins = [-1, 9, 13, 16, 20]
    labels = ["Fail (0-9)", "Pass (10-13)", "Good (14-16)", "Excellent (17-20)"]
    grade_categories = pd.cut(df["G3"], bins=bins, labels=labels)

    distribution_df = (
        pd.crosstab(df["studytime"], grade_categories, normalize="index") * 100
    )

    ax = distribution_df.plot(
        kind="bar",
        stacked=True,
        figsize=(10, 6),
        colormap="viridis",
        edgecolor="black",
    )

    plt.title("Distribution of Grade Categories across Study Time Groups", fontsize=14)
    plt.xlabel(
        "Weekly Study Time (1: <2 hrs, 2: 2-5 hrs, 3: 5-10 hrs, 4: >10 hrs)",
        fontsize=12,
    )
    plt.ylabel("Percentage of Students (%)", fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title="Grade Category", bbox_to_anchor=(1.05, 1), loc="upper left")

    for patch in ax.patches:
        width, height = patch.get_width(), patch.get_height()
        x, y = patch.get_xy()
        if height > 0:
            ax.annotate(
                f"{height:.1f}%",
                (x + width / 2, y + height / 2),
                ha="center",
                va="center",
                color="white",
                fontweight="bold",
                fontsize=10,
            )

    plt.tight_layout()
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_file, dpi=200)
    print(f"Plot saved to: {output_file}")
    plt.show()

    return output_path
