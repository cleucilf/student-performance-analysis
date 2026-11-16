import pandas as pd

def load_data(file):
    df = pd.read_csv(file)

    # check for duplicates and drop null values
    df[df.duplicated()]
    df.dropna(how='any')

    # drop any rows with invalid studytime or G3 values
    df.drop(df[1 > df['studytime']].index)
    df.drop(df[4 < df['studytime']].index)
    df.drop(df[0 > df['G3']].index)
    df.drop(df[20 < df['G3']].index)

    # convert mislabeled booleans into strings
    df['schoolsup'] = df['schoolsup'].replace({'yes': True, 'no': False}).astype(bool)
    df['famsup'] = df['famsup'].replace({'yes': True, 'no': False}).astype(bool)
    df['paid'] = df['paid'].replace({'yes': True, 'no': False}).astype(bool)
    df['activities'] = df['activities'].replace({'yes': True, 'no': False}).astype(bool)
    df['nursery'] = df['nursery'].replace({'yes': True, 'no': False}).astype(bool)
    df['higher'] = df['higher'].replace({'yes': True, 'no': False}).astype(bool)
    df['internet'] = df['internet'].replace({'yes': True, 'no': False}).astype(bool)
    df['romantic'] = df['romantic'].replace({'yes': True, 'no': False}).astype(bool)

    return df


load_data("student-mat.csv")
