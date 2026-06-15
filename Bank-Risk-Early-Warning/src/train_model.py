import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import os

FILE_PATH = "model/model.pkl"

def train_model(df):
    print("Training model...")
    X = df.drop('SeriousDlqin2yrs', axis=1)
    y = df["SeriousDlqin2yrs"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    if os.path.exists(FILE_PATH):
        model = joblib.load("model/model.pkl")
    else:
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        joblib.dump(model, FILE_PATH)
    probabilities = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, probabilities)
    print(f"AUC Score: {auc:.3f}")
    df_pred = pd.concat([X_test, y_test], axis=1)
    df_pred["default_probability"] = probabilities
    df_pred["risk_score"] = (probabilities * 100).round(0)
    df_pred.to_csv("data/data_predicted.csv")
    return df_pred