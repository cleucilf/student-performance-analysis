import pandas as pd


def analyze_studytime(df):
    """
    analyze studytime
    :param df: A pandas DataFrame containing the studytime and G3 columns.
    :return: A pandas DataFrame with one row per study-time category and columns for count, mean, median, and standard deviation.
    """
    # row for each student, first col studytime, second col G3
    s = time_groups(df)

    s1 = s[0]
    s2 = s[1]
    s3 = s[2]
    s4 = s[3]

    outdf = pd.DataFrame(
        {
            "count":    [s1.count(), s2.count(), s3.count(), s4.count()],
            "mean":     [s1.mean(), s2.mean(), s3.mean(), s4.mean()],
            "median":   [s1.median(), s2.median(), s3.median(), s4.median()],
            "std dev":  [s1.std(), s2.std(), s3.std(), s4.std()],
            "minimum":  [s1.min(), s2.min(), s3.min(), s4.min()],
            "maximum":  [s1.max(), s2.max(), s3.max(), s4.max()],
            "Q1":       [s1.quantile(0.25), s2.quantile(0.25), s3.quantile(0.25), s4.quantile(0.25)],
            "Q3":       [s1.quantile(0.75), s2.quantile(0.75), s3.quantile(0.75), s4.quantile(0.75)],
            "IQR":      [s1.quantile(0.75) - s1.quantile(0.25), s2.quantile(0.75) - s2.quantile(0.25), s3.quantile(0.75) - s3.quantile(0.25), s4.quantile(0.75) - s4.quantile(0.25)]
        }
    )

    outdf.index = ["<2 hr", "2-5 hr", "5-10 hr", ">10 hr"]

    return outdf

def time_groups(df):
    """
    Splits the data into series for the 4 time groups.
    :param df: A pandas DataFrame containing the studytime and G3 columns.
    :return: tuple of 4 pandas series for each time group
    """

    s1 = df.loc[df["studytime"] == 1, "G3"]
    s2 = df.loc[df["studytime"] == 2, "G3"]
    s3 = df.loc[df["studytime"] == 3, "G3"]
    s4 = df.loc[df["studytime"] == 4, "G3"]

    return s1, s2, s3, s4

def pearson(df):
    """
    performs pearson correlation
    :param df: A pandas DataFrame containing the studytime and G3 columns.
    :return: Pearson correlation
    """
    return df.corr(method="pearson")["studytime"]["G3"]

def spearman(df):
    """
    performs spearman correlation
    :param df: A pandas DataFrame containing the studytime and G3 columns.
    :return: Spearman correlation
    """
    return  df.corr(method="spearman")["studytime"]["G3"]

def kendall(df):
    """
    performs kendall correlation
    :param df: A pandas DataFrame containing the studytime and G3 columns.
    :return: Kendall correlation
    """
    return df.corr(method="kendall")["studytime"]["G3"]
