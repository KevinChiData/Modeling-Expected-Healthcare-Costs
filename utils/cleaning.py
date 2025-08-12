import pandas as pd

# Used to reduce clutter in the main notebook.
def create_age_groups(df):
    df['AGEGROUP'] = pd.cut(df['AGE42X'], bins = [0, 10, 20, 30, 40, 50, 60, 70, 100], labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+'])
    return df