import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    return df

def clean_data(df):
    # Handle missing values
    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
    df["NumberOfDependents"] = df["NumberOfDependents"].fillna(df["NumberOfDependents"].median())
    # Cap extreme values
    df["DebtRatio"] = df["DebtRatio"].clip(upper=5)
    df["RevolvingUtilizationOfUnsecuredLines"] = df["RevolvingUtilizationOfUnsecuredLines"].clip(upper=2)
    return df

def feature_engineering(df):
    df["income_to_debt"] = df["MonthlyIncome"] / (df["DebtRatio"] + 1)
    df["late_payment_flag"] = (df["NumberOfTime30-59DaysPastDueNotWorse"] > 0).astype(int)
    df["age_group"] = pd.cut(df["age"], bins=[20,30,40,50,60,100])
    df = pd.get_dummies(df, columns=["age_group"], drop_first=True)
    return df