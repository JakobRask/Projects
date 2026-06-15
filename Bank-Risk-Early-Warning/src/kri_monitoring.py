import yaml

def load_thresholds():
    with open(
        "config/risk_thresholds.yml",
        "r"
    ) as file:
        return yaml.safe_load(file)

def classify(value, green, amber):
    if value <= green:
        return "GREEN"
    if value <= amber:
        return "AMBER"
    return "RED"

def calculate_kri(df):
    default_rate = (df["SeriousDlqin2yrs"].mean()* 100)
    delinquency_rate = (df["late_payment_flag"].mean()* 100)
    # high_risk_customers = df.loc[df["risk_score"] > 15].shape[0]
    return {
        "default_rate": default_rate,
        "delinquency_rate": delinquency_rate
    }

def evaluate_kri(metrics):
    thresholds = load_thresholds()
    output = {}
    for metric, value in metrics.items():
        output[metric] = {
            "value": round(value, 2),
            "status": classify(
                value,
                thresholds[metric]["green"],
                thresholds[metric]["amber"]
            )
        }
    return output