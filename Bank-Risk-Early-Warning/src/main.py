from data_preprocessing import load_data, clean_data, feature_engineering
from train_model import train_model
from kri_monitoring import calculate_kri, evaluate_kri
from alert_engine import generate_alert
from report_generator import create_report

DATA_PATH = ("data/cs-training.csv")

def run_pipeline():
    print("Preprocessing data...")
    df = load_data(DATA_PATH)
    df = clean_data(df)
    df = feature_engineering(df)
    df = train_model(df)
    print("Calculating KRIs...")
    metrics = calculate_kri(df)
    results = evaluate_kri(metrics)
    print("Generating alerts...")
    alerts = generate_alert(results)
    print("Creating report...")
    create_report(results, alerts)
    print("Process complete.")

if __name__ == "__main__":
    run_pipeline()